from django.views import generic
from spiders_app.forms import URLForm


class URLView(generic.FormView):
    form_class = URLForm
    template_name = 'URLform.html'
    success_url = '/result/'

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        return super(URLView, self).form_valid(form)
