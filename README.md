# Basic Authentication and social authentication

create virtual environment
install requirements

cd core/

use application

**social authentication not finised because it asks to buy google cloud service i.e OAUTH2, which we can try by creating new gmail id for practice purpose**


For the project documentation
https://testdriven.io/blog/django-rest-auth/


for smtp gmail setup refer below video,
https://www.youtube.com/watch?v=Mezha1p_dTE&t=140s

Google,Github,facebook signup & Login
https://youtu.be/GQySb3W2feo?si=A_cqkLDvwFb65NAg


You can use your own SMTP server or utilize Brevo (formerly SendInBlue), Mailgun, SendGrid, or a similar service. I suggest you go with Brevo since they're relatively cheap and allow you to send a decent amount of emails daily (for free).


Future steps
* Consider swapping token authentication with djangorestframework-simplejwt or django-rest-knox. They provide further configuration options and are more * secure.
* To add another social provider such as Twitter or GitHub, take a look the at dj-rest-auth docs.
* To enable social account linking functionality, look into "Social Connect Views".
* To use the backend with a JavaScript-based frontend you'll most likely want to set up CORS headers via django-cors-headers.
