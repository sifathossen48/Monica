from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.contrib import messages
from website.forms import NewsletterForm
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
        articles =  Article.objects.order_by('-timestamp')
        paginator = Paginator(articles, 9)
        page_number = self.request.GET.get('page')
        context = super().get_context_data(**kwargs)
        context['websetting'] = WebsiteSetting.objects.last()
        context['articles'] = paginator.get_page(page_number)
        return context
    

class BlogDetailView(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        next_blog = article.next_blog()
        prev_blog = article.prev_blog()
        similar_articles = Article.objects.filter(
        category=article.category
        ).exclude(id=article.id)[:3]
        context = {
            'article': article,
            'next_blog': next_blog,
            'prev_blog': prev_blog,
            'similar_articles': similar_articles,
            'websetting': WebsiteSetting.objects.last()
        }
        return render(request, 'blog_details.html', context=context)

def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully subscribed!")
        else:
            messages.error(request, "Invalid email or already subscribed.")
    return redirect(request.META.get('HTTP_REFERER', '/'))