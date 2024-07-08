from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, UpdateForm
from .models import Record
import datetime


def home(request):
    records = Record.objects.all()


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in.")
            return redirect('home')
        else:
            messages.success(request, 'There was an Error logging in,  Please Try again!!! ')
            return redirect('home')
    
    else:
        return render(request, 'home.html', {'records' : records } )



def logout_user(request):
    logout(request)
    messages.success(request, "You have Been Logged out!!!")
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully Registered!!')
            return redirect('home')
        
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})

"""
def member_record(request, pk):
    def get_age(birthday):
        age = datetime.date.today()-birthday
        return int((age).days/365.25)
    if request.user.is_authenticated:
        member_record = Record.objects.get(id_no = pk)
        db = member_record.dob
        member_record.age = get_age(db)
        member_record.save()
        return render(request, 'record.html', {'member_record':member_record})
    
    else:
        messages.success(request, 'You must be logged in to view that page!!!')
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id_no = pk)
        delete_it.delete()
        messages.success(request, 'Record deleted Successfully!!!')
        return redirect('home')
    
    else:
        messages.success(request, 'Please Login to Delete!!!')
        return redirect('home')
    
"""
    
def add_record(request):
    def get_age(birthday):
        age = datetime.date.today()-birthday
        return int((age).days/365.25)
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            print (request.POST.get('dob'))
            if form.is_valid():
                dob = form.cleaned_data['dob']
                form.cleaned_data['age'] =  get_age(dob)
                print(form.cleaned_data['age'])
                form.save()
                
                messages.success(request, "Member Added...!")
                return redirect('home')
            else:
                messages.success(request, "Invalid data")
        return render(request,'add_record.html', {'form':form})
    else:
        messages.success(request, 'You must be logged in!!!')
        return render(request,'home.html', {'form':form})
"""
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id_no = pk)
        form = UpdateForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Upadated!")
            return redirect('home')
        return render(request,'update_record.html', {'form':form})
    else:
        messages.success(request, 'You must be logged in!!!')
        return redirect('home')

def index(request): 
    my_dict = {'one':'Hello you did it!'}
    return render(request,'index.html',context=my_dict)
"""


def member_record(request, pk):
    if request.user.is_authenticated:
        member_record = Record.objects.get(id_no = pk)
        def age_calculator(birthdate):
            today = datetime.date.today()
            age = (today - birthdate) // datetime.timedelta(days=365.2425)
            return age
        birthdate = member_record.dob
        calculated_age = age_calculator(birthdate)
        member_record.age = calculated_age
        member_record.save()
        return render(request, 'record.html', {'member_record':member_record})
    
    else:
        messages.success(request, 'You must be logged in to view that page!!!')
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id_no = pk)
        delete_it.delete()
        messages.success(request, 'Record deleted Successfully!!!')
        return redirect('home')
    
    else:
        messages.success(request, 'Please Login to Delete!!!')
        return redirect('home')
'''   
def add_record(request):
    def get_age(birthday):
        age = datetime.date.today()-birthday
        return int((age).days/365.25)
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            print("karuna is in")
            if form.is_valid():
                print("In post")
                dob = form.cleaned_data['dob']
                form.cleaned_data['age'] =  get_age(dob)
                form.save()
                print(form.cleaned_data['age'])
                messages.success(request, "Member Added...!")

                return redirect('update_record',pk=form.cleaned_data['id_no'])
            else:
                messages.success(request,"Invalid form")
        return render(request,'add_record.html', {'form':form})
    else:
        messages.success(request, 'You must be logged in!!!')
        return redirect('home')
'''

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id_no = pk)
        form = UpdateForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Upadated!")
            return redirect('home')
        return render(request,'update_record.html', {'form':form})
    else:
        messages.success(request, 'You must be logged in!!!')
        return redirect('home')


def lavazam(request):
    records = Record.objects.all()
    return render(request, 'lavazam.html', {'records' : records } )

def lavazam_outstanding(request):
    records = Record.objects.all()
    return render(request,'lavazam_Outstanding.html', {'records' : records })