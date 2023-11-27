from django.shortcuts import render, HttpResponse, get_object_or_404
# from datetime import datetime

from post.models import Product, Category, Review


def title_page(request):

    if request.method == 'GET':
        Product.objects.all()
        return render(request, 'index.html')



def product_view(request):
     if request.method == 'GET':
        products = Product.objects.all() # QuerySet
        categories = Category.objects.all()
        reviews = Review.objects.all()

        context = {
            'products': products,
            'category' : categories,
            'reviews' : reviews,

        }

        return render(request, 'product.html', context)

def category_view(request):
    if request.method == 'GET':
        category = Category.objects.all()

        context ={
            'category' : category
        }
        return render(request, 'category.html', context)

def product_datail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id = product_id)
        except Product.DoesNotExist:
            return render (request, 'errors/404.html')

        context  = {
            'product' : product
        }


        return render(request, 'product_detail.html', context)


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    context = {"category": category, "products": products}
    return render(request, 'product.html', context)


# def hello_world(request):
#     #return HttpResponse("Hello Bruh! What's up ?")
#     if request.method == 'GET':
#         return render(request, 'hello.html')


# def current_date(request):
#     now = datetime.now()
#     context = {
#         'current_date': now.strftime("%Y-%m-%d"),
#         'current_time': now.strftime("%H:%M:%S"),
#     }
#     if request.method == 'GET':
#         return render(request, 'current_date.html', context)


# def goodby (request):
#     if request.method == 'GET':
#         return render(request, 'goodby.html')


#     if request.method == 'GET':
#         return render(request, 'index.html')
