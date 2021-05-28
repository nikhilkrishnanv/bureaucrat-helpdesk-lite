# Changelog

## Release (2021-May-28 16:07:25)

### Updated addons:

- crnd_wsd (13.0.1.53.0 -> 13.0.1.62.1)
- generic_request (13.0.1.99.0 -> 13.0.1.114.1)

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



