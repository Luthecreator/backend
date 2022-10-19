from django.contrib import admin
from .models import Book, Post , Comment

# Register your models here.
admin.site.register(Book),


# customizing post model display
@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display= ('title','slug','author','publish','status')
    list_filter=('status','created','publish','author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering= ('status','publish')

# customizing comment model display
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display= ('name','email','post','created','active')
    list_filter= ('active','created','updated')
    search_fields= ('name','email','body')


