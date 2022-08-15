from django import forms


class GenericForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

        for fieldName in self.fields:
            field = self.fields[fieldName]
            field.widget.attrs["placeholder"] = field.label
