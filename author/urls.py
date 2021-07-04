from django.urls import path
from author import views as w_authors

urlpatterns = [
    path('', w_authors.index, name='authors'),
    path('create/', w_authors.create_author, name='create_author'),
    path('<int:author_id>', w_authors.get_author, name='author'),
    path('update/<int:author_id>/', w_authors.update_author, name='update'),
    path('delete/<int:author_id>', w_authors.delete_author),
]