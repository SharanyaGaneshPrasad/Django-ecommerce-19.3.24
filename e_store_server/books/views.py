from django.shortcuts import HttpResponse
from .models import books
from django.urls import reverse


def home_page_view(request):
    url = reverse("about_page")
    # url2 = reverse("players_page")
    page = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Our Team</title>
    </head>
    <body>
    <a href = "{url}">About Page</a>
    <h1>This is the homepage of our Team</h1>
    <p>This is the page with info about our team</p>
    </body>
    </html>
    """
    return HttpResponse(page)


def about_page_view(request):
    url = reverse("home_page")
    page = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Our Team</title>
    </head>
    <body>
    <a href = "{url}">Home Page</a>
    <h1>About</h1>
    <p>Contact data</p>
    </body>
    </html>
    """
    return HttpResponse(page)



# Create your views here.

# def books_home_page_view(request):
#     url = reverse("info_page")
#     display_page= f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#     <title>Our Team</title>
#     </head>
#     <body>
#     <a href = "{url}">Info Page</a>
#     <h1>This is the homepage of our Books</h1>
#     <p>This is the page with info about our Book collections</p>
#     <p> We have different genres</p>
#     <ol>
#     <li>Fantasy</li>
#     <li>Science Fiction</li>
#     <li>Biography</li>
#     <li>Horror</li>
#     <li>Historical</li>
#     </ol>
#     </body>
#     </html>

#     """
#     return HttpResponse(display_page)

# def books_info_page_view(request):
#     url= reverse('books_home_page')
#     genres=["Fantasy","Science_fiction","Biography","Horror","Historical"]
#     display_page1= """
#     <!DOCTYPE html>
#     <html>
#     <head>
#     <title>Our Team</title>
#     </head>
#     <body>
#     <h1>This Page shows different Genres</h1>
#     <ol>"""
#     for id,book in enumerate(books):
#         display_page1+=f"<p><li>"+genres[id]+"</p>"
#         display_page1+=book["name"]   
#     display_page2= """
#     </ol>
#     </body>
#     </html>"""
#     return HttpResponse(display_page1+display_page2)


# def books_info_page_view(request):
#     # url_books_home_page = reverse("books_home_page")
#     genres=["Fantasy","Science_fiction","Biography","Horror","Historical"]
#     display_page1= f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#     <title>Our Team</title>
#     </head>
#     <body>
#     <h1>This Page shows different Genres</h1>
#     <ol>"""
    
#     for id,book in enumerate(books):
#         book_link=reverse("book_details",args=[id+1])
#         display_page1+=f"<p><li>"+genres[id]+"</p>"
#         display_page1+=f"<a href={book_link}>"+book["name"] +"</a>"  
#     display_page2= f"""
#     </ol>
#     </body>
#     </html>"""
#     return HttpResponse(display_page1+display_page2)




# def bookdetails_page_view(request,id):
#     url_books_home_page = reverse("books_home_page")
#     url_books_info= reverse("books_info_page")
#     display_page = f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#     <title>Our BookStore</title>
#     </head>
#     <body>
#     <h1>About The Book {id}</h1>
#     <p>Name: {books[id-1]["name"]}</p>
#     <p>Price in Euros: {books[id-1]["price_in_euros"]}</p>
#     <p><a href = "{url_books_home_page}">Book Store</a></p>
#     <p><a href = "{url_books_info}">Books Genres</a></p>
#     </body>
#     </html>
#     """
#     return HttpResponse(display_page)