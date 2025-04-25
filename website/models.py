from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class WebsiteSetting(models.Model):
    site_name = models.CharField(max_length=25)
    owner_image = models.ImageField('owner/')
    owner_about = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='logo/')
    favicon = models.ImageField(upload_to='favicon/')
    home_title = models.CharField(max_length=150)
    scroll_button = models.CharField(max_length=20)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    dribble = models.CharField(max_length=50)
    about_pre_title = models.CharField(max_length=15)
    about_title = models.CharField(max_length=30)
    about_background_image = models.ImageField('about/')
    about_desc = models.TextField(null=True, blank=True)
    expertise_pre_title = models.CharField(max_length=15)
    expertise_title = models.CharField(max_length=30)
    expertise_desc = models.TextField(max_length=300)
    expertise_button_text = models.CharField(max_length=20)
    clients_pre_title = models.CharField(max_length=15)
    clients_title = models.CharField(max_length=100)
    clients_desc = models.TextField(null=True, blank=True)
    testimonials_pre_title = models.CharField(max_length=20)
    testimonials_title = models.CharField(max_length=30)
    cta_title = models.CharField(max_length=50)
    cta_desc = models.TextField(max_length=200)
    cta_button = models.CharField(max_length=20)
    article_pre_title = models.CharField(max_length=15)
    article_title = models.CharField(max_length=30)
    about_page_content_title = models.CharField(max_length=80)
    about_page_content_desc = models.TextField()
    about_page_main_content_title = models.CharField(max_length=50)
    about_page_main_content_desc = models.TextField()
    about_page_value_title = models.CharField(max_length=50)
    about_page_together_work_title = models.CharField(max_length=50)
    about_page_together_work_desc = RichTextField()
    more_abouts_owner_title = models.CharField(max_length=80)
    more_abouts_owner_desc = models.TextField()
    services_page_pre_title = models.CharField(max_length=20)
    services_page_title = models.CharField(max_length=30)
    services_page_display_title = models.CharField(max_length=50)
    services_page_display_desc = models.TextField()
    blog_page_pre_title = models.CharField(max_length=20)
    blog_page_title = models.CharField(max_length=50)
    contact_page_pre_title = models.CharField(max_length=20)
    contact_page_title = models.CharField(max_length=30)
    contact_page_content_title = models.CharField(max_length=80)
    contact_page_desc = models.TextField()
    contact_page_image = models.ImageField(upload_to='contact/')
    newsLetter_title = models.CharField(max_length=20)
    newsLetter_desc = models.TextField(max_length=100)
    email = models.EmailField(max_length=30)
    alt_email = models.EmailField(max_length=30, null=True, blank=True)
    email_button_text = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)
    alt_phone = models.CharField(max_length=15, null=True, blank=True)
    designs_year = models.CharField(max_length=5)
    designer_name = models.CharField(max_length=30)
    designer_profile = models.CharField(max_length=60)

    @property
    def short_cta_desc(self):
        return self.cta_desc[:200]

    def __str__(self):
        return self.site_name

class Expertise(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=300, null=True, blank=True)
    def __str__(self):
        return self.title

class Clients(models.Model):
    link = models.CharField(max_length=70)
    image = models.ImageField(upload_to='clients/')
    def __str__(self):
        return self.link

class Testimonial(models.Model):
    author_name = models.CharField(max_length=30)
    author_title = models.CharField(max_length=30)
    author_image = models.ImageField(upload_to='testimonial/')
    quote = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.author_name

class ArticleCategory(models.Model):
    category = models.CharField(max_length=30)
    def __str__(self):
        return self.category

class Article(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='article/')
    image2 = models.ImageField(upload_to='article/')
    desc = RichTextField()
    desc2 = RichTextField(blank=True,null=True)
    desc3 = RichTextField(blank=True,null=True)
    blockquote_title = models.CharField(max_length=20, null=True, blank=True)
    blockquote_desc = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    @property
    def short_desc(self):
        return self.desc[:200]
    def next_blog(self):
        return Article.objects.filter(id__gt=self.id).order_by('id').first()

    def prev_blog(self):
        return Article.objects.filter(id__lt=self.id).order_by('-id').first()

    def __str__(self):
        return self.title

class ValuesItem(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()
    def __str__(self):
        return self.title

class ServiceItem(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    def __str__(self):
        return self.title
    @property
    def get_service(self):
        return self.servicelist_set.all()

class ServiceList(models.Model):
    item = models.ForeignKey(ServiceItem, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email