from django import forms


SUBJECT_CHOICES = [
    ('General Question', 'General Question'),
    ('Technical Issue', 'Technical Issue'),
    ('Advertising', 'Advertising'),
    ('Complaint', 'Complaint'),
]


class ContactForm(forms.Form):
    from_email = forms.EmailField(label="YOUR EMAIL", required=True)
    subject = forms.CharField(label="SUBJECT", widget=forms.Select(choices=SUBJECT_CHOICES), required=True)
    message = forms.CharField(label="MESSAGE", widget=forms.Textarea(attrs={'rows': 5, 'cols': 27}), required=True)
