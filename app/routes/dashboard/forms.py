from wtforms.validators import (
    DataRequired,
    Length,
    Email,
)
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    TextAreaField
)


class SendEmailForm(FlaskForm):
    email = StringField(
        "Email*", validators=[DataRequired(), Length(min=3, max=100), Email()])
    subject = StringField(
        "Subject*", validators=[DataRequired(), Length(min=3, max=30)])
    body = TextAreaField("Body", render_kw={"rows": '9'}, validators=[DataRequired(
        message="Please provide password"), Length(
            min=8, message="Provide at least 8 characters")])
    submit = SubmitField("Send Email")