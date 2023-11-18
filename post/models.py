from django.db import models




class Product(models.Model):
    image = models.ImageField(upload_to = 'product', null = True, blank = True)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    rate = models.FloatField(default = 0)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
