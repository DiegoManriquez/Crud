from django.urls import path, include
from . import views

urlpatterns= [
    path('', views.CelularList.as_view(), name='celular_list'),
    path('view/<int:pk>', views.CelularView.as_view(), name='celular_view'),
    path('new', views.CelularCreate.as_view(), name='celular_new'),
    path('view/<int:pk>', views.CelularView.as_view(), name='celular_view'),
    path('edit/<int:pk>', views.CelularUpdate.as_view(), name='celular_edit'),
    path('delete/<int:pk>', views.CelularDelete.as_view(), name='celular_delete'),
]
