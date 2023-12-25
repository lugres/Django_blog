from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Not used anymore, kept for demostartive purposes - compare with the next class-based view
def  home(request):
	context = {
		'posts': Post.objects.all()
	}

	return render(request, 'blog/home.html', context)


class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

# This class-based view uses default Django template
# by convention <app>/<model>_<view_type>.html - blog/post_detail.html
class PostDetailView(DetailView):
	model = Post

# This expects post_form.html
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		# setting the post's author
		form.instance.author = self.request.user
		return super().form_valid(form)


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
