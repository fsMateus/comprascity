from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name", "is_active", "is_staff")
