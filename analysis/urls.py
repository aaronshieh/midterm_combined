from django.urls import path
from analysis import views

app_name='analysis'

urlpatterns = [
    path('', views.index,),
    path('editwatchlist/', views.editwatchlist),
    # path('companyinfo/', views.companyinfo),
    path('marketwatch/', views.marketwatch),
    path('dataupdate/', views.dataupdate),
    path('dataupdate/fillinstocklist', views.fillinstocklist),
    path('dataupdate/marktw50', views.marktw50),
    path('dataupdate/markmid100', views.markmid100),
    path('dataupdate/select', views.select),
    path('dataupdate/udfin9', views.udfin9),
    path('dataupdate/readmarket', views.readmarket),
    path('dataupdate/readmarket1', views.readmarket1),
    path('dataupdate/writemarket', views.writemarket),
    path('dataupdate/defaultwatchlist', views.defaultwatchlist),
]