Django signals:

Built-in Signals
Django provides several built-in signals, including:
    • django.db.models.signals.pre_save and post_save: Sent before or after a model’s save() method is called.
    • django.db.models.signals.pre_delete and post_delete: Sent before or after a model’s delete() method is called.https://getbootstrap.com/docs/5.3/components/navbar/
    • django.core.signals.request_started and request_finished: Sent when a request starts or finishes.
    • django.core.signals.got_request_exception: Sent when an exception is raised during request processing.
    • django.contrib.auth.signals.user_logged_in, user_logged_out, and user_login_failed: Sent during user authentication event
Refer:
https://medium.com/jungletronics/how-django-signals-work-81dc30d0dad5
