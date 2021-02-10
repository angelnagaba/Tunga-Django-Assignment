from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views


from profiles.views import (
    HomePage,
    CreateVisitorProfile,
    VisitorProfileList,
    ProfileDetailView,
    CreateTemperatureView,
    VisitorTemperatureList,
)

app_name = 'profiles'

urlpatterns = [
    
    path('home/', HomePage.as_view(), name='home'),
    path('register/', CreateVisitorProfile.as_view(), name='register_visitor'),
    path('login/', CreateVisitorProfile.as_view(), name='login'),
    path('addtemperature/', CreateTemperatureView.as_view(), name='add_temperature'),
    path('temperatures/', VisitorTemperatureList.as_view(), name='temperatures_list'),
    path('profiles/', VisitorProfileList.as_view(), name='profiles'),
    path('<int:pk>/viewprofile/', ProfileDetailView.as_view(),name="view_profile"),

    
    

]