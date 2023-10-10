from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from website.models import WebsiteSetting, Expertise, Clients, Testimonial, Article, ValuesItem, ServiceItem


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['websetting'] = WebsiteSetting.objects.last()
        context['expertise'] = Expertise.objects.all()
        context['clients'] = Clients.objects.all()
        context['testimonial'] = Testimonial.objects.all()
        context['articles'] = Article.objects.order_by('-timestamp')
        return context

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['websetting'] = WebsiteSetting.objects.last()
        context['testimonial'] = Testimonial.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['websetting'] = WebsiteSetting.objects.last()
        context['valuesItem'] = ValuesItem.objects.all()
        context['testimonial'] = Testimonial.objects.all()
        return context

class ServiceView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['websetting'] = WebsiteSetting.objects.last()
        context['testimonial'] = Testimonial.objects.all()
        context['servicesItem'] = ServiceItem.objects.all()
        return context

class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['websetting'] = WebsiteSetting.objects.last()
        context['articles'] = Article.objects.order_by('-timestamp')
        return context

class BlogDetailView(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        context = {
            'article': article,
            'websetting': WebsiteSetting.objects.last()
        }
        return render(request, 'blog_details.html', context=context)