from django.shortcuts import HttpResponse
from .models import Products
from django.urls import reverse
# Create your views here.

# def home_page_view(request):
#     display_page="""
#      <!DOCTYPE html>
#     <html>
#     <head>
#     <title>E_Store</title>
#     </head>
#     <body>
#     <h1>This is the homepage of our E_store</h1>
#     <p>This is the page with info about our Products</p>
#     </body>
#     </html>
#     """

#     return HttpResponse(display_page)

def home_page_view(request):
    products=Products.objects.all()
    display_page1= """
     <!DOCTYPE html>
    <html>
    <head>
    <title>E_Store</title>
    </head>
    <body>
    <h1>This is the homepage of our E_store</h1>
    <p>This is the page with info about our Products</p>
    <ol>
    """

    for i in products:
        display_page1+=f"<li>"+ i.product_name+ "</li>"

    display_page2="""
    </ol>
    </body>
    </html>
    """

    return HttpResponse(display_page1 + display_page2)


# def home_page_view(request):
#     products=Products.objects.all()
#     url_book_home_page=reverse("books_home_page")
#     """
#      <!DOCTYPE html>
#     <html>
#     <head>
#     <title>E_Store</title>
#     </head>
#     <body>
#     <h1>This is the homepage of our E_store</h1>
#     <p>This is the page with info about our Products</p>
#     <ol>
#     """

#     for i in products:
#         display_page1+=f"<li><a href ="{% url_book_home_page 'kkquit:home' %}""+ i.product_name+ "</li></a>"

#     display_page2="""
#     </ol>
#     </body>
#     </html>
#     """

#     return HttpResponse(display_page1 + display_page2)