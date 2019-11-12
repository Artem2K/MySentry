from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import ErrorModel
from .forms import ErrorListForm


class ErrorListView(ListView):
    model = ErrorModel
    template_name = 'error_list.html'
    form_class = ErrorListForm

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        # search_type = request.POST.get('type_search')
        # all_errors = ErrorModel.objects.filter(type=search_type)
        json = request.POST.get(request)
        print(json)
        return self.render_page(request)

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        all_errors = ErrorModel.objects.all()

        return self.render_page(request, all_errors)

    def render_page(self, request: HttpRequest, all_errors) -> HttpResponse:
        set_of_errors = set()
        for error in all_errors:
            set_of_errors.add(error.type)
        return render(request, self.template_name,
                      {'form': self.form_class(), 'set_errors': set_of_errors, 'table_errors': all_errors})


class ErrorDetailView(DetailView):
    model = ErrorModel
    template_name = 'error_detail.html'
