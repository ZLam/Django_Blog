from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
import markdown
import re

# Create your views here.

def resp_home(req):
    # strDesc = "haha"
    # return HttpResponse(strDesc + " " + "Hello World :)")

    # ret = render(
    #     req,
    #     "Blog/index.html",
    #     {
    #         "title" : "ZLam Blog",
    #         "welcome" : "HelloWorld :)"
    #     }
    # )
    # return ret

    postArr = models.Post.objects.all().order_by("-time_create")
    return render(req, "Blog/index.html", context={"postArr" : postArr})

def resp_post(req, id):
    post = get_object_or_404(models.Post, pk = id)
    md = markdown.Markdown(
        extensions = [
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
            "markdown.extensions.toc",
        ]
    )

    post.content = md.convert(post.content)
    toc = ""
    
    r = re.search(r"<div class=\"toc\">.*<ul>.*<ul>.*</div>", md.toc, re.S)
    if (r != None):
        toc = md.toc

    return render(req, "Blog/post.html", context={"post" : post, "toc" : toc})
    