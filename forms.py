from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField,IntegerField,DateField,SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from VT.models import User,Truck,Waste,ConGrievance,Search

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class StatusForm(FlaskForm):
	submit1 = SubmitField()
	#submit = SubmitField('Track Now')

class UpdateForm(FlaskForm):
	waste_id=IntegerField('Truck ID',validators=[DataRequired()])
	truck_dry=IntegerField('DRY WASTE',validators=[DataRequired()])
	truck_wet=IntegerField('WET WASTE',validators=[DataRequired()])
	truck_loc=StringField('LOCATION',validators=[DataRequired()])
	submit = SubmitField('Update')

class GrievanceForm(FlaskForm):
	grieve = StringField('Grievance',validators=[DataRequired()])
	submit = SubmitField('Submit')

class AddtruckForm(FlaskForm):
	truck_id=IntegerField('Truck ID',validators=[DataRequired()])
	truck_type=truck_dry=IntegerField('TRUCK TYPE',validators=[DataRequired()])
	submit = SubmitField('Submit')

class SearchForm(FlaskForm):
	truck_id=IntegerField('Truck ID',validators=[DataRequired()])
	date=DateField('Date',validators=[DataRequired()])
	submit2 = SubmitField('Submit')