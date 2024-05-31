from django.shortcuts import render, redirect
from .forms import filesForm
from django.contrib import messages

# Create your views here.
def upload_file(request):
	context={}
	if request.method == 'POST':
		form = filesForm(request.POST, request.FILES)
		if form.is_valid():
			upload_file = form.save()
			print('data Saved')
			messages.success(request, 'File uploaded successfully')
			return redirect('summary_report', pk = upload_file.pk )
		else:
			messages.error(request, 'Please upload a valid file')
			context['form'] = form
			return render(request, 'app/upload_file.html', context)
	
	form = filesForm()
	context['form'] = form
	return render(request, 'app/upload_file.html', context)
	

def summary_report(request, pk):
	return render(request, 'app/summary_report.html')