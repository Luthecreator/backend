from unicodedata import name
from django.urls import path
from .views import ContactUs, MyView, aboutPage,book_list,post_detail, post_list , loginView, profileView, logoutView


app_name = 'blog'


urlpatterns = [
    path("books_list/",book_list,name='book_list'),
    path("",post_list,),
    path("contact/",ContactUs,name="contact"),
    path("about/",aboutPage,name="about"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name='post_detail'),
    path("login/",loginView,name="login"),
    path("profile/",profileView, name= 'profile'),
    path("logout/",logoutView, name='logout')
]

