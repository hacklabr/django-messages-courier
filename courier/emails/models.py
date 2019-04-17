from django.db import models
from django.conf import settings

class EmailProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='mailing_profile',
        unique=True,
    )

    active = models.BooleanField(
        default=False
    )
