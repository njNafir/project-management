from django import forms
from .models import Project

class SubmitProjectForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['group_number'].widget.attrs.update({'class':'form-control group_number', 'placeholder':'Ex: 1'})
		self.fields['group_name'].widget.attrs.update({'class':'form-control group_name', 'placeholder':'Ex: Black'})
		self.fields['members_name'].widget.attrs.update({'class':'form-control members_name', 'placeholder':'Ex: David, Mile'})
		self.fields['title'].widget.attrs.update({'class':'form-control title', 'placeholder':'Ex: Hostel Management System'})
		self.fields['subtitle'].widget.attrs.update({'class':'form-control subtitle', 'placeholder':'Ex: Management Website'})
		self.fields['description'].widget.attrs.update({'class':'form-control description'})
		self.fields['used_skill'].widget.attrs.update({'class':'form-control used_skill', 'placeholder':'Ex: Python, Django etc'})
		self.fields['thumbnail'].widget.attrs.update({'class':'form-control thumbnail'})
		self.fields['project_proposal'].widget.attrs.update({'class':'form-control project_proposal', 'placeholder':'Ex: Project proposal in PDF format'})
		self.fields['project_file'].widget.attrs.update({'class':'form-control project_file', 'placeholder':'Ex: Project file in ZIP format'})

	class Meta:
		model = Project

		fields = [
			'group_number',
			'group_name',
			'members_name',
			'title',
			'subtitle',
			'description',
			'used_skill',
			'thumbnail',
			'project_proposal',
			'project_file'
		]

# class NormalContactForm(forms.ModelForm):
# 	def __init__(self, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
# 		self.fields['name'].widget.attrs.update({'class':'form-control name', 'placeholder':'Ex: Nj Nafir'})
# 		self.fields['email'].widget.attrs.update({'class':'form-control email', 'placeholder':'Ex: mdanjenafir24434@gmail.com'})
# 		self.fields['message'].widget.attrs.update({'class':'form-control text-light text-capitalize message'})

# 	class Meta:
# 		model = NormalContact

# 		fields = [
# 			'name',
# 			'email',
# 			'message'
# 		]