from django.views import generic
from spiders_app.forms import URLForm
import redis


class URLView(generic.FormView):
    form_class = URLForm
    template_name = 'URLform.html'
    success_url = '/'

    def form_valid(self, form):
        data = form.cleaned_data
        con = redis.StrictRedis()
        con.lpush(data.get('spider_name')+':start_urls', data.get('url'))
        return super(URLView, self).form_valid(form)
