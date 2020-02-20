from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "your full name", "id": "form_full_name"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "email@example.com", "id": "form_email"}))
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "content details goes here"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email should be gmail.com")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
