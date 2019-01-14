from django.shortcuts import render 

def index(request):
	context = {
		'judul' : 'Pondok Programmer',
		'subjudul' : 'Selamat Datang',
		'banner' : 'img/banner_home.png',
	}
	return render(request, 'index.html',context)