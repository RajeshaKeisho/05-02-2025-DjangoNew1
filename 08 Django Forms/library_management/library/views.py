from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book, Publisher
from .forms import ContactForm, AuthorForm, BookForm, PublisherForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data here (e.g., send an email)
            return redirect("success")
    else:
        form = ContactForm()
    return render(request, "library/contact.html", {"form": form})

def contact_success_view(request):
    return render(request, "library/contact_success.html")

def add_author_view(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("author_list")
    else:
        form = AuthorForm()
    return render(request, "library/add_author.html", {"form": form})


def author_list_view(request):
    authors = Author.objects.all()
    return render(request, "library/author_list.html", {"authors": authors})

def add_book_view(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "library/add_book.html", {"form": form})

# List Publishers View
def book_list_view(request):
    books = Book.objects.all()
    return render(request, "library/book_list.html", {"books": books})


# Add Publisher View
def add_publisher_view(request):
    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("publisher_list")
    else:
        form = PublisherForm()
    return render(request, "library/add_publisher.html", {"form": form})

# List Publishers View
def publisher_list_view(request):
    publishers = Publisher.objects.all()
    return render(request, "library/publisher_list.html", {"publishers": publishers})

# Update Publisher View
def update_publisher_view(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect("publisher_list")
    else:
        form = PublisherForm(instance=publisher)
    return render(request, "library/update_publisher.html", {"form": form, "publisher": publisher})

# Delete Publisher View
def delete_publisher_view(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == "POST":
        publisher.delete()
        return redirect("publisher_list")
    return render(request, "library/delete_publisher.html", {"publisher": publisher})
