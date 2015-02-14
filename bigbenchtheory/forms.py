from django import forms

FOODS = (
	('BRC', 'Broccoli'),
	('SPH', 'Spinach'))

class AddFood(forms.Form):
	foods = forms.ChoiceField(choices=FOODS)