from django.shortcuts import render 

def index(request):
	context = {
		'judul' : 'Pondok Programmer',
		'subjudul' : 'Selamat Datang',
		'nav' : [
			['/', 'Home'],
			['/blog', 'Blog'],
			['/about', 'About'],
			['/contact', 'Contact']
		]
	}
	return render(request, 'index.html',context)