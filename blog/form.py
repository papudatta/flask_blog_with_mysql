from wtforms import StringField, validators, TextAreaField
from blog_with_flask.author.form import RegisterForm
from flask_wtf import Form
from blog_with_flask.blog.models import Category
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_wtf.file import FileField, FileAllowed


class SetupForm(RegisterForm):
    name = StringField('Blog name', [
        validators.Required(), validators.Length(max=60)])


def categories():
    return Category.query


class PostForm(Form):
    image = FileField('Image', validators=[
        FileAllowed(['jpg', 'png'], 'Images only!')])
    title = StringField('Title', [
        validators.Required(), validators.Length(max=90)])
    body = TextAreaField('Content', validators=[validators.Required()])
    category = QuerySelectField('Category', query_factory=categories,
                                allow_blank=True)
    new_category = StringField('New Category')

