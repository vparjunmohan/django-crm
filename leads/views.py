from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def lead_page(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads,
    }
    return render(request, 'lead_list.html', context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead':lead,
    }
    return render(request, 'lead_detail.html', context)
