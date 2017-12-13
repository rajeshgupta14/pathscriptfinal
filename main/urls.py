"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
#from django.conf.urls import patterns 
from django.conf import settings
from django.contrib import admin
from myapp import views as myappviews 
from consultantform import views as myviews
from django.views.generic.base import TemplateView



urlpatterns = [
    url(r'^admin/',admin.site.urls),#fwdslash
    url(r'^home/$',myappviews.home,name="home"),
    url(r'^$',myappviews.auth_view,name="auth_view"),#addedslash
    url(r'^login/$',myappviews.auth_view,name="auth_view"),
    url(r'^logout/$',myappviews.getout,name="getout"),
    url(r'^invalid/$',myappviews.invalid_login,name="invalid_login"),
    url(r'^clients/$',myappviews.clients,name="clients"),
    url(r'^ram/(?P<consultantform_id>\d+)$',myviews.ram,name="ram"),
    url(r'^ram1/(?P<consultantform_id>\d+)$',myviews.ram1,name="ram1"),
    url(r'^ram2/(?P<consultantform_id>\d+)$',myviews.ram2,name="ram2"),
    url(r'^ram3/(?P<consultantform_id>\d+)$',myviews.ram3,name="ram3"),
    url(r'^ramm/(?P<checklistform_id>\d+)$',myviews.ramm,name="ramm"),
    url(r'^rammm/(?P<projectform_id>\d+)$',myviews.rammm,name="rammm"),
    url(r'^consultantformss/(?P<a_id>\d+)/$',myviews.consultantformss,name='consultantformss'),
    url(r'^projects/(?P<a_id>\d+)$',myviews.projects,name='projects'),
    url(r'^finalformss/(?P<a_id>\d+)/$',myviews.finalformss,name='finalformss'),
    url(r'^consultantformss/(?P<a_id>\d+)/get/(?P<consultantform_id>\d+)/$',myviews.consultantform,name='consultantform'),
    url(r'^consultantformss/(?P<a_id>\d+)/getbr/(?P<consultantform_id>\d+)/$',myviews.branchform,name='branchform'),
    url(r'^consultantformss/(?P<a_id>\d+)/getsu/(?P<consultantform_id>\d+)/$',myviews.subsidiaryform,name='subsidiaryform'),
    url(r'^consultantformss/(?P<a_id>\d+)/getre/(?P<consultantform_id>\d+)/$',myviews.relatedform,name='relatedform'),
    url(r'^consultantformss/(?P<a_id>\d+)/getpr/(?P<consultantform_id>\d+)/$',myviews.productform,name='productform'),
    url(r'^consultantformss/(?P<a_id>\d+)/gets/(?P<checklistform_id>\d+)/$',myviews.checklistform,name='checklistform'),
    url(r'^consultantformss/(?P<a_id>\d+)/getp/(?P<projectform_id>\d+)/$',myviews.projectform,name='projectform'),
    url(r'^consultantformss/(?P<a_id>\d+)/getf/(?P<serviceform_id>\d+)/$',myviews.serviceforms,name='serviceforms'),
    url(r'^consultantformss/(?P<a_id>\d+)/get/(?P<consultantform_id>\d+)/$',myviews.consultantform,name='consultantform'),
    url(r'^consultantformss/(?P<a_id>\d+)/gett/(?P<form_id>\d+)/$',myviews.finalform,name='finalform'),
    url(r'^consultantformss/(?P<a_id>\d+)/getd/(?P<project_id>\d+)/(?P<dueform_id>\d+)/$',myviews.sam,name='sam'),
    url(r'^consultantformss/(?P<a_id>\d+)/getsc/(?P<project_id>\d+)/(?P<scriptform_id>\d+)/$',myviews.samm,name='samm'),
    url(r'^consultantformss/(?P<a_id>\d+)/getst/(?P<project_id>\d+)/(?P<strategyform_id>\d+)/$',myviews.sammm,name='sammm'),
    url(r'^consultantformss/(?P<a_id>\d+)/getps/(?P<project_id>\d+)/(?P<psform_id>\d+)/$',myviews.dam,name='dam'),
    url(r'^consultantformss/(?P<a_id>\d+)/getdi/(?P<project_id>\d+)/(?P<digiform_id>\d+)/$',myviews.damm,name='damm'),
    url(r'^consultantformss/(?P<a_id>\d+)/getm/(?P<project_id>\d+)/(?P<miomform_id>\d+)/$',myviews.dammm,name='dammm'),
    url(r'^consultantformss/(?P<a_id>\d+)/getpd/(?P<project_id>\d+)/(?P<dueform_id>\d+)/$',myviews.samp,name='samp'),
    url(r'^consultantformss/(?P<a_id>\d+)/getpsc/(?P<project_id>\d+)/(?P<scriptform_id>\d+)/$',myviews.sammp,name='sammp'),
    url(r'^consultantformss/(?P<a_id>\d+)/getpst/(?P<project_id>\d+)/(?P<strategyform_id>\d+)/$',myviews.sammmp,name='sammmp'),
    url(r'^consultantformss/(?P<a_id>\d+)/getpps/(?P<project_id>\d+)/(?P<psform_id>\d+)/$',myviews.damp,name='damp'),
    url(r'^consultantformss/(?P<a_id>\d+)/getpdi/(?P<project_id>\d+)/(?P<digiform_id>\d+)/$',myviews.dammp,name='dammp'),
    url(r'^consultantformss/(?P<a_id>\d+)/getpm/(?P<project_id>\d+)/(?P<miomform_id>\d+)/$',myviews.dammmp,name='dammmp'),
    url(r'^consultantformss/(?P<a_id>\d+)/create/$',myviews.create,name='create'),
    url(r'^consultantformss/(?P<a_id>\d+)/create1/$',myviews.create1,name='create1'),
    url(r'^consultantformss/(?P<a_id>\d+)/create2/$',myviews.create2,name='create2'),
    url(r'^consultantformss/(?P<a_id>\d+)/create3/$',myviews.create3,name='create3'),
    url(r'^consultantformss/(?P<a_id>\d+)/checklist/$',myviews.checklist,name='checklist'),
    url(r'^consultantformss/(?P<a_id>\d+)/getf/(?P<project_id>\d+)/created$',myviews.created,name='created'),
    url(r'^consultantformss/(?P<a_id>\d+)/getf/(?P<project_id>\d+)/createsc$',myviews.createsc,name='createsc'),
    url(r'^consultantformss/(?P<a_id>\d+)/getf/(?P<project_id>\d+)/createst$',myviews.createst,name='createst'),
    url(r'^consultantformss/(?P<a_id>\d+)/getf/(?P<project_id>\d+)/createps$',myviews.createps,name='createps'),
    url(r'^consultantformss/(?P<a_id>\d+)/getf/(?P<project_id>\d+)/createdigi$',myviews.createdigi,name='createdigi'),
    url(r'^consultantformss/(?P<a_id>\d+)/getf/(?P<project_id>\d+)/createmiom$',myviews.createmiom,name='createmiom'),
    url(r'^500/$', TemplateView.as_view(template_name="404.html")),
    url(r'^404/$', TemplateView.as_view(template_name="404.html")),


]


if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
    

#if settings.DEBUG:
    