
from ast import If
import re
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import datetime
from django.urls import is_valid_path
from django.views.generic import TemplateView
from .models import Book , Post ,Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm

# Create your views here.

def displayTime(request):
    now = datetime.datetime.now()
    html = "Time is{}".format(now)
    return HttpResponse(html)

def contactView(request):
    return HttpResponse("Hello,Welcome to my blog")

# class-based view
class MyView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        template_name = "index.html"
        context = {
            'page':template_name
        }
        return context
        # return HttpResponse("template_name")

# book-list
def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html",{"books":books})

# view for all posts (post-list)
def post_list(request):
    object_list= Post.objects.all()
    paginator = Paginator(object_list, 3)                           #3:number of posts you want fetched/displayed
    page = request.GET.get('page')
    try: 
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'index.html',{'page':page,'posts':posts})

# views for single post
def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status='published',publish__year=year, publish__month=month,publish__day=day)
    comments=post.comments.filter(active=True)
    new_comment=None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
    else:
         comment_form= CommentForm()
    return render(request,'post_detail.html',{'post':post,'comments':comments,'new_comment':new_comment,'comment_form':comment_form})

