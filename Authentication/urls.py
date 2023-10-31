
from django.urls import path,include
from Authentication import views

urlpatterns = [
   path('register/',views.register,name='register'),
   path('login/',views.login_user,name='login'),
   path('',views.index,name='index'),
   path('lists/',views.lists,name='lists'),
   path('<int:id>/',views.base,name='base'),
   path('base/',views.base,name='base'),
   path('edit/<int:id>/',views.edit,name='edit'),
   path('logout/',views.logout_view,name='logout'),
   path('form/',views.form,name='form'),

   path('delete/<int:id>/',views.delete,name='delete'),
]