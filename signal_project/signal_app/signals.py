from django.contrib.auth.models import User
from signal_app.models import Profile
from django.db.models.signals import post_save,pre_save, pre_delete,post_delete
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('****************')
        print('Profile created!')
        print('****************')


# post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created is False:
        instance.profile.save()
        print('****************')
        print('Profile Updated!')
        print('****************')


# post_save.connect(update_profile, sender=User)

@receiver(pre_save, sender=Profile)
def before_profile_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = 'This is a default bio text.'
        print('****************')
        print('Profile pre-save: default bio set.')
        print('****************')


# @receiver(pre_delete, sender=Profile)
# def before_profile_delete(sender, instance, **kwargs):
#     print('Profile is about to be deleted!')

# @receiver(post_delete, sender=Profile)
# def after_profile_delete(sender, instance, **kwargs):
#     print('Profile has been deleted!')