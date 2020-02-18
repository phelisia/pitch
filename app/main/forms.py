from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required
from flask_wtf import FlaskForm

class PitchForm(FlaskForm):
    """
    Class to create a wtf form for creating a pitch
    """
    content = TextAreaField('INPUT YOUR PITCH')
    submit = SubmitField('SUBMIT')

class CommentForm(FlaskForm):
    """
    Class to create a wtf form for creating a pitch
    """
    opinion = TextAreaField('WRITE A COMMENT')
    submit = SubmitField('SUBMIT')

class CategoryForm(FlaskForm):
    """
    Class to create a wtf form for creating a pitch
    """
    name =  StringField('Category Name', validators=[Required()])
    submit = SubmitField('Create')