# pyMail
This script will send an email to  a specific addredd (multiple address soon).
It aims to be an automatic process without a user interface, for ex you can put this on a raspberry pi crontab and it will do the magic.

Stay tuned.
--

## -- TODO:
* [x] Change get_http_status server params to use function dynamically

### -- New Features:
* [x] The script will recognize automatically wich smtp server he need to send the email
* [ ] Set configuration params in a dotenv file
* [ ] Handle various request to provider exceptions
* [ ] Set first argument for subject and second for email body 
  * [ ] If no arguments passed, use default SUBJECT and BODY 
  
