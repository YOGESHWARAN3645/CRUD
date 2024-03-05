from django import forms  
from crud_app.models import UserTable  
class UserForm(forms.ModelForm):  
    class Meta:  
        model = UserTable  
        fields = "__all__"  