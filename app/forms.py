from django import forms
from .models import User, CTScan, RenalCellImage

class UserSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data


class CTScanForm(forms.ModelForm):
    class Meta:
        model = CTScan
        fields = ['scan_result']
        widgets = {
            'scan_result': forms.Textarea(attrs={'placeholder': 'Enter CT scan result'}),
        }
        labels = {
            'scan_result': 'CT Scan Result',
        }


class RenalCellImageForm(forms.ModelForm):
    class Meta:
        model = RenalCellImage
        fields = ['image_result']
        widgets = {
            'image_result': forms.Textarea(attrs={'placeholder': 'Enter renal cell image result'}),
        }
        labels = {
            'image_result': 'Renal Cell Image Result',
        }
