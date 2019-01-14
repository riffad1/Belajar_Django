from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'judul' : 'Pondok Programmer',
		'subjudul' : 'Ini adalah blog Pondok Programmer',
		'banner' : 'blog/img/banner_blog.png',
	}
	return render(request, 'index.html', context)