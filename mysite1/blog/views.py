from django.shortcuts import render

# Create your views here.
from datetime import datetime
from blog.models import BlogPost, BlogPostForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
# def archive(request):
#     posts = BlogPost.objects.all()
#     t = loader.get_template("archive.html")
#     c = {"posts": posts}
#     return HttpResponse(t.render(c))


# def archive(request):
#     post = BlogPost.objects.all()
#     return render(request, template_name='archive.html', context={'posts': post})

archive = lambda req: render(req, 'archive.html', context={'posts': BlogPost.objects.all(), 'form': BlogPostForm()})


def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.now()
            post.save()
    return HttpResponseRedirect('/blog/')
