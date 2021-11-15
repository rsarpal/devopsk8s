from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

counter=0

def downloadImage():	
	img=requests.get("https://picsum.photos/1200")
	print (img.content)
	with open("/tmp/kube/static/k8simage.jpg","wb") as f:
		f.write(img.content)

def homePageView(request):
	global counter
	if (counter==0):
	  downloadImage()
	counter =+ 1
	return render(request, 'index.html')