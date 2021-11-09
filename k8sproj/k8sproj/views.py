from django.shortcuts import render, redirect
from django.http import HttpResponse


def homePageView(request):
	return render(request, 'index.html')