from django.conf.urls import url
from django.urls import path, re_path
from rest_framework import  routers
from .views import TwitterViewSet, TwitterView, TwitterViewNoParam

router = routers.DefaultRouter()
router.register('',TwitterViewSet)

# urlpatterns = router.urls

# urlpatterns = [
#     # re_path(r'^articles/(?P<id>\w+)/$',TwitterView)
#     path('articles/',TwitterView.as_view()),
#     path('articles/<int:pk>',TwitterView.as_view()),
# ]
urlpatterns = [
    url(r'^articles/$', TwitterViewNoParam.as_view()),
    url(r'^articles/(?P<pk>\d+)/$', TwitterView.as_view(), name="details-article")
]
