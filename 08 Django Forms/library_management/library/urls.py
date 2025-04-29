from django.urls import path
from . import views

urlpatterns = [
    path("contact/", views.contact_view, name="contact"),
    path("contact/success/", views.contact_success_view, name="success"),  # Add this line
    path("add-author/", views.add_author_view, name="add_author"),
    path("author-list/", views.author_list_view, name="author_list"),  # Add this line
    path("add-book/", views.add_book_view, name="add_book"),
    path("book-list/", views.book_list_view, name="book_list"),  # Add this line



    # Publisher URLs
    path("publishers/", views.publisher_list_view, name="publisher_list"),
    path("add-publisher/", views.add_publisher_view, name="add_publisher"),
    path("update-publisher/<int:pk>/", views.update_publisher_view, name="update_publisher"),
    path("delete-publisher/<int:pk>/", views.delete_publisher_view, name="delete_publisher"),
]
