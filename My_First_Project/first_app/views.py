from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms
from django.db.models import Avg

# Create your views here.


def contact(request):
    return HttpResponse("<h1>This is contact page</h1> <a href='/about/'>About</a> | <a href='/layout/'>Layout</a> ")

def about(request):
    return HttpResponse("<h1>This is about page</h1> <a href='/'>Contact</a> | <a href='/layout/'>Layout</a> ")

def layout(request):
    return HttpResponse("<h1>This is layout page</h1> <a href='/'>Contact</a> | <a href='/about/'>About</a> ")

def index(request):
    # SELECT * FROM MUSICIAN ORDER BY first_name
    musician_list = Musician.objects.order_by('first_name')
    dict = {'text_1': "This is a list of musician",
            'musician': musician_list}
    return render(request, 'first_app/index.html', context = dict)

def form(request):
    new_form = forms.user_form()
    dict1 = {'test_form': new_form,
             'heading_1': "This is from user django library"}
    
    if request.method == 'POST':
        new_form = forms.user_form(request.POST)
        
        if new_form.is_valid():
            user_name = new_form.cleaned_data['user_name']
            user_dob = new_form.cleaned_data['user_dob']
            user_email = new_form.cleaned_data['user_email']
            
            dict1.update({'user_name':user_name})
            dict1.update({'user_dob':user_dob})
            dict1.update({'user_email':user_email})
            dict1.update({'form_submited':"Yes"})
    
    return render(request, 'first_app/form.html', context = dict1)

def form1(request):
    new_form = forms.user_form1()
    dict1 = {'test_form': new_form,
             'heading_1': "This is from user django library"}
    
    if request.method == 'POST':
        new_form = forms.user_form1(request.POST)
        
        if new_form.is_valid():
        
            dict1.update({'boolean_field': new_form.cleaned_data['boolean_field']})
            dict1.update({'char_field': new_form.cleaned_data['char_field']})
            dict1.update({'choice_field': new_form.cleaned_data['choice_field']})
            dict1.update({'choice_field1': new_form.cleaned_data['choice_field1']})
            dict1.update({'form_submited': "Yes"})
    
    return render(request, 'first_app/form1.html', context = dict1)


def form2(request):
    new_form = forms.user_form2()
    dict1 = {'test_form': new_form,
             'heading_1': "This is from user django library"}
    
    if request.method == 'POST':
        new_form = forms.user_form2(request.POST)
        dict1.update({'test_form':new_form})
        
        if new_form.is_valid():
        
            # dict1.update({'char_field': new_form.cleaned_data['char_field']})
            dict1.update({'number_field': new_form.cleaned_data['number_field']})
            dict1.update({'form_submited': "Yes"})
    
    return render(request, 'first_app/form2.html', context = dict1)


def form3(request):
    new_form = forms.user_form3()
    dict1 = {'test_form': new_form,
             'heading_1': "This is from user django library"}
    
    if request.method == 'POST':
        new_form = forms.user_form3(request.POST)
        dict1.update({'test_form':new_form})
        
        if new_form.is_valid():
        
            dict1.update({'number_field': 'Fields Match !!'})
            dict1.update({'form_submited': "Yes"})
    
    return render(request, 'first_app/form3.html', context = dict1)


def data_form(request):
    new_form = forms.MusicianForm()
    
    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST)
        
        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
        
    dict2 = {'test_form': new_form,
             'heading_1': 'Add New Musician'}

    return render(request, 'first_app/form4.html', context = dict2)

def tem_inherit(request):
    text_dict = {'sample_text': 'everything is temporary in life',
                 'sample_text1': 'Remember Why You Started',
                 'sample_text2': 'Take Care Of Today',
                 'sample_text3': '10',
                 'sample_text4': 'django',
                 'sample_text5': 'enter you password',
                 'sample_text6': Album.objects.get(pk=1),
                 'sample_text7': Album.objects.get(pk=2),
                 'sample_text8': 'sample text',}
    return render(request, 'first_app/inherit_index.html', context=text_dict)

def tem_inherit_one(request):
    return render(request, 'first_app/inherit_form.html')


def index_new_learn(request):
    mus_new_list = Musician.objects.order_by('first_name')
    
    
    dict4 = {'text_4': "Home Page",
             'musician_list': mus_new_list,
             }
    return render(request, 'first_app/index_new.html', context = dict4)


def album_list(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_all_list = Album.objects.filter(artist=artist_id).order_by('name')
    artist_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))
    
    # pk = primary key
    dict5 = {'text_4': "List of Albums",
             'artist_all_info': artist_info,
             'album_song_list': album_all_list,
             'artist_rating_all': artist_rating,
             }
    return render(request, 'first_app/album_list.html', context = dict5)


def musician_form(request):
    new_mus_form = forms.MusicianForm()
    
    if request.method == 'POST':
        new_mus_form = forms.MusicianForm(request.POST)
        
        if new_mus_form.is_valid():
            new_mus_form.save(commit=True)
            return index_new_learn(request)
        
    dict6 = {'text_4': "Add Musician",
             'musician_form': new_mus_form,
             }
    return render(request, 'first_app/musician_form.html', context = dict6)

def album_form(request):
    new_alb_form = forms.AlbumForm()
    
    if request.method == 'POST':
        new_alb_form = forms.AlbumForm(request.POST)
        
        if new_alb_form.is_valid():
            new_alb_form.save(commit=True)
            return index_new_learn(request)
        
        
    dict7 = {'text_4': "Add Albums",
             'album_form':new_alb_form,
             }
    return render(request, 'first_app/album_form.html', context = dict7)


def edit_artist(request, artist_id):
    artist_new_info = Musician.objects.get(pk=artist_id)
    edit_form_new = forms.MusicianForm(instance=artist_new_info)
    
    if request.method == 'POST':
        edit_form_new = forms.MusicianForm(request.POST, instance=artist_new_info)
        
        if edit_form_new.is_valid():
            edit_form_new.save(commit=True)
            return album_list(request, artist_id)
    
    dict8 = {'edit_artist': edit_form_new}
    return render(request, 'first_app/edit_artist.html', context = dict8)

def edit_album(request, album_id):
    album_new_info = Album.objects.get(pk=album_id)
    edit_form_alb = forms.AlbumForm(instance=album_new_info)
    dict9 = {}
    
    if request.method == 'POST':
        edit_form_alb = forms.AlbumForm(request.POST, instance=album_new_info)
        
        if edit_form_alb.is_valid():
            edit_form_alb.save(commit=True)
            dict9.update({'success_text':'Album Successfully Updated'})

    
    dict9.update({'edit_album': edit_form_alb})
    dict9.update({'the_album_id': album_id})
    return render(request, 'first_app/edit_album.html', context = dict9)

def delete_album(request, album_id):
    new_album = Album.objects.get(pk=album_id).delete()
    dict10 = {'delete_success': 'Album Deleted Successfully'}
    return render(request, 'first_app/delete.html', context = dict10)


def delete_musician(request, artist_id):
    new_musician = Musician.objects.get(pk=artist_id).delete()
    dict11 = {'delete_success': 'Musician Deleted Successfully'}
    return render(request, 'first_app/delete.html', context = dict11)
