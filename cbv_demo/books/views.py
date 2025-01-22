
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

# 1. TemplateView
class HomePageView(TemplateView):
    template_name = "books/home.html"

# 2. ListView
class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"

# 3. DetailView
class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"

# 4. CreateView
class BookCreateView(CreateView):
    model = Book
    template_name = "books/book_form.html"
    fields = ['title', 'author', 'description', 'is_published']
    success_url = reverse_lazy('book-list')

# 5. UpdateView
class BookUpdateView(UpdateView):
    model = Book
    template_name = "books/book_form.html"
    fields = ['title', 'author', 'description', 'is_published']
    success_url = reverse_lazy('book-list')

# 6. DeleteView
class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = reverse_lazy('book-list')
