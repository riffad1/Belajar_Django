from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'judul' : 'About',
		'subjudul' : 'Tentang Pondok Programmer',
		'banner' : 'about/img/banner_about.png',
	}
	return render(request,'index.html', context)