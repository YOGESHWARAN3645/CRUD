from django.urls import path
from crud_app import views

urlpatterns = [
    path('',views.ShowHttpResponse),
    path('json',views.ShowJsonResponse),
    path('json/<int:id>',views.ShowParticularIdData),
    path('Create/',views.UserFormView),
    path('delete/<int:id>',views.deleteData),
    path('update/<int:id>',views.updateData),

]