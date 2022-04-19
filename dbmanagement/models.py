from sre_constants import CATEGORY_NOT_LINEBREAK
from django.db import models
from django.conf import settings

# Create your models here.

class Db(models.Model):
    HEREDIS = 'HEREDIS'
    CALIBRE = 'CALIBRE'

    ROLE_CHOICES = (
        (HEREDIS, 'Heredis'),
        (CALIBRE, 'Calibre'),
    )
    
    file = models.FileField(upload_to='db/')
    software = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='logiciel')
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)