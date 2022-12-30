from django.urls import path
from django.conf.urls import url
from first_app import views

app_name = "first_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('form1/', views.form1, name='form1'),
    path('form2/', views.form2, name='form2'),
    path('form2/', views.form2, name='form2'),
    path('form3/', views.form3, name='form3'),
    path('data_form/', views.data_form, name='data_form'),
    path('inherit/', views.tem_inherit, name='temp1'),
    path('inherit1/', views.tem_inherit_one, name='temp2'),
    
    path('index_new/', views.index_new_learn, name='index_new_learn'),
    
    path('album_form/', views.album_form, name='album_form'),
    path('musician_form/', views.musician_form, name='musician_form'),
    
    path('album_list/<int:artist_id>/', views.album_list, name='album_list'),
    path('edit_artist/<int:artist_id>/', views.edit_artist, name='edit_artist'),
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),
    
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
    
    path('delete_musician/<int:artist_id>/', views.delete_musician, name='delete_musician'),
    
    
]

# <a href="{% url 'first_app:delete_artist artist_id=artist_new_info.id '%}" onclick="return confirm('Delete Musician !')" class="btn btn-danger btn-sm">Delete</a>
