from django.contrib import admin

from website.models import NewsletterSubscription, WebsiteSetting, Expertise, Clients, Testimonial, ArticleCategory, Article, ValuesItem, \
    ServiceItem, ServiceList

# Register your models here.
admin.site.register(WebsiteSetting)
admin.site.register(Expertise)
admin.site.register(Clients)
admin.site.register(Testimonial)
admin.site.register(ArticleCategory)
admin.site.register(Article)
admin.site.register(ValuesItem)
admin.site.register(ServiceItem)
admin.site.register(ServiceList)
admin.site.register(NewsletterSubscription)
