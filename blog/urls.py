from django.urls import path
from .views import MyView, contactView, displayTime , book_list, post_detail, post_list


app_name = 'blog'


urlpatterns = [
    path("books_list/",book_list,name='book_list'),
    path("",post_list,),
    path("contact/",contactView),
    path("about/",MyView.as_view(),name="home"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name='post_detail')
]

