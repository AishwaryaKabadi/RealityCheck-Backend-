from django.db import models


class Picture(models.Model):
    Original_Image = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    QR_Embedded_Image = models.ImageField()