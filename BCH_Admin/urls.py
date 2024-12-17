from django.urls import path
from . import views

urlpatterns=[
    path('',views.AuthenticationAdmin.admin_login, name='admin-login'),
    path('dashboard/',views.Dashboard.dashboard,name='dashboard'),
    path('logout/',views.AuthenticationAdmin.SignOut,name='LogOut'),
    path('myprofiles/',views.AdminPages.myprofile,name='myprofile'),
    path('Error_404/',views.AdminPages.Error_404,name='error_404'),
    path('blank/',views.AdminPages.blank,name='blank'),
    path('Menu/',views.AdminPages.admin_menu,name='Admin_menu'),
    path('abouts/',views.AdminPages.abouts,name='abouts'),
    path('forgot_password/',views.AdminPages.forgot_password,name='forgot_password'),
    path('table/',views.AdminPages.table,name='table'),
    path('Admin_service/',views.AdminPages.service,name='admin_service'),
    path('offer_services/',views.AdminPages.offer_services,name='offer_services'),
    # type of coffee sections
    path('Coldcoffee/',views.AdminPages.cold_coffee, name='coldcoffee'),
    path('Hotcoffee/',views.AdminPages.hot_coffee, name='hotcoffee'),


    # routing for the update

    path('update_Vision/<int:id>',views.Update.vision_update, name='vision_update'),
    path('update_story/<int:id>',views.Update.story_update, name='story_update'),

    # uploading the coffee type on site
    path('addhotcoffee/',views.Add_Coffee.add_hot_coffee,name='addhotcoffee'),
    path('addcoldcoffee/',views.Add_Coffee.add_cold_coffee,name='addcoldcoffee'),
    path('update/<int:id>',views.offer_update, name='offer-update'),

    # delete Query
    path('delete-hot-product/<int:id>',views.hot_items_delete,name='product-delete'),
    path('delete-cold-product/<int:id>',views.cold_items_delete,name='product-delete'),
    path('del_offer/<int:id>',views.Delete_item.offer,name='offer_del'),
]