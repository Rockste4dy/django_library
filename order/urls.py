from django.urls import path
from order import views as w_orders

urlpatterns = [
    path('', w_orders.index, name='orders'),
    path('create/', w_orders.create_order, name='create_order'),
    path('<int:order_id>', w_orders.get_order, name='read_order'),
    path('update/<int:order_id>/', w_orders.update_order, name='update_order'),
    path('delete/<int:order_id>', w_orders.delete_order, name='delete_order'),
    path('search/', w_orders.search_orders),
]