from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        'auth.User',
        on_delete = models.CASCADE,
        related_name = 'profile'
    )

    avatar = models.ImageField(
        upload_to='avarats',
        blank=True,
        null = True
    )

    bio = models.TextField(
        blank = True,
        null = True
    )
