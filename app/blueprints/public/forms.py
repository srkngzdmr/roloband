from __future__ import annotations
"""Public form'lar."""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional


class ContactForm(FlaskForm):
    full_name = StringField("Adınız Soyadınız",
                            validators=[DataRequired(), Length(max=150)])
    company = StringField("Firma", validators=[Optional(), Length(max=200)])
    email = StringField("E-posta",
                        validators=[DataRequired(), Email(), Length(max=150)])
    phone = StringField("Telefon", validators=[Optional(), Length(max=50)])
    subject = StringField("Konu", validators=[Optional(), Length(max=200)])
    message = TextAreaField("Mesajınız",
                            validators=[DataRequired(), Length(min=10, max=4000)])
    submit = SubmitField("Mesajı Gönder")
