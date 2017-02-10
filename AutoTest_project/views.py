
from django.views.generic import ListView, DetailView, UpdateView
from AutoTest_project.models import Test_web, browser, Test_user
from .forms import TestWebForm
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse


class WebView(ListView):
    """
    列表页
    """
    template_name = "web.html"
    context_object_name = "test_list"

    def get_queryset(self):
        test_list = Test_web.objects.all()
        return test_list


class WebEditView(UpdateView):
    """
    编辑页面
    """
    form_class = TestWebForm
    model = Test_web
    template_name = "webDetail.html"
    context_object_name = "Test_web"
    template_name_suffix = '_update_form'
    pk_url_kwarg = 'Test_id'

    def get_object(self, queryset=None):
        obj = super(WebEditView, self).get_object()
        # obj.body = markdown2.markdown(obj.body, extras=['fenced-code-blocks'], )
        return obj

    def get_context_data(self, **kwargs):
        kwargs["browser_list"] = browser.objects.all()
        kwargs['form'] = TestWebForm(initial={
            'website': self.get_object().website,
            'test_cases': self.get_object().test_cases,
            'test_user_input': (self.get_object().test_user.id, self.get_object().test_user.user_name),
            'email': self.get_object().email,
            'browser_input': (self.get_object().browser.id, self.get_object().browser.browser)
        })
        return super(WebEditView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST)

        if form.is_valid():
            self.object.website = request.POST['website']
            self.object.test_cases = request.POST['test_cases']

            test_user = Test_user.objects.filter(id=request.POST['test_user_input'])
            self.object.test_user = test_user[0]

            browser_input = browser.objects.filter(id=request.POST['browser_input'])
            self.object.browser = browser_input[0]

            self.object.save()
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("web")


def run_test(request):
    pass
