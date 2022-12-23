from django.shortcuts import render

# Create your views here.

tweets =[{'name': 'Mati', 'text': 'To jest pierwszy wpis na wroblu'},{'name': 'Jacek', 'text': 'Jestem drugi'}]

def home(request):
	context ={'tweets' : tweets}
	return render(request, 'feed/home.html',context)
