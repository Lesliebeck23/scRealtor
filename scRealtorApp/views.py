from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
# This allows us to list a query set into the database. The list brings back all the blog posts the detail brings back a specific one. 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Listing, Testimonial
from .forms import ListingForm, EditForm
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home.html', {})


class FeatureView(ListView):
    #designate what model to use
    model = Listing
    template_name = 'features.html'
    ordering = ['-created_at']


def manager(request):
    return render(request, 'manager.html', {})


class AddListingView(CreateView):
    model = Listing
    form_class = ListingForm
    template_name = 'manager.html'

class UpdateListingView(UpdateView):
    model = Listing
    form_class = EditForm
    template_name = 'update_listing.html'

class DeleteListingView(DeleteView):
    model = Listing
    template_name = 'delete_listing.html'
    success_url = reverse_lazy('features')

def contact(request):
    return render(request, 'contact.html', {})

def home_buying(request):
    return render(request, 'home_buying.html', {})


def home_selling(request):
    return render(request, 'home_selling.html', {})


def testimonials(request):
    context = {
        'all_testimonials': Testimonial.objects.all(),
    }
    return render(request, 'testimonials.html', context)


def add_testimonial(request):
    if request.method == "POST":
        testimonials = Testimonial.objects.create(client_name=request.POST['client_name'], client_testimonial=request.POST['client_testimonial'])
    return redirect('testimonials')


def delete_testimonial(request, testimonial_id):
    if request.method == "POST":
        testimonial_to_delete = Testimonial.objects.get(id=testimonial_id)
        testimonial_to_delete.delete()
    return redirect('testimonials')
