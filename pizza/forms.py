from django import forms
from pizza.models import Pizza,Size

# class PizzaForm(forms.Form):
# 	# topping1 = forms.CharField(label='Topping 1',max_length=100)
# 	# topping2 = forms.CharField(label='Topping 2',max_length=100)
# 	size = forms.ChoiceField(label='Size',choices=[('small','small'),('medium','medium'),('large','large')])
# 	# topping1 = forms.CharField(label='Topping 1',max_length=100,widget=forms.Textarea)
# 	# topping2 = forms.CharField(label='Topping 2',max_length=100,widget=forms.PasswordInput)
# 	#toppings = forms.MultipleChoiceField(choices=[('pep','peperoni'),('cheese','cheese')])
# 	toppings = forms.MultipleChoiceField(choices=[('pep','peperoni'),('cheese','cheese')],widget=forms.CheckboxSelectMultiple)


#if wants to use the forms related to models then instead of creating it use ModelForm
class PizzaForm(forms.ModelForm):
	#size = forms.ModelChoiceField(queryset=Size.objects,empty_label=None,widget=forms.RadioSelect)
	#image = forms.ImageField()
	class Meta:
		model = Pizza
		fields = ['topping1','topping2','size'] #defined in models.py
		##by default name of label is capitalizing 1st word of model field
		labels = {'topping1':'Topping 1','topping2':'Topping 2'} #{fields of model:our desired name}
		#widgets = {'size':forms.CheckboxSelectMultiple}

class MultiplePizzaForm(forms.Form):
	number = forms.IntegerField(min_value=2,max_value=6)