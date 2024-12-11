from django.shortcuts import render

def index(request):

    context = {
        'title': 'Табель',
        'content': 'FDfdsfsdf'
    }
    return render(request, 'tabel/index.html', context)
