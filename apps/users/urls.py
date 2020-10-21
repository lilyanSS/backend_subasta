from django.urls import path


from apps.users import views

app_name = 'user'
urlpatterns = [
path('session/', views.LoginView.as_view(), name="create_session")

]

