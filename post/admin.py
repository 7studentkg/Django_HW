from django.contrib import admin
from django.http.request import HttpRequest


from post.models import Product, Category, Review


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'rate', 'create_at']
    # list_editable = ['rate']
    list_filter = ['category']
    list_per_page = 10
    search_fields = ['title', 'content', 'category__title']


    def has_add_permission(self, request):
        return True

#     # def has_delete_permission(self, request):
#     #     return True

#     # def has_change_permission(self, request ):
#     #     return True



admin.site.register(Category)
admin.site.register(Review)
