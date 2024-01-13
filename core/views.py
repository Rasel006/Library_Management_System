from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from book.models import Book
from category.models import Category

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            books = Book.objects.filter(category=category)
        
        categories = Category.objects.all()
        context['categories'] = categories
        context['books'] = books
        return context