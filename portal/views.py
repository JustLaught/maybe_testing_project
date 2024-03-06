from django.shortcuts import render, redirect, HttpResponse
from .models import Article, Comment, Bookmark
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


#* Create your views here.
def index(request):
    sort_field = request.GET.get('sort')
    search_field = request.GET.get('search')
    if search_field == 'null':
        search_field = None
        
    if search_field and sort_field:
        articles_by_name = Article.objects.filter(name__icontains=search_field)[:10]
        article_by_text = Article.objects.filter(content__icontains=search_field)[:10]
        articles = articles_by_name.union(article_by_text).order_by(sort_field)[:10]

    if not search_field and sort_field:
        articles = Article.objects.order_by(sort_field).all()[:10]
        
    if search_field and not sort_field:
        articles_by_name = Article.objects.filter(name__icontains=search_field)[:10]
        article_by_text = Article.objects.filter(content__icontains=search_field)[:10]
        articles = articles_by_name.union(article_by_text)[:10]

    if not search_field and not sort_field:
        articles = Article.objects.all()[:10]
   
    return render(request, 'index.html', {'articles': articles})

def login_user(request):
    if request.method == 'POST':
        # todo: Add hash to paswords 
        name = request.POST['user_name']
        password = request.POST['Password']
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'sightin.html', {'autheticated': False})
    else:
        return render(request, 'sightin.html')

def register(request):
    if request.method == 'POST':
        #// name = request.POST['first_name']
        #// lastname = request.POST['last_name']
        # todo: Add hash to paswords 
        password = request.POST['password']
        password2 = request.POST['repeatPassword']
        if password != password2:
            return render(request, 'register.html', {'invalid_password': True})
        else:
            username = request.POST['user_name']
            email = request.POST['email']
            password = request.POST['password']
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect('index')
    else:
        return render(request, 'register.html')

def article(request, id):
    article = Article.objects.get(id=id)
    article.views += 1
    article.save()
    in_bookmarks = False
    try:
        for marks in request.user.bookmarks.all():
            if article == marks.article:
                in_bookmarks = True
    except AttributeError:
        in_bookmarks = False

    return render(request, 'article.html', {'article': article, 'in_bookmarks': in_bookmarks})

def bookmarks(request):
    if request.user.is_authenticated:
        return render(request, 'bookmarks.html')
    else: return redirect('index')

def add_bookmarks(request, id):
    article = Article.objects.get(id=id)
    for marks in request.user.bookmarks.all():
        if article == marks.article:
            marks.delete()
            return redirect('article', id)
        
    bookmark = Bookmark(article=article, user=request.user)
    bookmark.save()
    
    return redirect('article', id)

def serch(request):
    return render(request, 'base.html')

def comment(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            content = request.POST['content']
            article = Article.objects.get(id=id)
            user = request.user
            comment = Comment(content=content, article=article, user=user)
            comment.save()
            return redirect('index')
        else: return render(request, 'comment.html')
    else: return redirect('article', id)

def change_scheme(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'GET':
            BodyColor = request.GET.get("BodyColor")
            TextColor = request.GET.get("TextColor")
            FontSizeNum = request.GET.get("FontSizeNum")
            if FontSizeNum != '' and BodyColor != '' and TextColor != '':
                with open('newsportal/static/styles/styles.css', 'w+') as f:
                    f.write('body{' + f'background-color: {BodyColor}; color: {TextColor}; font-size: {FontSizeNum}px;' + '}')
            elif BodyColor != '' and TextColor != '': 
                with open('newsportal/static/styles/styles.css', 'w+') as f:
                    f.write('body{' + f'background-color: {BodyColor}; color: {TextColor};' + '}')
                return redirect('index')       
        return render(request, 'change_scheme.html')
    else:
        return redirect('index')

def reset_change_scheme(request):
    if request.user.is_authenticated and request.user.is_superuser:
        with open('newsportal/static/styles/styles.css', 'r+') as f:
            f.read()
        with open('newsportal/static/styles/styles.css', 'w+') as f:
            f.write('')
        return redirect('index')
    return redirect('index')

def ratings(request):
    if request.user.is_authenticated and request.user.is_superuser:  
        sort_filter = request.GET.get('sort')
        if sort_filter:
            articles = Article.objects.order_by(sort_filter).all()
            return render(request, 'article_rating.html', {'articles': articles})
        else:
            articles = Article.objects.all()
            return render(request, 'article_rating.html', {'articles': articles})
    return redirect('index')

def logout_user(request):
    logout(request)
    return redirect('index')