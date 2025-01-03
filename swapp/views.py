from django.shortcuts import render
from .models import BlogPost, BlogPostPhoto
from collections import defaultdict
import pprint
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    blogposts = BlogPost.objects.order_by("-rank")

    post_list = BlogPost.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 12)
    try:
        blogposts = paginator.page(page)
    except PageNotAnInteger:
        blogposts = paginator.page(1)
    except EmptyPage:
        blogposts = paginator.page(paginator.num_pages)


    context = {
        "blogposts": blogposts,
    }

    return render(request, "index.html", context)


def post(request,slug):
    blogposts = BlogPost.objects.order_by("-id")
    blogpost = BlogPost.objects.get(slug=slug)

    context = {
        "blogposts": blogposts,
        "blogpost": blogpost,

    }

    return render(request, "post.html", context)

class HomePageView(TemplateView):
    template_name = 'index.html'

class SearchResultsView(ListView):
    model = BlogPost
    template_name = 'search_results.html'
    

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query is not None:
            object_list = BlogPost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(date__icontains=query) 
            )

            
        return object_list
    