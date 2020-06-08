# Changelog

## Release (2020-Jun-08 19:03:15)

### Updated addons:

- bureaucrat_helpdesk_lite (13.0.1.0.14 -> 13.0.1.1.0)
- crnd_service_desk (13.0.0.1.0 -> 13.0.1.3.0)
- crnd_wsd (13.0.1.26.0 -> 13.0.1.41.2)
- generic_request (13.0.1.40.0 -> 13.0.1.62.1)

### Notable changes:

#### crnd_wsd
##### Version 1.40.0

- Added ability to restrict max text size of request text on website UI and
    make this configurable through global options
- Added visual information about the number of characters entered


##### Version 1.37.0

Merge with crnd_wsd_timesheet addon


##### Version 1.32.0

Use different colors for deadline icon depending on deadline value


##### Version 1.29.0

Improved file uploading from website UI.
- automatically bind uploaded files and images to created request.
- open uploaded files in new tab in browse
- download uploaded documents (instead of displaying them)



##### Version 1.28.0

Show deadline on request page and in request list


#### generic_request
##### Version 1.58.0

Merge with generic_request_timesheet module


##### Version 1.56.0

Enable *create_edit* and *quick_create* features of *author* and *partner*
fields of request 


##### Version 1.54.0

Added ability to assign multiple requests with a single operations.
Just select requests from list view and call context action *Assign*.


##### Version 1.53.0

- Automatically move created stage to the end of list of stages.
  This is required to avoid case when new stage become first one and
  thus it become starting stage for requests.
- Better support for handling mails received from unknown contacts.
  In this case `email_from` will be saved on request
- Save `email_cc` on request (if first email contains `cc`)
- Automatically subscribe partners mentioned in ``CC`` header of incoming mail
- Implement partner suggestions for mailing for requests.
  Odoo will automatically suggest to subscribe partner and / or author of request
  if that is not following request yet


##### Version 1.52.0

Use different colors for deadline icon, depending on its value.


##### Version 1.47.0

Update form view of Request Type


##### Version 1.46.0

Module `generic_request_tag` merged into `generic_request`


##### Version 1.45.0

- Intoruced new field: *Deadline*
- Small improvements to UI
- Fixed regression, missing *Kind* field on request form view


##### Version 1.44.0

Fix regression in detection of author when creator is specified directly,
but author is not specified.


##### Version 1.41.0

Introduced *Request Creation Templates* feature,
that have to be used mostly by other modules to create requests with default values.




## Release (2020-Jan-14 12:10:38)

### Added addons:

- bureaucrat_helpdesk_lite (13.0.1.0.14)
- crnd_service_desk (13.0.0.1.0)
- crnd_wsd (13.0.1.26.0)
- generic_request (13.0.1.40.0)

