# Changelog

## Release (2021-Sep-09 13:23:25)

### Updated addons:

- bureaucrat_helpdesk_lite (12.0.1.3.0 -> 12.0.1.4.0)
- crnd_wsd (12.0.1.68.0 -> 12.0.1.73.0)
- generic_request (12.0.1.123.0 -> 12.0.1.133.0)

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



