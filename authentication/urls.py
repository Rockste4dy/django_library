from django.urls import path
from authentication import views as w_users

urlpatterns = [
    path('', w_users.index, name='users'),
    path('create/', w_users.create_user, name='create_user'),
    path('<int:user_id>', w_users.get_user, name='user'),
    path('update/<int:user_id>/', w_users.update_user, name='update'),
    path('delete/<int:user_id>', w_users.delete_user),
]