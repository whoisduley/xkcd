from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SelectField, SubmitField, validators
from wtforms.validators import DataRequired

class GeneratorForm(Form):
	lowerRange = SelectField('lowerRange', choices=[('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])
	upperRange = SelectField('upperRange', choices=[('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])

	passLength = StringField('passLength', [validators.Length(min=25, max=50)], default='25')

	alternating = BooleanField('alternating')
	double = BooleanField('double')

	zero = BooleanField('zero')
	one = BooleanField('one')
	two = BooleanField('two')
	three = BooleanField('three')
	four = BooleanField('four')
	five = BooleanField('five')
	six = BooleanField('six')
	seven = BooleanField('seven')
	eight = BooleanField('eight')
	myNumber = BooleanField('myNumber')

	capitalOne = BooleanField('capitalOne')
	capitalTwo = BooleanField('capitalTwo')
	capitalThree = BooleanField('capitalThree')
	capitalFour = BooleanField('capitalFour')