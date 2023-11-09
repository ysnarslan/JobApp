from django import forms
from django.utils.translation import gettext_lazy as _

from subscribe.models import Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        # exclude = ("first_name", )
        labels = {
            "first_name": _("First Name:"),
            "last_name": _("Last Name:"),
            "email": _("E-mail"),
        }
        help_texts = {
            "first_name": _("Enter your first name. (Only character)")
        }
        error_messages = {
            "first_name": {
                "required": _("You cannot move forward without first name")
            },
        }

# def validate_comma(value):
#     if "," in value:
#         raise forms.ValidationError("Invalid last name.")
#     return value
#
# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=255,
#         label="First Name:",
#         required=True,
#         help_text="Enter your first name. (Only character)",
#     )
#     last_name = forms.CharField(
#         max_length=255,
#         label="Last Name:",
#         disabled=False,
#         validators=[validate_comma],
#     )
#     email = forms.EmailField(
#         max_length=255,
#         label="E-mail:",
#     )
#
#     def clean_first_name(self):
#         data = self.cleaned_data["first_name"]
#         if "," in data:
#             raise forms.ValidationError("Invalid first name.")
#         return data
