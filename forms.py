from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, email, EqualTo, Length
from flask_login import UserMixin

class CommetForm(FlaskForm):
    full_name = StringField('Tam adınız', validators=[DataRequired(message='Adınızı daxil edin')], render_kw={'placeholder': 'Ad Soyad'})
    content = TextAreaField('Şərhiniz', validators=[DataRequired(message='Şərhinizi qeyd edin')], render_kw={'placeholder': 'Şərh yazın'})

class RegisterForm(UserMixin, FlaskForm):
    name = StringField('Adınız', validators=[DataRequired(message='Adınızı daxil edin'), Length(min=3, max=30)], render_kw={'placeholder': 'Adınız'})
    surname = StringField('Soyadınız', validators=[DataRequired(message='Soyadınızı daxil edin'), Length(min=5, max=30)], render_kw={'placeholder': 'Soyadınız'})
    email = StringField('Email', validators=[DataRequired(message='Emailinizi daxil edin'), email(message='Düzgün email adresi daxil edin')], render_kw={'placeholder': 'example@gmail.com'})
    username = StringField('Istifadəçi adı', validators=[DataRequired(message='Istifadəçi adınızı daxil edin'), Length(min=3, max=30)], render_kw={'placeholder' : 'Istifadəçi adınız'})
    password = PasswordField('Şifrə', validators=[DataRequired(message='Güclü bir şifrə yaradın'), EqualTo('password_confirm', message='Daxil etdiyiniz şifrələr uyğun deyil'), Length(min=8, max=30)])
    password_confirm = PasswordField('Şifrə təsdiq', validators=[Length(min=8, max=30)])

class LoginForm(FlaskForm, UserMixin):
    username = StringField('Istifadəçi adınız', validators=[DataRequired(message='Istifadəçi adınızı daxil edin')], render_kw={'placeholder' : 'Istifadəçi adınız'})
    password = PasswordField('Şifrə', validators=[DataRequired(message='Şifrənizi daxil edin')])
