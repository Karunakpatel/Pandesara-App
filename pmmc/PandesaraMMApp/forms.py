from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

Choice_value =  [(None, 'Select'),('Female', 'સ્ત્રી'), ('Male', 'પુરુષ'), ('Others', 'અન્ય')]  
Fees_CHOICES = [('Yes','yes'),('No','no'),]
BG_Choices = [(None,'Select'),('O+','O+'),('O-','O-'),('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-')]

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

"""
class AddRecordForm(forms.ModelForm):
    id_no = forms.CharField(required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"સભ્ય આઈડી","class": "form-control"}),label="સભ્ય આઈડી")
    name = forms.CharField(required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"નામ","class": "form-control"}),label="નામ")
    gender =forms.ChoiceField(choices=Choice_value, label="લિંગ")
    dob = forms.DateField(required=True, 
        widget=forms.widgets.DateInput(attrs={"placeholder":"જન્મ તારીખ","class": "form-control", "type": "date"}),label="જન્મ તારીખ")
    age = forms.IntegerField(required=False, disabled=True,
        widget=forms.widgets.TextInput(attrs={"placeholder":"ઉંમર","class": "form-control"}),label="ઉંમર")
    firm = forms.CharField(required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"બિઝનેસ સંસ્થા","class": "form-control"}),label="બિઝનેસ સંસ્થા")
    blood_group = forms.CharField(required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"બ્લડ ગ્રુપ","class": "form-control"}),label="બ્લડ ગ્રુપ")
    contact_no = forms.CharField(required=True, max_length=10,
        widget=forms.widgets.TextInput(attrs={"placeholder":"સંપર્ક નં","class": "form-control"}),label="સંપર્ક નં")
    education = forms.CharField(required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"શિક્ષણ","class": "form-control"}),label="શિક્ષણ")
    address = forms.CharField(required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"સરનામું","class": "form-control"}),label="સરનામું")
    fees = forms.CharField(label='લવાજમ', widget=forms.RadioSelect(choices=Fees_CHOICES))

    class Meta:
        model = Record
        exclude = ("user","age") 

class UpdateForm(forms.ModelForm):
    id_no = forms.CharField(required=True, disabled= True,
        widget=forms.widgets.TextInput(attrs={"placeholder":"સભ્ય આઈડી","class": "form-control"}),label="સભ્ય આઈડી")
    name = forms.CharField(required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"નામ","class": "form-control"}),label="નામ")
    gender =forms.ChoiceField(choices=Choice_value, label="લિંગ")
    dob = forms.DateField(required=True, 
        widget=forms.widgets.DateInput(attrs={"placeholder":"જન્મ તારીખ","class": "form-control", "type": "date"}),label="જન્મ તારીખ")
    age = forms.IntegerField(required=False, disabled=True,
        widget=forms.widgets.TextInput(attrs={"placeholder":"ઉંમર","class": "form-control"}),label="ઉંમર")
    firm = forms.CharField(required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"બિઝનેસ સંસ્થા","class": "form-control"}),label="બિઝનેસ સંસ્થા")
    blood_group = forms.CharField(required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"બ્લડ ગ્રુપ","class": "form-control"}),label="બ્લડ ગ્રુપ")
    contact_no = forms.CharField(required=True, max_length=10,
        widget=forms.widgets.TextInput(attrs={"placeholder":"સંપર્ક નં","class": "form-control"}),label="સંપર્ક નં")
    education = forms.CharField(required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"શિક્ષણ","class": "form-control"}),label="શિક્ષણ")
    address = forms.CharField(required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"સરનામું","class": "form-control"}),label="સરનામું")
    fees = forms.CharField(label='લવાજમ', widget=forms.RadioSelect(choices=Fees_CHOICES))
    

    class Meta:
        model = Record
        exclude = ("user",) 

    """
    
