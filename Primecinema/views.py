from email.mime import image
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import UploadMovie as Upload
# Create your views here.

def home(request):
    return render(request, "Cinema_app/index.html")
# signup
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)

        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "your Account has been created successfully.")
        
        return redirect('signin')


    return render(request, "Cinema_app/signup.html")
#signin
def signin(request):
    if request.method == 'POST':
        username = request.POST['usern']
        password = request.POST['password']

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name

            return redirect('home')
        else:
            print("no")
            messages.error(request, "Invalid Credintial")
            return redirect('home')





    return render(request, "Cinema_app/signin.html")
#signout
def signout(request):
    logout(request)
    messages.success(request, "logged out successfully!")
    return redirect('home')

#index
def index(request):
    if request.method == 'POST':
        movie=Upload()
        movie.title=request.POST['title']
        movie.main_actors=request.POST['main_actors']
        movie.genre=request.POST['genre']
        movie.Author=request.POST['author']
        movie.image=request.FILES['image']
        movie.save()
        
        movies=Upload.objects.all()
        return render(request, "Cinema_app/index.html", {"obj":movies})
    else:
        print("home")
    mov=Upload.objects.all()
    return render(request, "Cinema_app/index.html",{"mov":mov})
    


