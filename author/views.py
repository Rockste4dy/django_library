from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddForm
from .models import Author


menu = [1, 2, 3]

BASE_CONREXT = {'menu': menu}

def index(request):
    list_authors = list(Author.get_all())
    print(list_authors[1])
    context = {
        'list_authors': list_authors,
        'title': 'Наші Автори'
               }
    context.update(BASE_CONREXT)
    return render(request, 'author/index.html', context)
#
def get_author(request, author_id):
    info = Author.get_by_id(author_id)
    books = info.books.all()
    context = {
        'title': f"{info.name} {info.surname} {info.patronymic}",
        'info': info,
        'books': books
    }
    context.update(BASE_CONREXT)
    return render(request, 'author/user.html', context)
#
def update_author(request, author_id):
    author = Author.get_by_id(author_id)
    author_dict = Author.to_dict(author)
    form = AddForm(author_dict)
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                author.update(**form.cleaned_data)
                return redirect('authors')
            except:
                form.add_error(None, 'При редагувані автора виникла помилка')

    context = {
        'author_id': author_id,
        'title': "Редагуємо автора",
        'form': form
    }
    context.update(BASE_CONREXT)
    return render(request, 'author/update.html', context)
#
def create_author(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                Author.objects.create(**form.cleaned_data)
                return redirect('authors')
            except:
                form.add_error(None, 'При додавані користувача виникла помилка')

    else:
        form = AddForm()
    context = {
        'title': "Створюємо нового користувача",
        'form': form
    }
    context.update(BASE_CONREXT)
    return render(request, 'author/addauthor.html', context)
#
def delete_author(request, author_id):
    if Author.delete_by_id(author_id):
        return redirect('authors')
    return HttpResponse('Памілка!!!')