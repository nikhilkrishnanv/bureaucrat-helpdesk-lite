# Changelog

## Release (2021-May-28 16:02:43)

### Updated addons:

- crnd_wsd (12.0.1.53.0 -> 12.0.1.62.0)
- generic_request (12.0.1.99.0 -> 12.0.1.114.0)

### Notable changes:

#### crnd_wsd
##### Version 1.54.0

- Changeg *UploadFile* icon in text editor.
  Now this button has icon *paperclip* + textual name *Attach file*
- Added configurable helptext, that could be displayed below request text
  on request creation form on website. This text could be configured
  on request type level (see Website Request Text Help field)


#### generic_request
##### Version 1.114.0

- Add new request events (Request Archived / Request Unarchived).
- Add filters in search view.
- Add simplet tests.


##### Version 1.112.0

- Add field `active` to model request.request.
- Add a group whose users are allowed to archive / unarchive requests.


##### Version 1.111.0

#### Version 1.111.0
Added new request event types: 'author-changed' and 'partner-changed'.
 

##### Version 1.103.0

Added global configuration, that allows to chooses if it is needed to suggest
Global CC as recipients of request


##### Version 1.101.0

- Add `email_cc` data to suggested recipients.
- Add global option that allows to automatically create partners,
  if request created from incoming email, and author of email and cc of email
  are not present in odoo's contacts database




## Release (2021-Jan-18 13:28:00)

### Updated addons:

- crnd_wsd (12.0.1.47.0 -> 12.0.1.53.0)
- generic_request (12.0.1.80.1 -> 12.0.1.99.0)

### Notable changes:

#### crnd_wsd
##### Version 1.50.0

Added mult-site support for requests


#### generic_request
##### Version 1.99.0

Add global setting that could be used to show/hide request statistics on kanban views of
request-related objects like Request Category, Request type, etc


##### Version 1.89.0

Now requests created via xml-RPC or json RPC will get *API* channel automatically
(if not provided in creation parameters)


##### Version 1.85.0

- Added new search filters for requests
    - Today
    - 24 hours
    - Week
    - Month
    - Year
- Added new group by filters for request's search view
    - Assignee
    - Is Closed
- Added request statistics (requests open/closed for today, 24h, week, etc) to
  following models:
    - Request Type
    - Request Category
    - Request Channel
    - Request Kind


##### Version 1.84.0

Added *Requests* page to user form view, that is used to display request statistics for user.


##### Version 1.83.0

Added button to generate default stages and route on request type that has no
request stages.


##### Version 1.81.0

Added new request event types:
- Timetracking / Start Work
- Timetracking / Stop Work




## Release (2020-Sep-09 12:08:53)

### Updated addons:

- bureaucrat_helpdesk_lite (12.0.1.1.0 -> 12.0.1.2.0)
- crnd_wsd (12.0.1.41.1 -> 12.0.1.47.0)
- generic_request (12.0.1.62.0 -> 12.0.1.80.1)

### Notable changes:

#### crnd_wsd
##### Version 1.47.0

Automatically set channel to Website for requests created from website


#### generic_request
##### Version 1.72.0

Added new request stage type 'Progress'


##### Version 1.70.0

Added new field Channel to request. The field could be used to determine source of request Website / Web / Mail / Other
Automatically set correct channels for requests created from Web and E-mail


##### Version 1.68.0

Remove obsolete modules from settings page.
Obsolte modules are:
- `generic_request_action_condition`


##### Version 1.67.0

Added *kanban_state* feature to requests.
Now it is possible to define additional Blocked or Ready states on request.
Also, changes of kanban state triggers event *Kanban State*




## Release (2020-Jun-08 19:03:07)

### Updated addons:

- bureaucrat_helpdesk_lite (12.0.1.0.14 -> 12.0.1.1.0)
- crnd_service_desk (12.0.1.2.0 -> 12.0.1.3.0)
- crnd_wsd (12.0.1.26.0 -> 12.0.1.41.1)
- generic_request (12.0.1.40.0 -> 12.0.1.62.0)

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




## Release (2020-Jan-14 12:09:49)

### Added addons:

- bureaucrat_helpdesk_lite (12.0.1.0.14)
- crnd_service_desk (12.0.1.2.0)
- crnd_wsd (12.0.1.26.0)
- generic_request (12.0.1.40.0)

