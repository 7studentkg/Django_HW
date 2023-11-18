from django.db import models

<<<<<<< HEAD


class Product(models.Model):
    image = models.ImageField(upload_to = 'product', null = True, blank = True)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    rate = models.FloatField(default = 0)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
=======
# Create your models here.
>>>>>>> 5cc4ba3f8366d81ac57f1c64477c59f67b462210
