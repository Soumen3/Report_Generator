from django.urls import path
from . import views

urlpatterns = [
	path('', views.upload_file, name='upload_file'),
	path('summary-report/<int:pk>', views.summary_report, name='summary_report')
]