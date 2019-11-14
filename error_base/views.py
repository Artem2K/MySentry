from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.forms import ModelForm
from django.contrib.auth.tokens import default_token_generator

from random import randint
from datetime import datetime

from .models import ErrorModel, AppModel
from .forms import ErrorListForm


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
        dates_with_error = set()
        for error in all_errors:
            set_of_errors.add(error.type)
            dates_with_error.add(datetime.date(error.date))
        dict_with_count_error_per_day = {}
        for date_with_error in dates_with_error:
            count_errors_in_day = 0
            for error in all_errors:
                if datetime.date(error.date) == date_with_error:
                    count_errors_in_day += 1
            dict_with_count_error_per_day[date_with_error] = count_errors_in_day
        return render(request, self.template_name,
                      {'form': self.form_class(),
                       'set_errors': set_of_errors,
                       'table_errors': all_errors,
                       'dict_with_count_error_per_day': dict_with_count_error_per_day,
                       })


class AppDetailView(DetailView):
    model = AppModel
    template_name = 'app_detail.html'
    form_class = ErrorListForm

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        apps = AppModel.objects.filter(id=pk)
        search_type = request.GET.get('type_search')
        day_search = request.GET.get('day_search')
        all_errors = self.query_for_all_errors(search_type, day_search, pk)
        set_of_errors = set()
        dates_with_error = set()
        for error in all_errors:
            set_of_errors.add(error.type)
            dates_with_error.add(datetime.date(error.date))
        dict_with_count_error_per_day = {}
        for date_with_error in dates_with_error:
            count_errors_in_day = 0
            for error in all_errors:
                if datetime.date(error.date) == date_with_error:
                    count_errors_in_day += 1
            dict_with_count_error_per_day[date_with_error] = count_errors_in_day
        return render(request, self.template_name,
                      {'form': self.form_class(),
                       'set_errors': set_of_errors,
                       'table_errors': all_errors,
                       'apps': apps,
                       'dict_with_count_error_per_day': dict_with_count_error_per_day,
                       })

    def query_for_all_errors(self, search_type_field: str, search_date_field: str, pk: int) -> QuerySet:
        if search_type_field == '' and search_date_field == '':
            all_errors = ErrorModel.objects.filter(app_id=pk)
            return all_errors
        elif search_type_field != '' and search_date_field == '':
            all_errors = ErrorModel.objects.filter(type=search_type_field, app_id=pk)
            return all_errors
        elif search_type_field == '' and search_date_field != '':
            all_errors = ErrorModel.objects.filter(app_id=pk, date__startswith=f'{search_date_field}')
            return all_errors
        return ErrorModel.objects.filter(app_id=pk, type=search_type_field, date__startswith=f'{search_date_field}')

class RecordNewError(CreateView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args, **kwargs):
        print('in view')
        app_id = kwargs['id']
        error_type = request.POST['error_type']
        error_message = request.POST['error_message']
        error_stack_trace = request.POST['error_stack_trace']
        token = request.META['HTTP_TOKEN']
        app = AppModel.objects.filter(id=app_id, token=token).first()
        if app is None:
            return HttpResponse('Error handler content', status=403)
        new_error = ErrorModel()
        new_error.app_id = app
        new_error.type = error_type
        new_error.message = error_message
        new_error.stack_trace = error_stack_trace
        new_error.date = datetime.now()
        new_error.save()
        return HttpResponse({'error_type': error_type,
                             'error_message': error_message,
                             'error_stack_trace': error_stack_trace,
                             })


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




