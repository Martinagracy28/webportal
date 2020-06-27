from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Alumini,Posts
from .forms import PostsForm,AluminiForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def base(request):
    if request.method=="POST":
        return render(request,"register.html")
    else:
        posts = Posts.objects.all()
        return render(request,"base.html",{'posts':posts})


def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1= request.POST['password1']
        password2= request.POST['password2']
        if password1==password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username is already taken")
                return redirect("register")
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email is already taken")
                return redirect("register")    
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
                user.save()
                messages.info(request,"user created")
                return redirect('login')
        else:
            messages.info(request,"Password1 is not match with password2")
            return redirect("register")

    else:
        return render(request,'register.html')

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user=auth.authenticate(username=username,password = password)
        if user is not None:
            auth.login(request,user)
            u = user.id
            alumini = Alumini.objects.filter(user_id = u)
            if alumini:   
                posts = Posts.objects.all()
                return render(request,"base.html",{'posts':posts})
            else:
                messages.info(request,"you still dont have an profile,so create a profile ")
            
                return render(request,"dashboard.html")
        else:
            messages.info(request,"invalid credentials")
            return redirect('register')
    else:
        return render(request,"login.html")    

def logout(request):
    auth.logout(request)
    return redirect("/") 

def posts(request):
    posts = Posts.objects.all()
    return render(request,"base.html",{'posts':posts})   

def profile(request, pk):
    if request.method == "POST":
        return render(request,'dashboard.html')
    else:
        if Alumini.objects.filter(user_id = pk).exists(): 
            alumini = Alumini.objects.get(user_id = pk)
            print(alumini)
            return render(request,'dashboard.html',{'alumini':alumini})
           
        else:
            print("note")
            return render(request,'dashboard.html')

@login_required(login_url='login')        
def newpost(request,pk):
    if Alumini.objects.filter(user_id = pk).exists():
        alumini = Alumini.objects.get(user_id=pk)
        form = PostsForm(initial={'alumini':alumini})
        if request.method == "POST":
            form = PostsForm(request.POST, request.FILES)
            if form.is_valid():
                post_item = form.save(commit = False)
                post_item.save()
                print("saved")
                print(form.cleaned_data)
                messages.info(request,"items are posted")
                return redirect("/")
            else:
                print("not valid")
                return redirect("/")    
        else:
            return render(request,'addpost.html',{'form':form,'alumini':alumini})
    else:
        return render(request,'addpost.html')                 
        
def viewing(request,pk):
    if Alumini.objects.filter(user_id = pk).exists():
        alumini = Alumini.objects.get(user_id = pk)
        aluminipost = alumini.posts_set.all()
        print("no")
        print(aluminipost)
        return render(request,'mypost.html',{'aluminipost':aluminipost,'alumini':alumini})

    else:
        messages.info(request,"still you don't have a profile so create a new profile")
        return render(request,'mypost.html')    



def view(request,pk):
    posts = Posts.objects.get(id=pk)
    return render(request,'view.html',{'posts':posts})

def update(request,pk):

    posts = Posts.objects.get(id=pk)
    form = PostsForm(instance = posts)
    if request.method == "POST":
        form = PostsForm(request.POST,instance=posts)
        if form.is_valid():
            form.save()
            messages.info(request,"updated successfully")
            return redirect('/')
    else:
        return render(request,'update.html',{'form':form})  

def delete(request,pk):
    p = Posts.objects.get(id=pk)
    p.delete()
    messages.info(request,"post deleted")
    return redirect('/')

def edit(request,pk):

    alumini = Alumini.objects.get(id=pk)
    form = AluminiForm(instance = alumini)
    if request.method == "POST":
        form = AluminiForm(request.POST,instance=alumini)
        if form.is_valid():
            form.save()
            messages.info(request,"updated successfully")
            return redirect('/')
    else:

        return render(request,'newprofile.html',{'form':form})  


def newprofile(request,pk):
    user = User.objects.get(id=pk)
    form = AluminiForm(initial={'user':user})
    if request.method == "POST":
        form = AluminiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            print(form.cleaned_data)
            messages.info(request,"new profile is created")
            posts = Posts.objects.all()
            return render(request,"base.html",{'posts':posts})
          
        else:
            print("not valid")
            return redirect("/")    
    else:
        return render(request,'newprofile.html',{'form':form})        

     