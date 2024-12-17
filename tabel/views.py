from django.shortcuts import get_object_or_404, render

from .models import Employee

def index(request):

    user = get_object_or_404(Employee, tab=request.user.id)

    if user.rang.is_admin:
        children = Employee.objects.filter(depart=user.depart)

    context = {
        'user': user,
        'children': children,
    }

    return render(request, 'tabel/index.html', context)
