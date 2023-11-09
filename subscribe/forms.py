from django import forms


def validate_comma(value):
    if "," in value:
        raise forms.ValidationError("Invalid last name.")
    return value

class SubscribeForm(forms.Form):
    first_name = forms.CharField(
        max_length=255,
        label="First Name:",
        required=True,
        help_text="Enter your first name. (Only character)",
    )
    last_name = forms.CharField(
        max_length=255,
        label="Last Name:",
        disabled=False,
        validators=[validate_comma],
    )
    email = forms.EmailField(
        max_length=255,
        label="E-mail:",
    )

    def clean_first_name(self):
        data = self.cleaned_data["first_name"]
        if "," in data:
            raise forms.ValidationError("Invalid first name.")
        return data
