from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import Sign_up_form, log_in_form, Add_post_form
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from enroll.models import Post
from django.contrib.auth.models import Group
# Create your views here.
#Home
def home(request):
  posts = Post.objects.all()
  return render(request,'enroll/home.html', {'posts': posts})

#about
def about(request):
  return render(request,'enroll/about.html')

#contact
def contact(request):
  return render(request,'enroll/contact.html')

#signup
def signup(request):
  if request.method == 'POST':
    fm = Sign_up_form(request.POST)
    if fm.is_valid():
      user = fm.save()
      group = Group.objects.get(name="Aurthor")
      user.groups.add(group)
      messages.success(request, 'Conratulations!! Now You are An Aurthor')
  else: 
    fm = Sign_up_form()
  return render(request,'enroll/signup.html', {'form': fm})

#login
def log_in(request):
  if not request.user.is_authenticated:
    if request.method == 'POST':
      fm = log_in_form(request=request, data=request.POST)
      if fm.is_valid():
        uname = fm.cleaned_data['username']
        upass = fm.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        if user is not None:
          login(request, user)
          messages.success(request, 'Login successfully !!')
          nm = request.user.username
          return HttpResponseRedirect('/dashboard/',)
    else:  
      fm = log_in_form()
    return render(request,'enroll/login.html', {'form':fm})
  else:
    return HttpResponseRedirect('/dashboard/')

#logout
def log_out(request):
  logout(request)
  messages.error(request,'Logout Successfully !!')
  return HttpResponseRedirect('/login/')

#dashboard
def dashboard(request):
  if request.user.is_authenticated:
    posts = Post.objects.all()
    name = request.user.get_full_name()
    gps = request.user.groups.all()
    return render(request,'enroll/dashboard.html', {'name':name,'groups': gps ,'uname':request.user.username,'email':request.user.email,'posts':posts})
  else:
    return HttpResponseRedirect('/login/')

#add Post
def add_post(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      fm = Add_post_form(request.POST)
      if fm.is_valid():
        fm.save()
        messages.success(request, 'Post sdded successfull !')
        return HttpResponseRedirect('/dashboard/')
    else:  
      fm = Add_post_form()
    return render(request, 'enroll/addpost.html', {'form':fm})
  else: 
    return HttpResponseRedirect('/login/')
    
#Edit Post
def edit_post(request,id):
  if request.user.is_authenticated:
    pi = Post.objects.get(pk=id)
    if request.method == 'POST':
      fm = Add_post_form(request.POST, instance=pi)
      if fm.is_valid():
        fm.save()
        messages.success(request, 'Post updated successfull !')
        return HttpResponseRedirect('/dashboard/')
    else:  
      fm = Add_post_form(instance=pi)
    return render(request, 'enroll/editpost.html', {'form':fm})
  else: 
    return HttpResponseRedirect('/login/')

#Delete Post
def delete_post(request,id):
  if request.user.is_authenticated:
    pi = Post.objects.get(pk=id)
    pi.delete()
    messages.success(request, 'Post deleted successfull !')
    return HttpResponseRedirect('/dashboard/')
  else: 
    return HttpResponseRedirect('/login/')
  