from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddForm, EditForm
from .models import Order
import datetime


menu = [1, 2, 3]

BASE_CONREXT = {'menu': menu}

def index(request):
    order_by = request.GET.get('order_by', 'id')
    list_orders = Order.objects.all().order_by(order_by)
    context = {
        'list_orders': list_orders,
        'title': 'Наші замовлення'
               }
    context.update(BASE_CONREXT)
    return render(request, 'order/index.html', context)

def create_order(request):
    plated_end_at = datetime.datetime.today() + datetime.timedelta(days = 7)
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                print("order try")
                if not Order.create(plated_end_at=plated_end_at, **form.cleaned_data):
                    form.add_error(None, f"Шановний_а {form.cleaned_data['user']} На жаль в бібліотеці залишилася тільки одна книжка. І вона конче потрібна бібліотекарю. Спробуйте вибрати іншу книгу")
                else:
                    return redirect('orders')
            except:
                form.add_error(None, 'При додавані замовлення виникла помилка')
    else:
        form = AddForm()
    context = {
        'title': "Створюємо нове замовлення",
        'form': form
    }
    context.update(BASE_CONREXT)
    return render(request, 'order/addorder.html', context)

def get_order(request, order_id):
    info = Order.get_by_id(order_id)
    context = {
        'title': f"Замовлення {info.id} ",
        'info': info
    }
    context.update(BASE_CONREXT)
    return render(request, 'order/user.html', context)

def update_order(request, order_id):
    order = Order.get_by_id(order_id)
    order_dict = Order.to_dict(order)
    if order_dict['end_at'] is None:
        # order_dict['end_at'] = datetime.datetime.today()
        order_dict['end_at'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    form = EditForm(order_dict)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                order.update(**form.cleaned_data)
                return redirect('orders')
            except:
                form.add_error(None, 'При редагувані замовлення виникла помилка')

    context = {
        'order_id': order_id,
        'title': "Редагуємо замовлення",
        'form': form
    }
    context.update(BASE_CONREXT)
    return render(request, 'order/update_order.html', context)

def delete_order(request, order_id):
    if Order.delete_by_id(order_id):
        return redirect('orders')
    return HttpResponse('Памілка!!! Ти намагаєшся видалити не завершене замовлення. Спочатку зазнач дату повернення а потім вже видаляй')

def search_orders(request):
    answer = request.GET['answer']
    list_orders = list(Order.objects.filter(Q(book__name__contains=answer) |
                                            Q(book__description__contains=answer)|
                                            Q(user__first_name__contains=answer)|
                                            Q(user__middle_name__contains=answer)|
                                            Q(user__last_name__contains=answer)))
    context = {
        'list_orders': list_orders,
        'title': 'Наші Книжки'
    }
    context.update(BASE_CONREXT)
    return render(request, 'order/index.html', context)