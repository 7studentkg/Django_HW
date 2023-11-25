from django.db import models



class Category(models.Model):
    title = models.CharField(max_length = 150)


class Product(models.Model):
    image = models.ImageField(upload_to = 'product', null = True, blank = True)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    rate = models.FloatField(default = 0)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'category')


    def __str__ (self):
        return f'{self.id} {self.title}'
