from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from Garden.views import TreeResponseView, FruitResponseView, FruitListView


urlpatterns = [
    path('', RedirectView.as_view(url='tree/'),),
    path('admin/', admin.site.urls),
    path('tree/', TreeResponseView.as_view(),),
    path('fruit/', FruitResponseView.as_view(),),
    path('fruits/', FruitListView.as_view(),),

]