class AddRecordForm(forms.ModelForm):
   id_no = forms.CharField(required=True,
       widget=forms.widgets.TextInput(attrs={"placeholder":"સભ્ય આઈડી","class": "form-control"}),label="સભ્ય આઈડી")
   parivar_no = forms.CharField(required=True,
       widget=forms.widgets.TextInput(attrs={"placeholder":"પરિવાર નં","class": "form-control"}),label="પરિવાર નં")
   family_id = forms.CharField(
       widget=forms.widgets.TextInput(attrs={"placeholder":"યુવા સંઘ ફેમિલી આઈડી","class": "form-control"}),label="યુવા સંઘ ફેમિલી આઈડી")
   name = forms.CharField(required=True,
       widget=forms.widgets.TextInput(attrs={"placeholder":"નામ","class": "form-control"}),label="નામ")
   gender =forms.ChoiceField(choices=Choice_value, label="લિંગ")
   dob = forms.DateField(required=True,
       widget=forms.widgets.DateInput(attrs={"placeholder":"જન્મ તારીખ","class": "form-control", "type": "date"}),label="જન્મ તારીખ")
   #age = forms.IntegerField(required=False,
       #widget=forms.widgets.TextInput(attrs={"placeholder":"ઉંમર","class": "form-control"}),label="ઉંમર")
   firm = forms.CharField(required=True,
       widget=forms.widgets.TextInput(attrs={"placeholder":"બિઝનેસ સંસ્થા","class": "form-control"}),label="બિઝનેસ સંસ્થા")
   blood_group = forms.CharField(required=True,
       widget=forms.widgets.TextInput(attrs={"placeholder":"બ્લડ ગ્રુપ","class": "form-control"}),label="બ્લડ ગ્રુપ")
   contact_no = forms.CharField(required=True, max_length=10,
       widget=forms.widgets.TextInput(attrs={"placeholder":"સંપર્ક નં","class": "form-control"}),label="સંપર્ક નં")
   education = forms.CharField(required=True,
       widget=forms.widgets.TextInput(attrs={"placeholder":"શિક્ષણ","class": "form-control"}),label="શિક્ષણ")
   address = forms.CharField(required=True,
       widget=forms.widgets.TextInput(attrs={"placeholder":"સરનામું","class": "form-control"}),label="સરનામું")
   fees = forms.ChoiceField(choices=Fees_CHOICES, label="લવાજમ")
   designation = forms.CharField(required=True,
       widget=forms.widgets.TextInput(attrs={"placeholder":"હોદ્દો","class": "form-control"}),label="હોદ્દો")
   sabhasad_no = forms.CharField(
       widget=forms.widgets.TextInput(attrs={"placeholder":"સભાસદ નં","class": "form-control"}),label="સભાસદ નં")
   reciept_no = forms.CharField(
       widget=forms.widgets.TextInput(attrs={"placeholder":"રસીદ નં","class": "form-control"}),label="રસીદ નં")
   reciept_date = forms.CharField(
       widget=forms.widgets.TextInput(attrs={"placeholder":"રસીદ તારીખ","class": "form-control"}),label="રસીદ તારીખ")
   kutch_watan = forms.CharField(
       widget=forms.widgets.TextInput(attrs={"placeholder":"કચ્છ વતન","class": "form-control"}),label="કચ્છ વતન")
   
   
   class Meta:
        model = Record
        exclude = ("user",)

class UpdateForm(forms.ModelForm):
    id_no = forms.CharField(required=True,
       widget=forms.widgets.TextInput(attrs={"placeholder":"સભ્ય આઈડી","class": "form-control"}),label="સભ્ય આઈડી")
    parivar_no = forms.CharField(required=True,
       widget=forms.widgets.TextInput(attrs={"placeholder":"પરિવાર નં","class": "form-control"}),label="પરિવાર નં")
    family_id = forms.CharField(
       widget=forms.widgets.TextInput(attrs={"placeholder":"યુવા સંઘ ફેમિલી આઈડી","class": "form-control"}),label="યુવા સંઘ ફેમિલી આઈડી")
    name = forms.CharField(required=True,
       widget=forms.widgets.TextInput(attrs={"placeholder":"નામ","class": "form-control"}),label="નામ")
    gender =forms.ChoiceField(choices=Choice_value, label="લિંગ")
    dob = forms.DateField(required=True,
       widget=forms.widgets.DateInput(attrs={"placeholder":"જન્મ તારીખ","class": "form-control", "type": "date"}),label="જન્મ તારીખ")
    age = forms.IntegerField(required=False,
       widget=forms.widgets.TextInput(attrs={"placeholder":"ઉંમર","class": "form-control"}),label="ઉંમર")
    firm = forms.CharField(required=True,
       widget=forms.widgets.TextInput(attrs={"placeholder":"બિઝનેસ સંસ્થા","class": "form-control"}),label="બિઝનેસ સંસ્થા")
    blood_group = forms.CharField(required=True,
       widget=forms.widgets.TextInput(attrs={"placeholder":"બ્લડ ગ્રુપ","class": "form-control"}),label="બ્લડ ગ્રુપ")
    contact_no = forms.CharField(required=True, max_length=10,
       widget=forms.widgets.TextInput(attrs={"placeholder":"સંપર્ક નં","class": "form-control"}),label="સંપર્ક નં")
    education = forms.CharField(required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder":"શિક્ષણ","class": "form-control"}),label="શિક્ષણ")
    address = forms.CharField(required=True,
       widget=forms.widgets.TextInput(attrs={"placeholder":"સરનામું","class": "form-control"}),label="સરનામું")
    fees = forms.ChoiceField(choices=Fees_CHOICES, label="લવાજમ")
    designation = forms.CharField(required=True,
       widget=forms.widgets.TextInput(attrs={"placeholder":"હોદ્દો","class": "form-control"}),label="હોદ્દો")
    sabhasad_no = forms.CharField(
       widget=forms.widgets.TextInput(attrs={"placeholder":"સભાસદ નં","class": "form-control"}),label="સભાસદ નં")
    reciept_no = forms.CharField(
       widget=forms.widgets.TextInput(attrs={"placeholder":"રસીદ નં","class": "form-control"}),label="રસીદ નં")
    reciept_date = forms.CharField(
       widget=forms.widgets.TextInput(attrs={"placeholder":"રસીદ તારીખ","class": "form-control"}),label="રસીદ તારીખ")
    kutch_watan = forms.CharField(
       widget=forms.widgets.TextInput(attrs={"placeholder":"કચ્છ વતન","class": "form-control"}),label="કચ્છ વતન")
    
    class Meta:
        model = Record
        exclude = ("user",)
