from django.shortcuts import render
from .models import Book
def home(request):
    book =  Book.objects.all() 
    context ={'books':book}
    return render(request=request,template_name='books.html',context = context)
    
def book_detail(request,id):
    book = Book.objects.get(id=id)
    context = {'book':book}
    return render(request, 'book_detail.html',context)