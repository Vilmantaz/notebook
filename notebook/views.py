from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Category, Record, UserRecord, UserCategory
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.contrib import messages
from django.views import generic
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required





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

class UserCategoriesListView(LoginRequiredMixin, generic.ListView):
   model = UserCategory
   context_object_name = 'user_categories'
   template_name ='notebook/categories.html'

   def get_queryset(self):
        return UserCategory.objects.filter(user=self.request.user)

class UserRecordListView(LoginRequiredMixin, generic.ListView):
    model = Record
    context_object_name = 'user_records'
    template_name ='notebook/categories.html'

    def get_queryset(self):
            return UserRecord.objects.filter(user=self.request.user)

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

# class UserCategoriesCreateView(LoginRequiredMixin, generic.CreateView):
#     model = UserCategory
#     success_url = reverse_lazy('notebook:categories')
#     template_name = 'notebook/user_categories_form.html'
#     form_class = UserCategoryCreateForm

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
@login_required
def UserCategoriesCreate(request):
    if request.method == "POST":
        # user_categories = UserCategory.category.get()
        name = request.POST['category']
        if Category.objects.filter(name=name).exists():
            messages.error(request, f'Tokia kategoja {name} jau yra!')
            return redirect('notebook:categories-new')
        else:
            Category.objects.create(name=name)
            # user_categories.add(new_category)
            return redirect('notebook:categories')
    return render(request, 'notebook/user_categories_form.html')