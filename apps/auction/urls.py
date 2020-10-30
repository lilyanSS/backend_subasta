from django.urls import path


from apps.auction import views

app_name = 'auction'
urlpatterns = [
path("auction/", views.vechicleAuctionView, name="auction"),
path("list/", views.auctionList, name="list")
]
