from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# 요청 처리에 필요한 함수 정의




# 게시글 목록
def index(request):
    articles = Article.objects.all().order_by('-pk')  # pk 가 큰 글(= 최신 글) 을 위로 올려준다.
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)




# 게시글 작성 화면 및 DB 저장
def create(request):
    if request.method == 'POST':  # POST 요청이라면
        # 1. 사용자가 작성한 내용을 DB에 저장 == POST
        # ModelForm 이므로 사용자가 입력한 데이터의 유효성 검사를 수행하고,
        # model instance 의 역할을 해 주면 됨.
        form = ArticleForm(data = request.POST)  # 사용자가 입력한 데이터는 request.POST 에 있으므로 그 데이터를 인자로 넘겨줌.
        if form.is_valid():  # 유효하다면
            form.save()  # 저장.
            return redirect('articles_url:index')  # 이후 목록으로 redirect
    
    else:
        # 2. 게시글 작성 화면 응답 == GET
        # ModelForm 인스턴스 만들어서 템플릿으로 전달
        form = ArticleForm()  # 비어있는 form

    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)




# 게시글 상세 화면
def detail(request, pk):
    # 상세 페이지를 보여줄 때는 게시글의 내용이 필요하다. 그러므로, pk 를 통해 DB 에서 조사한다.
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)




# 게시글 수정 화면 및 DB 저장
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
    # 1. 사용자가 수정한 내용을 DB에 저장 == POST
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles_url:detail', article.pk)

    else:
        # 2. 게시글 수정 화면 응답 == GET
        form = ArticleForm(instance=article)  # instance=article 이거 때문에 create 와 달라진다!
    
    context = {
        'form': form, 
        'article': article, 
    }
    return render(request, 'articles/update.html', context)




# 게시글 삭제 및 DB 삭제
def delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('articles_url:index')
    return redirect('articles_url:detail', pk)