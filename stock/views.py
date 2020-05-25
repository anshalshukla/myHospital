from django.shortcuts import render
from django.http import HttpResponseRedirect
from home.context_processors import hasGroup
from .models import stock
from django.contrib import messages

# Create your views here.
def inventory(request):
    c = {}
    user = request.user
    if hasGroup(user, 'inventory_manager'):
        c['stocks'] = stock.objects.all()
    else:
        messages.add_message(request, messages.WARNING, 'Access Denied.')
        return HttpResponseRedirect('/')
    return render(request, 'stock/view_all.html', c)