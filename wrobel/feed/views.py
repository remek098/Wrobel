from django.shortcuts import render
from .models import tweet
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class TweetListView(LoginRequiredMixin, ListView):
	model = tweet
	template_name = 'feed/home.html'
	ordering = ['-datetime']

class TweetCreateView(LoginRequiredMixin, CreateView):
	model = tweet
	fields = ['text']
	success_url = '/'

	def form_valid(self, form):
		form.instance.uname = self.request.user
		return super().form_valid(form)

class TweetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = tweet
	fields = ['text']
	success_url = '/'

	def test_func(self):
		tweet = self.get_object()
		if(self.request.user == tweet.uname):
			return True
		return False

class TweetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = tweet
	success_url = '/'

	def test_func(self):
		tweet = self.get_object()
		if(self.request.user == tweet.uname):
			return True
		return False