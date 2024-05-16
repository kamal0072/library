from django.shortcuts import render, redirect
from .models import Book
from .forms import BookModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
#view for reading all the books
def show_book(request):
    shelf = Book.objects.all()
    return render(request, 'book/detail.html', {'shelf' : shelf})

#view for uploading the books
def upload(request):
    if request.method == 'POST':
        fm = BookModelForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request, "your information upload successfully..")
            return HttpResponseRedirect('/book')
    else:
        fm = BookModelForm()
    return render(request, 'book/upload_form.html', {'fm' : fm})

#view for updating the books
def update_book(request, id):
    # book_id = int(id)
    try:
        books_sel = Book.objects.get(id=id)
    except:
        return redirect("/book")
    fm=BookModelForm(request.POST or None, instance=books_sel)
    if fm.is_valid():
        fm.save()
        messages.success(request, "your information updated successfully..")
        return redirect("/book")
    return render(request,'book/update_form.html',{'fm':fm})

def delete_book(request,pk):
    book_id=int(pk)
    try:
        book_sel=Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('/book')
    messages.info(request, "Book deleted")
    book_sel.delete()
    return redirect('/book')

# #view for deleting the books
# def delete_book(request, pk):
#     book = Book.objects.get(id = pk)
#     book.delete()
#     return redirect('/book')
