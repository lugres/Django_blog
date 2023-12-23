from django.shortcuts import render
from .models import Post

# Some dummy post data for testing purpose
posts = [
	{
		'author': 'Angela Lu',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'December 11, 2022'
	},
	{
		'author': 'Jimmy Chin',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'December 15, 2022'
	},
]


def  home(request):
	context = {
		'posts': Post.objects.all()
	}

	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
