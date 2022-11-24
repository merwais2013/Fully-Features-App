from wtforms import StringField, SubmitField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField("Post")
