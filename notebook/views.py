from django.shortcuts import render
from .models import Category, Record

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
