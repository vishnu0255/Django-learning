from django.shortcuts import render
from first_app import models,forms
#from django.http import HttpResponse
# Create your views here.
word=""
wordscount={}
def home(request):
	#return HttpResponse("hello")
	return render(request,"html/home.html")
def wordcounthome(request):
	#return HttpResponse("hello")
	return render(request,"html/wordcounthome.html")
def wordcount(request):
	#return HttpResponse("hello")
	return render(request,"html/wordcount.html")
def result(request):
	word = request.GET['word']
	count=0
	#return HttpResponse("hello")
	for i in word.split():
		count = count + 1
	return render(request,"html/result.html",{'count':count})
def users(request):
	j=0
	users_details=models.User.objects.all()
	users_details_dict={'user_details_list':users_details,'j':j}
	return render(request,"html/users.html",context=users_details_dict)
def formcreation(request):
	form = forms.formcreate()
	if request.method == "POST":
		form = forms.formcreate(request.POST)
		if form.is_valid():
			print("success")
			print("sno "+str(form.cleaned_data['sno']))												
			print("name "+form.cleaned_data['name'])
			print("testtext "+form.cleaned_data['testtext'])
	return render(request,"html/form.html",{'form':form})
def modelFormcreate(request):
	form = forms.modelFormcreate(request.POST)
	print(form.is_valid())
	if form.is_valid():
		form.save()
	return render(request,"html/formmodel.html",{'form':form})


	
	