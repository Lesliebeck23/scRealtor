from django.urls import path
from . import views
from .views import *




urlpatterns = [
    path('', views.home, name="home"),
    path('features/', FeatureView.as_view(), name="features"),
#    path('manager/', views.manager, name="manager"),
    path('manager/', AddListingView.as_view(), name='manager'),
    path('listing/edit/<int:pk>', UpdateListingView.as_view(), name='update_listing'),
    path('listing/<int:pk>/delete', DeleteListingView.as_view(), name='delete_listing'),
    path('contact', views.contact, name="contact"),
    path('home_buying', views.home_buying, name="home_buying"),
    path('home_selling', views.home_selling, name="home_selling"),
    path('testimonials', views.testimonials, name="testimonials"),
    path('add_testimonial', views.add_testimonial, name="add_testimonial"),
    path('testimonials/<int:testimonial_id>/delete', views.delete_testimonial, name="delete_testimonial"),


]