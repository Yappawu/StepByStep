from flask_wtf import Form
from wtforms import PasswordField, StringField, BooleanField
from wtforms.validators import Required, ValidationError

from stepbystep.models import UserModel


class LoginForm(Form):
    username = StringField('Username', [Required()])
    password = PasswordField('Password', [Required()])
    remember_me = BooleanField('Remember Me')

    def validate_password(self, field):
        user = UserModel.objects.filter(
            username=self.username.data
        ).first()
        if user is not None and user.verify_password(field.data):
            self.user = user
        else:
            raise ValidationError(u'Username or password is invalid')
