from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login 
from django.contrib import messages
from .forms import CreateUserForm
# Create your views here.
# def loginView(request):
#     return render(request, "authenticate/login.html")

def registerView(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password1"]
            user= authenticate(username=username, password=password, email=email)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('blog:profile')
    else:
        form=CreateUserForm()
    return render(request,'registration/signup.html',{'form':form})
