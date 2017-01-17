from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from AutoTest_project.models import Test_web


def index(request):
    return render(request, 'index.html')


def web(request):
    return render(request, 'web.html')


def edit_web(request):
    return render(request, "webDetail.html")


class WebView(ListView):
    template_name = "web.html"
    context_object_name = "test_list"

    def get_queryset(self):
        test_list = Test_web.objects.all()
        # for article in test_list:
        #     article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return test_list

    # def get_context_data(self, **kwargs):
    #     kwargs['category_list'] = Category.objects.all().order_by('name')
    #     return super(IndexView, self).get_context_data(**kwargs)


class WebDetailView(DetailView):

    model = Test_web
    template_name = "webDetail.html"
    context_object_name = "Test_web"
    pk_url_kwarg = 'Test_id'

    def get_object(self, queryset=None):
        obj = super(WebDetailView, self).get_object()
        # obj.body = markdown2.markdown(obj.body, extras=['fenced-code-blocks'], )
        return obj