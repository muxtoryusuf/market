from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, is_superuser=False):
        if is_superuser:
            user = self.model(phone_number=phone_number)
        else:
            user = self.model(phone_number=phone_number)
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if password is not None:
            user.set_password(password)
        user.is_superuser = is_superuser
        user.save()
        return user

    def create_staffuser(self, phone_number, password):
        if not password:
            raise ValueError('staff/admins must have a password.')
        user = self.create_user(phone_number=phone_number, password=password)
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self, phone_number, password):
        if not password:
            raise ValueError('superusers must have a password.')
        user = self.create_user(phone_number=phone_number, password=password, is_superuser=True)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
