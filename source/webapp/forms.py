from django import forms
from webapp.models import Announcement, Comment
from django.forms import widgets


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'description', 'category', 'img', 'price']


class ModerateAnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'description', 'category', 'img', 'price', 'status']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comments']
        widgets = {'comments': widgets.Textarea}
