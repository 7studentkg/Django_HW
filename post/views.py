from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
# from datetime import datetime

from post.models import Product, Category, Review
from post.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm


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
            'product' : product,
        }
        return render(request, 'product_detail.html', context)



def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    context = {"category": category, "products": products}
    return render(request, 'product.html', context)


def product_create(request):
    if request.method == 'GET':
        context = {
            'form' : ProductCreateForm
        }
        return render(request, 'create_p.html', context)
    if request.method == "POST":
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():  # Проверка входящих данных
            Product.objects.create(**form.cleaned_data)
                # title = form.cleaned_data['title'],
                # content = form.cleaned_data['content'],
                # image = form.cleaned_data['image'],
                # rate = form.cleaned_data['rate']

            return redirect ('/product')

        context = {
        'form' : form
        }

    return render(request, 'create_c.html', context)

def category_create(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save() # сохраняет
            return redirect('/category')

    else:
        form = CategoryCreateForm()

    context = {'form': form}
    return render(request, 'create_c.html', context)

def review_create(request):
    if request.method == 'POST':
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product')

    else:
        form = ReviewCreateForm()

    context = {'form': form}
    return render(request, 'create_r.html', context)

# def product_update_view(request, product_id):
#     product = get_object_or_404(Product, id=product_id)

#     if request.method == 'POST':
#         form = ProductCreateForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('product_detail', product_id=product_id)
#     else:
#         form = ProductCreateForm(instance=product)

#     context = {
#         'form': form,
#         'product': product,
#     }

#     return render(request, 'update.html', context)

def product_update_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')

    if request.method == "GET":
        context = {
            'form' : ProductCreateForm(instance=product)
        }
        return render(request, 'update.html', context)

    if request.method == "POST":
        form = ProductCreateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()

            return redirect(f'/product/{product_id}')

    context = {
        'form' : form
    }
    return render (request, 'product/update.html', context)

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
