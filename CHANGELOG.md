# Changelog

## Release (2021-Sep-09 13:27:01)

### Updated addons:

- bureaucrat_helpdesk_lite (14.0.1.3.2 -> 14.0.1.4.0)
- crnd_wsd (14.0.1.68.0 -> 14.0.1.73.0)
- generic_request (14.0.1.123.0 -> 14.0.1.133.0)

### Notable changes:

#### crnd_wsd
##### Version 1.73.0

Added new field Access Groups on the request category / type.
If portal user belongs to one of groups mentioned in this field,
then he will be able to read this category or type.


##### Version 1.71.0

Added new option in settings, that could be used to allow unregistered users
create requests.
The only additional thing that have to be provided by unregistered user is his email and optionaly name.
To enable this option, navigate to *Requests / Configuration / Settings* and
choose *Allow to create request* in field *Website Service Desk (Public Visibility)*.
After this step, unregistered users will be able to create requests from your website


##### Version 1.70.0

Added support for new *tiles* layout for request creation process.

This setting could be enabled in *Website* settings menu
(look for *Bureaucrat Website Settings* section)

When new layout style for request creation process selected, then
Services, categories and types will be displayed as tiles (boxes) instead of
radio buttons.


##### Version 1.69.0

- Added ability to limit maximum size for uploads
- Added ability to limit file types (mime types) allowed for upload
- Improved handling of max request text symbols


#### generic_request
##### Version 1.131.0

- Do not allow to create requests from emails that come from email addresses that are aliases (managed by odoo).
  This is needed to avoid possible infinite loops when two emails start sending autoreplies to each other.
- Starting from this version in *Email* field on request, only email address will be saved.
  The author name will be saved in *Author name* field.
  Previously, author name was saved in *Author name* field, but it also was
  present in *Email* field in format ```Author name <author@email.com>```.


##### Version 1.126.0

Added I (info) button to author, partner, and user fields.
Click on this new button will shoe popover with additional info on partner/user,
that allows to easily and fast copy phone, email, or name of partner/author/user




## Release (2021-Jul-09 15:59:09)

### Updated addons:

- bureaucrat_helpdesk_lite (14.0.1.3.1 -> 14.0.1.3.2)


## Release (2021-Jul-09 15:04:47)

### Updated addons:

- bureaucrat_helpdesk_lite (14.0.1.2.0 -> 14.0.1.3.1)
- crnd_service_desk (14.0.1.3.0 -> 14.0.1.4.0)
- crnd_wsd (14.0.1.62.1 -> 14.0.1.68.0)
- generic_request (14.0.1.114.3 -> 14.0.1.123.0)

### Notable changes:

#### generic_request
##### Version 1.120.0

Show open/closed requests stat for request's partner and author




## Release (2021-May-28 16:08:52)

### Updated addons:

- crnd_wsd (14.0.1.53.0 -> 14.0.1.62.1)
- generic_request (14.0.1.99.0 -> 14.0.1.114.3)

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




## Release (2021-Jan-20 12:24:29)

### Added addons:

- bureaucrat_helpdesk_lite (14.0.1.2.0)
- crnd_service_desk (14.0.1.3.0)
- crnd_wsd (14.0.1.53.0)
- generic_request (14.0.1.99.0)

