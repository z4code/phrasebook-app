from django.shortcuts import render, redirect
# from django.contrib import messages
from django.views import generic
from .models import Category, Phrase

# Home.
class HomeView(generic.ListView):
    model = Category
    template_name = 'main/home.html'
    context_object_name = 'categories'

def home(request):
    '''Home.'''
    # categories = Category.objects.all()
    # languages = Language.objects.all()
    return render(request, 'main/home.html', {})

def view_category(request, slug):
    '''Category.'''
    category = Category.objects.get(slug=slug)
    phrases = Phrase.objects.filter(category=category)
    # language = Language.objects.get()
    count = phrases.count()
    return render(request, 'main/view-category.html', {'phrases': phrases, 'category': category, 'count': count})


