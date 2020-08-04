from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post


def title(request):
    return render(request, 'blog/heading.html')

def home(request):   # home function
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):    #home list view
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class UserPostListView(ListView):    #home list view
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):    #home list view
    model = Post

#LoginRequiredMixin(for user to login before creating newpost)
class PostCreateView(LoginRequiredMixin, CreateView):    #home list view
    model = Post
    fields = ['title', 'content']

    # for giving author name to be name of user who logged in
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# LoginRequiredMixin- login before creating post
# UserPassesTestMixin-  post can be updated by author only
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):    #home list view
    model = Post
    fields = ['title', 'content']

    # for giving author name to be name of user who logged in
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # post can be updated by author only
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):    #home list view
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html')


