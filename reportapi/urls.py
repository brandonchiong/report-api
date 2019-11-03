from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('read/<int:report_id>', views.read, name='read'),
    path('update/<int:report_id>', views.update, name='update'),
    path('delete/<int:report_id>', views.delete, name='delete'),
    path('all/', views.all_reports, name='all'),
]
