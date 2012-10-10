# top-level views for the project, which don't belong in any specific app
from django.shortcuts import render
from models import NewsPost

def index(request):
	c = {}
	c['some'] = 'SOME!'
	c['news_list'] = ['aaa', 'bbb', 'ccc', 'd', 'e', 'f', 'g', 'h',
		'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'] #NewsPost.objects.all()
	return render(request, 'index.html', c)
