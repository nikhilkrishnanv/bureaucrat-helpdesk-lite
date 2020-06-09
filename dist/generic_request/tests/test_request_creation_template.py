from odoo.tests.common import SavepointCase


class TestRequestCreationTemplate(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestRequestCreationTemplate, cls).setUpClass()
        cls.template = cls.env.ref(
            'generic_request.demo_request_creation_template')

    def test_request_creation_template(self):
        request = self.template.do_create_request({})
        self.assertEqual(
            request.category_id, self.template.request_category_id)
        self.assertEqual(request.type_id, self.template.request_type_id)
        self.assertEqual(request.request_text, self.template.request_text)
