from django.contrib.auth.models import login_required
from django.shortcuts import render
from item.models import Item
# Create your views here.


@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request , 'dashbourd/index.html', {
        'items':items,
    })