from django.utils import timezone
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    # views.post_list 함수는 이제 DB에서 필요한 데이터를 가져와서
    # post_list.html에게 넘겨줘야 함
    posts = Post.objects.filter(published_date__lte=timezone.now()).\
        order_by('-published_date')
        # 출판일자가 지금보다 이전으로 들어있는 행만 검색
    return render(      # render() 함수를 호출하여 화면을 출력
                request, # 함수에게 사용자가 요청한 정보를 전달
                'blog/post_list.html', # 화면 출력 주체 지정
                {'posts': posts}) # 화면 출력에 사용할 데이터 전달

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()  # 자동 게시 처리
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()  # 자동 게시 처리
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)   # 원글 post 획득
    if request.method == "POST":           # 만일 요청이 'POST'이면:
        form = CommentForm(request.POST)    # 댓글 폼 form을 request.POST로 채워서 생성
        if form.is_valid():                 # 만일 form 정당하면:
            comment = form.save(commit=False)    # 	form을 댓글 comment로 저장
            comment.post = post                  # 	댓글의 원글 post 획득
            comment.save()                       # 	댓글 저장
            return redirect('post_detail', pk=post.pk)   # 게시글 상세 보기 화면으로 리다이렉트하고 종료
    else:     # 아니면:
        form = CommentForm()    # 	빈 폼 form 생성
    # 댓글 작성 화면으로 이동
    return render(request,
                  'blog/add_comment_to_post.html',
                  {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
























