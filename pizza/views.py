from django.shortcuts import render
from pizza.forms import PizzaForm,MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza

def home(request):
	return render(request ,'pizza/home.html')

def order(request):
	multiple_form = MultiplePizzaForm() #we have to show it on every order page
	if request.method == 'POST':
		filled_form = PizzaForm(request.POST) #take all info from post and include it here in create a newform object
		print("Areeba",filled_form)
		if filled_form.is_valid():  #return true if fields are same as we defined in our forms.py
			print("clean_data",filled_form.cleaned_data['size'])
			note = "Thanks for ordering! Your %s %s and %s pizza is on its way!" %(filled_form.cleaned_data['size'],
			filled_form.cleaned_data['topping1'], #.cleaned_data['forms_field/models_field']
			filled_form.cleaned_data['topping2'],) #form.cleaned_data is an dictionary object that contains all validated data
			created_pizza = filled_form.save()   #save and  return pizza object with id
			print("created_pizza",created_pizza.id)
			created_pizza_pk = created_pizza.id
			filled_form  = PizzaForm() #for server validation new form name should be same as post method
		else:
			created_pizza_pk = None
			note = 'Pizza order has failed. Try again!'
		return render(request, 'pizza/order.html',{'created_pizza_pk':created_pizza_pk,'pizzaform':filled_form ,'note':note,'multiple_form':multiple_form})
	else:
		form = PizzaForm()
		print("formmmm", form)
		return render(request, 'pizza/order.html',{'pizzaform':form,'multiple_form':multiple_form})
	
def pizzas(request):
	number_of_pizzas = 2
	filled_multiple_pizzas_form = MultiplePizzaForm(request.GET) #get data from request.form and filled in form
	if filled_multiple_pizzas_form.is_valid():
		number_of_pizzas = filled_multiple_pizzas_form.cleaned_data['number']
	#Make a class which will deal with multiple forms
	PizzaFormSet = formset_factory(PizzaForm,extra=number_of_pizzas) #specify form which we want multiple time and their quantity in extra
	formset = PizzaFormSet()  #multiple forms have been called
	
	if request.method == 'POST':
		filled_formset = PizzaFormSet(request.POST)
		if filled_formset.is_valid():
			for form in filled_formset:
				form.save()
			note = 'Pizzas have been ordered'
		else:
			note = 'Order was not created,PLease try again!'
		return render(request,'pizza/pizzas.html',{'note':note,'formset':formset,'no':number_of_pizzas})
	else:
		return render(request,'pizza/pizzas.html',{'formset':formset,'no':number_of_pizzas})

def edit_order(request,pk):
	pizza = Pizza.objects.get(pk=pk)
	print("pizza",pizza)
	form = PizzaForm(instance=pizza) #show that form which is populated with values where pk=pizza.pk
	if request.method == 'POST':
		filled_form = PizzaForm(request.POST,instance=pizza) #update the data filled by user (obtained from Post request)
		if filled_form.is_valid():
			filled_form.save()
			form = filled_form
			note = "Order has been updated"
			return render (request,'pizza/edit_order.html',{'note':note,'pizza':pizza,'pizzaform':form})
	return render (request,'pizza/edit_order.html',{'pizza':pizza,'pizzaform':form})


