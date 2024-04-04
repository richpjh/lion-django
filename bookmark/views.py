from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

class BookmarkLV(ListView):
    Model=Bookmark
    # template_name="bookmark/bookmark_list.html" #appname/model_name_list.html
    # context_object_name = "object_list" # object_list
    
    pass
class BookmarkDV(DetailView):
    model=Bookmark
        # temlate_name="bookmark/bookmark_detail.html" 
 
