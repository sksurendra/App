from django.conf.urls import patterns,url
from pools import views

urlpatterns = patterns('',
        url(r'^$',views.index,name='index')
        url(r'^/two.html$',views.two,name='two')
           (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
                       )
