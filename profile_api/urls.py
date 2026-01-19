from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health, name='health'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('skills/top/', views.SkillsTopView.as_view(), name='skills_top'),
    path('work-experiences/', views.WorkExperienceView.as_view(), name='work_experiences'),
    path('search/', views.SearchView.as_view(), name='search'),
]