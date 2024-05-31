from django.shortcuts import render, redirect
from .forms import filesForm
from django.contrib import messages
import pandas as pd
from .models import files

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
	context ={}
	myFile = files.objects.get(pk=pk)	
	myFile_path = myFile.file.path

	if myFile_path.endswith('.csv'):
		df = pd.read_csv(myFile_path)
	else:
		df = pd.read_excel(myFile_path)
	
	print('dataframe:', df.head(2))

	state_column = next((col for col in df.columns if 'state' in col.lower()), None)
	dpd_column = next((col for col in df.columns if 'dpd' in col.lower()), None)
	if state_column is None or dpd_column is None:
		print('No column related to state or DPD found')
		messages.error(request, 'No column related to state or DPD found')
	else:
		# Group by 'State' and 'DPD' columns and count the number of occurrences
		summary = df.groupby([state_column, dpd_column]).size().reset_index(name='Count')

		# Convert the DataFrame to HTML to display it in your template
		context['summary'] = summary.to_html(index=False)


	return render(request, 'app/summary_report.html',context)