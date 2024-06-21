Django signals:

Built-in Signals:



Django provides several built-in signals, including:
    • django.db.models.signals.pre_save and post_save: Sent before or after a model’s save() method is called.

    • django.db.models.signals.pre_delete and post_delete: Sent before or after a model’s delete() method is called.https://getbootstrap.com/docs/5.3/components/navbar/

    • django.core.signals.request_started and request_finished: Sent when a request starts or finishes.

    • django.core.signals.got_request_exception: Sent when an exception is raised during request processing.
    
    • django.contrib.auth.signals.user_logged_in, user_logged_out, and user_login_failed: Sent during user authentication event




Refer:
https://medium.com/jungletronics/how-django-signals-work-81dc30d0dad5




for clear undestanding:
https://www.google.com/search?sca_esv=19780ec8fcf2a1b8&sca_upv=1&sxsrf=ADLYWIIgyBMU6hY9hQReX_i1YKN_XISdZg:1718944038077&q=django+signals+and+their+usage&tbm=vid&source=lnms&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3J_86uWOeqwdnV0yaSF-x2joZDvir2QxhZkTA8rK1etu4ohtqlTKXOQ56HmFa2r_epndM3O_Pg3eZzqhmskTYrDUq4znXDBd7PoLKI2b-P6R2amGrM44CRlQMbguMhFtgOaBlL37-_CLULp7cXd_6eCm2Q0jd&sa=X&ved=2ahUKEwiV4JzG7euGAxVHxzgGHbG6DCEQ0pQJegQIDRAB&biw=1164&bih=551&dpr=1.1#fpstate=ive&vld=cid:2bbe206f,vid:rEX50LJrFuU,st:0