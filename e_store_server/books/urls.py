from django.urls import path
from . import views

app_name="books"

urlpatterns=[
    path("", views.home_page_view, name="home_page"),
    path("about/", views.about_page_view, name="about_page"),
    # path("", views.books_home_page_view, name="books_home_page"),
    # path("info", views.books_info_page_view, name="info_page"),
    # path("info/<int:id>/", views.bookdetails_page_view, name="book_details"),
   
    
]