from django import forms
from .models import Identity
from datetime import date


class IdentityVerificationForm(forms.ModelForm):
    confirm_cellphone = forms.CharField(
        label="Confirm Cellphone Number",
        min_length=10,
        max_length=10,
        widget=forms.TextInput(attrs={"placeholder": "Confirm your cellphone number"})
    )

    class Meta:
        model = Identity
        fields = ["id_number", "full_names", "surname", "cellphone"]

    def clean(self):
        cleaned_data = super().clean()
        cellphone = cleaned_data.get("cellphone")
        confirm_cellphone = cleaned_data.get("confirm_cellphone")

        if cellphone and confirm_cellphone and cellphone != confirm_cellphone:
            self.add_error("confirm_cellphone", "Cellphone numbers do not match.")

        # Check age requirement
        if dob:
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 18:
                self.add_error("dob", "You must be at least 18 years old to register to vote.")

        return cleaned_data