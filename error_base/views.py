from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.forms import ModelForm
from django.contrib.auth.tokens import default_token_generator

from .models import ErrorModel, AppModel
from .forms import ErrorListForm
from random import randint
from datetime import datetime


class ErrorListView(ListView):
    model = ErrorModel
    template_name = 'error_list.html'
    form_class = ErrorListForm

    def get(self, request: HttpRequest) -> HttpResponse:

        search_type = request.GET.get('type_search')
        if search_type != '':
            all_errors = ErrorModel.objects.filter(type=search_type)
        else:
            all_errors = ErrorModel.objects.all()
        set_of_errors = set()
        for error in all_errors:
            set_of_errors.add(error.type)
        return render(request, self.template_name,
                      {'form': self.form_class(), 'set_errors': set_of_errors, 'table_errors': all_errors})


class AppDetailView(DetailView):
    model = AppModel
    template_name = 'app_detail.html'
    form_class = ErrorListForm

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        apps = AppModel.objects.filter(id=pk)
        search_type = request.GET.get('type_search')
        if search_type != '':
            all_errors = ErrorModel.objects.filter(type=search_type, app_id=pk)
        else:
            all_errors = ErrorModel.objects.filter(app_id=pk)
        set_of_errors = set()
        for error in all_errors:
            set_of_errors.add(error.type)
        return render(request, self.template_name,
                      {'form': self.form_class(), 'set_errors': set_of_errors, 'table_errors': all_errors, 'apps': apps})


class RecordNewError(CreateView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args, **kwargs):
        app_id = kwargs['id']
        error_type = request.POST['error_type']
        error_message = request.POST['error_message']
        error_stack_trace = request.POST['error_stack_trace']
        token = request.META['HTTP_TOKEN']
        apps = AppModel.objects.filter(id=app_id)
        print(app_id, error_type, error_message, error_stack_trace, token)
        for app in apps:
            if app.token == token:
                new_error = ErrorModel()
                new_error.app_id = app
                new_error.type = error_type
                new_error.message = error_message
                new_error.stack_trace = error_stack_trace
                new_error.date = datetime.now()
                new_error.save()
        return HttpResponse(request)


class RegisterApp(CreateView):
    model = AppModel
    template_name = 'register_app.html'
    fields = ('name',)
    success_url = reverse_lazy('home')

    def form_valid(self, form: ModelForm) -> ModelForm:
        form.instance.user = self.request.user
        form.instance.token = default_token_generator._make_token_with_timestamp(self.request.user, randint(0, 9999))
        return super().form_valid(form)


class AppsListView(ListView):
    model = AppModel
    template_name = 'apps.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        all_apps = AppModel.objects.filter(user=self.request.user)
        return render(request, self.template_name, {'my_apps': all_apps})




