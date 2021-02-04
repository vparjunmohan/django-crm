from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
# Create your views here.

# class based view


class LandingPageView(TemplateView):
    template_name = 'landing.html'

# equivalent function based view
# def landing_page(request):
#     return render(request, 'landing.html')

# class based view


class LeadListView(ListView):
    template_name = 'lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'

# equivalent function based view
# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         'leads': leads,
#     }
#     return render(request, 'lead_list.html', context)

# class based view


class LeadDetailView(DetailView):
    template_name = 'lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'

# equivalent function based view
# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         'lead':lead,
#     }
#     return render(request, 'lead_detail.html', context)

# class based view


class LeadCreateView(CreateView):
    template_name = 'lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self) -> str:
        return reverse('lead-list')

# equivalent function based view
# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('lead-list')
#     context = {'form': form}
#     return render(request, 'lead_create.html', context)

# class based view


class LeadUpdateView(UpdateView):
    template_name = 'lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse('lead-list')

# equivalent function based view
# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect('lead-list')
#     context = {
#         'form': form,
#         'lead': lead,
#     }
#     return render(request, 'lead_update.html', context)

# class based view


class LeadDeleteView(DeleteView):
    template_name = 'lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse('lead-list')

# equivalent function based view
# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect('lead-list')


# Using Django forms

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.agent = agent
#             lead.save()
#             return redirect('leads')
#     context = {
#         'form': form,
#         'lead': lead,
#     }
#     return render(request, 'lead_update.html', context)

# def lead_create(request):
#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(first_name=first_name,
#                                 last_name=last_name, age=age, agent=agent)
#             return redirect('leads')
#     context = {'form': form}
#     return render(request, 'lead_create.html', context)
