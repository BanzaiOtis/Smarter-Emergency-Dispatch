from django.conf.urls import url, include
from django.contrib import admin
import django_sb_admin.views

urlpatterns = [
    # url(r'^$', django_sb_admin.views.map, name='sb_admin_map'),
    url(r'^$', django_sb_admin.views.main, name='sb_admin_main'),
    url(r'^dashboard/$', django_sb_admin.views.dashboard, name='sb_admin_dashboard'),
    url(r'^charts/$', django_sb_admin.views.charts, name='sb_admin_charts'),
    url(r'^tables/$', django_sb_admin.views.tables, name='sb_admin_tables'),
    url(r'^forms/$', django_sb_admin.views.forms, name='sb_admin_forms'),
    url(r'^bootstrap-elements/$', django_sb_admin.views.bootstrap_elements, name='sb_admin_bootstrap_elements'),
    url(r'^bootstrap-grid/$', django_sb_admin.views.bootstrap_grid, name='sb_admin_bootstrap_grid'),
    url(r'^rtl-dashboard/$', django_sb_admin.views.rtl_dashboard, name='sb_admin_rtl_dashboard'),
    url(r'^blank/$', django_sb_admin.views.blank, name='sb_admin_blank'),
	url(r'^about/$', django_sb_admin.views.about, name='sb_admin_about'),
	url(r'^map/$', django_sb_admin.views.map, name='sb_admin_map'),
	
]