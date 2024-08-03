from django.contrib import admin
from django.urls import path
from Analyser import views

urlpatterns = [
    path('', views.index, name='index'),  # Map the root URL to the index view
    path('analyze/', views.analyze_sentiment, name='analyze_sentiment'),
    path('result/<int:analysis_id>/', views.result, name='result'),
    path('history/', views.history, name='history'),
    path('admin/', admin.site.urls),  # Include admin URL if needed
]

