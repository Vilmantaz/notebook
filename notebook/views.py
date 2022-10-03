from django.shortcuts import render
from .models import Category, Record
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.contrib import messages
from django.views import generic
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    
    categories = Category.objects.all()

    records = Record.objects.all()  
    records_num = Record.objects.count()

    context = {
        'categories': categories,
        'records': records,
        'records_num': records_num,
    }
    return render(request, 'notebook/index.html', context=context)


# def user_categories(request):
#     if request.user.is_authenticated:
        
#         categories = User.category
#     return render(request, 'notebook/categories.html', {'categories': categories})

class UserCategoriesListView(LoginRequiredMixin, ListView):
   model = Category
   model = Record
   context_object_name = 'categories'
   template_name ='notebook/categories.html'


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('notebook:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('notebook:register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('notebook:register')
    return render(request, 'notebook/register.html')

