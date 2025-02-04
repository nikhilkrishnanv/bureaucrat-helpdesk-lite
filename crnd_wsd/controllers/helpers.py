import io
import os
import json
import base64
import logging
from PIL import Image
from werkzeug.urls import url_quote

from odoo import http, tools, _
from odoo.tools import ustr
from odoo.http import request

from .controller_mixin import WSDControllerMixin

_logger = logging.getLogger(__name__)


class WSDHelpers(WSDControllerMixin, http.Controller):

    def _optimize_image(self, image_data, disable_optimization=False):
        try:
            image = Image.open(io.BytesIO(image_data))
            w, h = image.size
            if w * h >= 42e6:  # Nokia Lumia 1020 photo resolution
                raise ValueError(_(
                    u"Image size excessive, uploaded images "
                    u"must be smaller than 42 million pixel"))
            if not disable_optimization and image.format in ('PNG', 'JPEG'):
                image_data = tools.image_save_for_web(image)
        except IOError:  # pylint: disable=except-pass
            pass
        return image_data

    def _get_max_upload_size(self):
        """ Get configuration for max upload size
        """
        return request.env.user.company_id._get_request_max_upload_file_size()

    @http.route('/crnd_wsd/file_upload', type='http',
                auth='user', methods=['POST'], website=True)
    def wsd_upload_file(self, upload, alt='File', filename=None,
                        is_image=False, **post_data):
        Attachments = request.env['ir.attachment'].sudo()
        attachment_data = {
            'name': alt,
            # TODO: How to use file type checking for case 'upload'?
            'datas_fname': filename or 'upload',
            'public': False,
        }

        if post_data.get('request_id'):
            try:
                attachment_data['res_id'] = int(post_data.get('request_id'))
            except (ValueError, TypeError):
                _logger.debug(
                    "Cannon convert request_id %r",
                    post_data.get('request_id'),
                    exc_info=True)
            else:
                attachment_data['res_model'] = 'request.request'

        # Check max filesize and return error if file is too big
        upload.seek(0, os.SEEK_END)
        file_size = upload.tell()
        max_size = self._get_max_upload_size()
        if max_size and file_size > max_size:
            _logger.warning(
                "File size is too big: %s > %s", file_size, max_size)
            return json.dumps({
                'status': 'FAIL',
                'success': False,
                'message': _(
                    "File size is too big!"),
            })
        upload.seek(0, os.SEEK_SET)

        try:
            data = upload.read()

            if is_image:
                data = self._optimize_image(data, disable_optimization=False)

            attachment = Attachments.create(dict(
                attachment_data,
                datas=base64.b64encode(data),
            ))
        except Exception as e:
            _logger.exception("Failed to upload file to attachment")
            message = ustr(e)
            return json.dumps({
                'status': 'FAIL',
                'success': False,
                'message': message,
            })

        attachment.generate_access_token()
        if is_image:
            attachment_url = "%s?access_token=%s" % (
                url_quote("/web/image/%d/%s" % (
                    attachment.id,
                    attachment.datas_fname)),
                attachment.sudo().access_token,
            )
        else:
            attachment_url = "%s?access_token=%s&download" % (
                url_quote("/web/content/%d/%s" % (
                    attachment.id,
                    attachment.datas_fname)),
                attachment.sudo().access_token,
            )

        return json.dumps({
            'status': 'OK',
            'success': True,
            'attachment_url': attachment_url,
        })

    @http.route('/crnd_wsd/api/request/update-text', type='json',
                auth='user', methods=['POST'], website=True)
    def wsd_request_update_text(self, request_id, request_text):
        try:
            reqs = self._id_to_record('request.request', request_id)
            reqs.ensure_one()
        except Exception as exc:
            return {
                'error': _("Access denied"),
                'debug': ustr(exc),
            }

        if not reqs.can_change_request_text:
            return {
                'error': _("Access denied"),
            }

        try:
            reqs.request_text = request_text
        except Exception as exc:
            return {
                'error': _("Access denied"),
                'debug': ustr(exc),
            }

        return {
            'request_text': reqs.request_text,
        }

    @http.route('/crnd_wsd/api/request/do-action', type='json',
                auth='user', methods=['POST'], website=True)
    def wsd_request_actions(self, request_id, action_id, response_text=None):
        try:
            reqs = self._id_to_record('request.request', request_id)
            reqs.ensure_one()

            action_route = request.env['request.stage.route'].search([
                ('website_published', '=', True),
                ('stage_from_id', '=', reqs.sudo().stage_id.id),
                ('request_type_id', '=', reqs.sudo().type_id.id),
                ('id', '=', int(action_id)),
            ])
            action_route.ensure_one()
            action_route.check_access_rights('read')
            action_route.check_access_rule('read')
        except Exception as exc:
            return {
                'error': _("Access denied"),
                'debug': ustr(exc),
            }

        try:
            if (action_route.close and
                    action_route.require_response and response_text):
                reqs.response_text = response_text
            reqs.stage_id = action_route.stage_to_id
        except Exception as exc:
            return {
                'error': _("Access denied"),
                'debug': ustr(exc),
            }

        return {
            'status': 'ok',
            'extra_action': action_route.website_extra_action,
        }
