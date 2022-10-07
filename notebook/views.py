from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Category, Record, Profile
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.contrib import messages
from django.db.models import Q
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, RecordCreateForm






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

class CategoriesListView(LoginRequiredMixin, generic.ListView):
   model = Category
   context_object_name = 'user_categories'
   template_name ='notebook/categories.html'

   def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class RecordsListView(LoginRequiredMixin, generic.ListView):
    model = Record
    context_object_name = 'user_records'
    template_name ='notebook/categorie_records.html'

    def get_queryset(self):
        category_id = self.kwargs['pk']
        return Record.objects.filter(user=self.request.user).filter(category_id = category_id)
    

# def user_categories(request):
#     if request.user.is_authenticated:
#         categories = UserCategory.category.name
#         context = {
#             'categories': categories
#         }
#     return render(request, 'notebook/categories.html', context=context)

# class UserRecordListView(LoginRequiredMixin, generic.ListView):
#     model = UserRecord
#     model = UserCategory
#     context_object_name = 'user_categories'
#     context_object_name = 'user_records'
#     template_name ='notebook/categories.html'

    # def get_queryset(self):
    #         return Record.objects.filter(user=self.request.user)

# def register(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']
#         if password == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, f'Vartotojo vardas {username} užimtas!')
#                 return redirect('notebook:register')
#             else:
#                 if User.objects.filter(email=email).exists():
#                     messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
#                     return redirect('notebook:register')
#                 else:
#                     User.objects.create_user(username=username, email=email, password=password)
#         else:
#             messages.error(request, 'Slaptažodžiai nesutampa!')
#             return redirect('notebook:register')
#     return render(request, 'notebook/register.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'], 
                email=form.cleaned_data['email'], 
                password=form.cleaned_data['password'])
            messages.info(request, 'Registracija sėkminga')
            return redirect('notebook:register')
    else:
        form = RegistrationForm()
    return render(request, 'notebook/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'notebook/profile.html')

class RecordCreateView(LoginRequiredMixin, generic.CreateView):
    model = Record
    success_url = reverse_lazy('notebook:categories')
    template_name = 'notebook/user_record_form.html'
    form_class = RecordCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def UserCategoriesCreate(request):
    user = request.user
    print(user.id)
    if request.method == "POST":
        name = request.POST['name']
        
        if Category.objects.filter(name=name).exists():
            messages.error(request, f'Tokia kategoja {name} jau yra!')
            return redirect('notebook:categories-new')
        else:
            Category.objects.create(name=name, user = request.user)
            
            return redirect('notebook:categories')
    return render(request, 'notebook/user_categories_form.html')


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('notebook:categories')
    template_name = 'notebook/user_categories_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        category = self.get_object()
        return self.request.user == category.user

class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Category
    success_url = reverse_lazy('notebook:categories')
    template_name = 'notebook/user_category_delete.html'

    def test_func(self):
        category = self.get_object()
        return self.request.user == category.user

@login_required
def search(request):
    query = request.GET.get('query')
    search_results = Record.objects.filter(Q(name__icontains=query))
    return render(request, 'notebook/search.html', {'records': search_results, 'query': query})
 
class UserRecordDetailView(LoginRequiredMixin, generic.DetailView):
    model = Record
    template_name = 'notebook/user_record.html'