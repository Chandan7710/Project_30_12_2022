from django import forms
from django.core import validators
from first_app import models

''' 
you can also imoport bt using moadles name

from first_app.models import Musician, Album

'''


class user_form(forms.Form):
    
    # <label for="user_name">Full Name</label>
    # <input type="text" name="user_name" value="" placeholder="Enter Your Name" required = "True" style="width:200px;">
    user_name = forms.CharField(required=True, label="Full Name ", widget=forms.TextInput(attrs={'placeholder':'Enter your Full Name', 'style': 'width:200px'}))
    
    # <input type="date" name="" value="">
    user_dob = forms.DateField(label="Date Of Birth ", widget=forms.TextInput(attrs={'type':'date'}))
    
    
    user_email = forms.EmailField(label="User Email ")
    
    
   
# required=True, label="Full Name", initial="Krishna"
# label="User Email"

''' by default it will be User name and User email
    to change that use above html functions '''
    
    
class user_form1(forms.Form):
    boolean_field = forms.BooleanField(required=False)
    char_field = forms.CharField(max_length=15, min_length=5)
    choice_field = forms.ChoiceField(choices=[('', '--SELECT OPTION--'), ('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    choices = (('Apple', 'A'), ('Ball', 'B'), ('Cat', 'C'), ('Dog', 'D'), ('Eagle', 'E'))
    choice_field1 = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)



class user_form2(forms.Form):
    name = forms.CharField(validators = [validators.MaxLengthValidator(10), validators.MinLengthValidator(5)])
    number_field = forms.IntegerField(validators= [validators.MaxValueValidator(10), validators.MinValueValidator(5)])


class user_form3(forms.Form):
    user_email = forms.EmailField()
    user_vmail = forms.EmailField()
    
    def clean(self):
        all_cleaned_data = super().clean()
        user_email = all_cleaned_data['user_email']
        user_vmail = all_cleaned_data['user_vmail']
        
        if user_email != user_vmail:
            raise forms.ValidationError("Fields Not Martch !")
        

'''

forms.ModelForm is a build in django class and it is
inherited to the class that we are created

'''
class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"
        

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = models.Album
        fields = "__all__"