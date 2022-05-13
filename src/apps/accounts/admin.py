from django.contrib import admin
from django import forms
from .models import User, TradePoint, Visit
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = "__all__"

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    # password = ReadOnlyPasswordHashField()
    password = None

    class Meta:
        model = User
        fields = ('password', 'is_staff', 'is_superuser')

    def clean_password(self):
        return self.initial["password"]


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'phone_number', 'created_at', 'updated_at')
    list_filter = ('created_at', )

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'phone_number',)
        }),
        ('Important dates', {'fields': ('last_login', )}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'user_permissions')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'phone_number', 'password')
        }),
    )

    list_display_links = ('phone_number',)
    ordering = ('-id',)


@admin.register(TradePoint)
class TradePointAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'user',
    )


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):

    list_display = (
        'market',
        'latitude',
        'longitude',
    )


