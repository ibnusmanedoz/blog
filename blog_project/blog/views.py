from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DeleteView, ListView, DetailView, UpdateView, CreateView
from blog.models import Post, Comment
from blog.forms import CommentForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog/about.html'

class ContactView(TemplateView):
    template_name = 'blog/contact.html'

class PostList(ListView):
    model = Post
    template_name='blog/homepage.html'
    context_object_name = 'postlist'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    login_url = '/login/'
    template_name = 'blog/new_post.html'
    form_class = PostForm

class PostUpdate(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    template_name = 'blog/new_post.html'
    form_class = PostForm
    model = Post

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('homepage')
    template_name = 'blog/delete_post.html'

class PostDraft(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Post
    template_name = 'blog/post_draft_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')

##############################################################
##############################################################
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
