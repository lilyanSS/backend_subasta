from django.urls import path


from apps.users import views

app_name = 'user'
urlpatterns = [
path('session/', views.LoginView.as_view(), name="create_session"),
path("personal_info/", views.showPersonalInfo, name="showPersonalInfo"),
path("bank_account/", views.showBankAccount, name="showBankAccount"),
path("logout/", views.Logout, name="logout")

]

