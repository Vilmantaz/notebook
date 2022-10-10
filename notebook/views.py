from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Category, Record
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import RecordCreateForm

def index(request):

    return render(request, 'notebook/index.html')



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
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('notebook:register')
    return render(request, 'notebook/register.html')

@login_required
def profile(request):
    return render(request, 'notebook/profile.html')


class RecordsListView(LoginRequiredMixin, generic.ListView):
    model = Record
    context_object_name = 'user_records'
    template_name ='notebook/categorie_records.html'
    paginate_by = 4

    def get_queryset(self):
        category_id = self.kwargs['pk']
        return Record.objects.filter(user=self.request.user).filter(category_id = category_id)

 
class UserRecordDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Record
    template_name = 'notebook/user_record.html'

    def test_func(self):
        record = self.get_object()
        return self.request.user == record.user

class RecordCreateView(LoginRequiredMixin, generic.CreateView):
    model = Record
    template_name = 'notebook/user_record_form.html'
    form_class = RecordCreateForm

    def get_success_url(self):
        return reverse_lazy("notebook:categorie_records", kwargs={"pk": self.object.category_id})

    def get_form_kwargs(self):
        kwargs = super(RecordCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecordUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Record
    fields = ['name', 'content', 'image']
    template_name = 'notebook/user_record_form.html'

    def get_success_url(self):
        return reverse_lazy("notebook:categorie_records", kwargs={"pk": self.object.category_id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        record = self.get_object()
        return self.request.user == record.user


class RecordDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Record
    success_url = reverse_lazy('notebook:categories')
    template_name = 'notebook/category_record_delete.html'

    def test_func(self):
        record = self.get_object()
        return self.request.user == record.user


class CategoriesListView(LoginRequiredMixin, generic.ListView):
   model = Category
   context_object_name = 'user_categories'
   template_name ='notebook/categories.html'
   paginate_by = 4

   def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


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
    context_object_name = 'category_name'
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
    search_results = Record.objects.filter(name__icontains=query).filter(user=request.user)
    return render(request, 'notebook/search.html', {'records': search_results, 'query': query})