from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from Aanisite import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index , name="index"),
    path('products/', views.products_view, name="products"),
    path('about-us/', TemplateView.as_view(template_name="Aanisite/about-us.html") , name="about_us"),
    path('contact-us/', TemplateView.as_view(template_name="Aanisite/contact-us.html"), name="contact_us"),
    path('contact-us/handle-form/', views.contact_us_form_handler, name="handle_form"),
    path('contract/', views.contract, name='contract'),
    path('hire/', views.employment_form_render, name="hire"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)