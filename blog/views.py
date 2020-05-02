from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostCategory
from users.models import Profile



class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5



class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 5


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")



class PostDetailView(DetailView):
    model = Post



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "image", "category", "summary", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "image", "category", "summary", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            return False


class PostCategoryListView(ListView):
    model = Post
    template_name = "blog/category_posts.html"
    context_object_name = "category_posts"
    paginate_by = 5


    def get_queryset(self):
        category = get_object_or_404(PostCategory, slug=self.kwargs.get("slug"))
        return Post.objects.filter(category_id=category).order_by("-date_posted")



def about(request):
    return render(request, "blog/about.html", {"title": "About"})



def home(request):
    return render(request, "blog/home.html")
