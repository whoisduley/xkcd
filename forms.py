from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
    lowerRange = SelectField('lowerRange', choices=[('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])
    upperRange = SelectField('upperRange', choices=[('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])

    passlength = IntegerField('passlength')

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

   	submit = SubmitField('submit')