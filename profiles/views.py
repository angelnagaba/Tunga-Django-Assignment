from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView, UpdateView, DetailView, TemplateView, View, DeleteView, ListView)
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
# Create your views here.
from django.urls import reverse_lazy
from .forms import ProfileForm,TemperatureForm
from .models import profiles, Temperature




class HomePage(LoginRequiredMixin, TemplateView):

    template_name = 'visitor_list.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        return context

        
'''
Create farmer profile. Used class based view.
'''

class CreateVisitorProfile(LoginRequiredMixin,CreateView):
    template_name = 'register_visitor.html'
    success_url = reverse_lazy('profiles:create_profile')
    form_class = ProfileForm
    success_message = "Visitor profile was created successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(CreateVisitorProfile, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateVisitorProfile, self).get_form_kwargs()
        return kwargs


    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            
            return self.form_valid(form)
        else:
            print(form.errors)
        return self.form_invalid(form)


    def form_valid(self, form):
        profile = form.save(commit=False)
       
        profile.user = self.request.user
        profile.save()
       

        return redirect('profiles:profiles')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))

class VisitorProfileList(ListView):
    model = profiles
    template_name = 'visitor_list.html'
    context_object_name = "profilerecord"

   
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = profiles
    context_object_name = "profilerecord"

    template_name = "view_visitor_details.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)

        context.update({

        })
        return context

class CreateTemperatureView(LoginRequiredMixin, CreateView):
    template_name = 'add_temperature.html'
    success_url = reverse_lazy('profiles:add_temperature')
    form_class = TemperatureForm
    success_message = "Visitor profile was created successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(CreateTemperatureView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateTemperatureView, self).get_form_kwargs()
        return kwargs


    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            
            return self.form_valid(form)
        else:
            print(form.errors)
        return self.form_invalid(form)


    def form_valid(self, form):
        profile = form.save(commit=False)
       
        profile.user = self.request.user
        profile.save()
       

        return redirect('profiles:temperatures_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))



class VisitorTemperatureList(ListView):
    model = Temperature
    template_name = 'temperature_list.html'
    # context_object_name = "temperaturerecord"

    def get_context_data(self, **kwargs):
        context = super(VisitorTemperatureList, self).get_context_data(**kwargs)
        context['temperaturerecord'] = Temperature.objects.order_by('-date')
        return context
        
