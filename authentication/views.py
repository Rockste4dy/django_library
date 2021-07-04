from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddForm
from .models import CustomUser
from book.models import Book


menu = [1, 2, 3]

BASE_CONREXT = {'menu': menu}

# Create your views here.
def index(request):
    list_users = list(CustomUser.get_all())
    # return HttpResponse(list_users)
    context = {
        'list_users': list_users,
        'title': 'Наші користувачі'
               }
    context.update(BASE_CONREXT)
    return render(request, 'authentification/index.html', context)

def get_user(request, user_id):
    info = CustomUser.get_by_id(user_id)
    # books = info.order_set.all().values_list()
    books = []
    books_list = info.order_set.all().values_list()
    for book in books_list:
        books.append(Book.get_by_id(book[2]))
    # books = info.order_set.all().values_list()[0][0]
    # print(books)
    context = {
        'title': f"{info.first_name} {info.middle_name} {info.last_name}",
        'info': info,
        'books': books,
    }
    context.update(BASE_CONREXT)
    return render(request, 'authentification/user.html', context)

def update_user(request, user_id):
    user = CustomUser.get_by_id(user_id)
    user_dict = CustomUser.to_dict(user)
    form = AddForm(user_dict)
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user.update(**form.cleaned_data)
                return redirect('users')
            except:
                form.add_error(None, 'При редагувані користувача виникла помилка')

    context = {
        'user_id': user_id,
        'title': "Редагуємо користувача",
        'form': form
    }
    context.update(BASE_CONREXT)
    return render(request, 'authentification/update.html', context)

def delete_user(request, user_id):
    if CustomUser.delete_by_id(user_id):
        return redirect('users')
    return HttpResponse('Памілка!!!')

def create_user(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                CustomUser.objects.create(**form.cleaned_data)
                return redirect('users')
            except:
                form.add_error(None, 'При додавані користувача виникла помилка')


    else:
        form = AddForm()
    context = {
        'title': "Створюємо нового користувача",
        'form': form
    }
    context.update(BASE_CONREXT)
    return render(request, 'authentification/adduser.html', context)

