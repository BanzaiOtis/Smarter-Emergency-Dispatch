from django import forms
from .models import Current_emscall, Current_ambulance


# Create your forms here
class CurrentCallForm(forms.ModelForm):
	"""Form to input address of current emergency call"""
	def __init__(self, *args, **kwargs):
        # first call parent's constructor
		super(CurrentCallForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
		self.fields['addr'].required = False

	class Meta:
		model = Current_emscall
		fields = ("addr",)


# USING THIS FORM RETURNS THE FOLLOWING ERROR: Current_ambulance with this Amb id already exists.
# class CurrentAmbulanceForm(forms.ModelForm):
# 	"""Form to input id of ambulance that is now back in service"""
# 	def __init__(self, *args, **kwargs):
#         # first call parent's constructor
# 		super(CurrentAmbulanceForm, self).__init__(*args, **kwargs)
#         # there's a `fields` property now
# 		self.fields['amb_id'].required = False

# 	class Meta:
# 		model = Current_ambulance
# 		fields = ("amb_id",)


# USING THIS FORM RETURNS THE FOLLOWING ERROR: Current_ambulance matching query does not exist.
class CurrentAmbulanceForm(forms.Form):
	"""Form to input id of ambulance that is now back in service"""
	def __init__(self, *args, **kwargs):
        # first call parent's constructor
		super(CurrentAmbulanceForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
		self.fields['amb_id'].required = False

	amb_id = forms.IntegerField(label="Ambulance ID")