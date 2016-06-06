from django.conf.urls import url
import views
import populate

urlpatterns = [
    url(r'^$', views.site, name='site'),
    url(r'form_view', views.form_view, name='form_view'),
]
