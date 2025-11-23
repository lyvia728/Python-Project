from django import forms
from .models import Identity

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

