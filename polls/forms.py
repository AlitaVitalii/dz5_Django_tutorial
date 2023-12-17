from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from polls.models import Question


class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)

    # subject = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)


# class QuestionCreateForm(forms.Form):
#     question_text = forms.CharField(label="Text: ", max_length=100, required=True)
#     pub_date = forms.DateTimeField(label="Date: ", initial=datetime.now())
#
#     def clean(self):
#         cleaned_data = super().clean()
#         # if cleaned_data["question_text"] == "123":
#         #     raise ValidationError("question_text - - 123")
#         return cleaned_data
#
#     def clean_question_text(self):
#         data = self.cleaned_data["question_text"]
#         if data == "123":
#             raise ValidationError("question_text - - 123")
#         return data

class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("question_text", "pub_date")
        # fields = ("question_text", )

