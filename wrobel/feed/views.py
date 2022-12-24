from django.shortcuts import render
from .models import tweet

# Create your views here.


def home(request):
	context ={'tweets' : tweet.objects.all}
	return render(request, 'feed/home.html',context)
