from django.shortcuts import render
from django.views.generic import ListView
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


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
