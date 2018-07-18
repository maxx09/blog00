from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Article, Comment, HashTag, Category


def index(request):
    return render(request, "index.html")

def list_page(request):

    category = request.GET.get('category')
    hashtag = request.GET.get('hashtag')

    if not category and not hashtag:
        article_list = Article.objects.all()
    elif category and hashtag:
        article_list = Article.objects.filter(category__category_name=category, hashtag__tag=hashtag)
    elif category:
        article_list = Article.objects.filter(category__category_name=category)
    else:
        article_list = Article.objects.filter(hashtag__tag=hashtag)
    
    hashtag_list = HashTag.objects.all()
    category_list = Category.objects.all()
    context = {
        'article_list' : article_list,
        'hashtag_list' : hashtag_list,
        'category_list' : category_list
    }
    return render(request, "article_list.html", context)



def detail(request, article_id):

    article = Article.objects.get(id=article_id)
    hashtag_list = HashTag.objects.all()
    category_list = Category.objects.all()
    comment_list = Comment.objects.filter(article__id=article_id, is_public=True)
    context = { 
        'article' : article,
        'category_list' : category_list,
        'hashtag_list' : hashtag_list,
        'comment_list' : comment_list
    }
    if request.method == "GET":
        pass    
    elif request.method == "POST":
        username = request.POST.get('username')
        content = request.POST.get('content')
        Comment.objects.create(
            article=article,
            username=username,
            content=content
        )
        return HttpResponseRedirect('/articles/{}/'.format(article_id))
    return render(request, "detail.html", context)
    

def contact(request):
    return render(request, "contact.html")