from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import numpy as np
import joblib
import pandas as pd
import sklearn
# Create your views here.
import pickle


model=joblib.load('LoanPredictionModel_pkl1')


def index(request):
    return render(request,'home.html')
def result(request):
    print (request)
    if request.method == 'POST':
        temp={}
        temp['Gender']=request.POST.get('Gender')
        temp['Married']=request.POST.get('Married')
        temp['Dependents']=request.POST.get('Dependents')
        temp['Education'] = request.POST.get('Education')
        temp['Self_Employed'] = request.POST.get('Self_Employed')
        temp['ApplicantIncome'] = request.POST.get('ApplicantIncome')
        temp['CoapplicantIncome'] = request.POST.get('CoapplicantIncome')
        temp['LoanAmount'] = request.POST.get('LoanAmount')
        temp['Loan_Amount_Term'] = request.POST.get('Loan_Amount_Term')
        temp['Credit_History'] = request.POST.get('Credit_History')
        temp['Property_Area'] = request.POST.get('Property_Area')

        print(temp.keys())
        print(temp)
        out = pd.DataFrame({'x': temp}).transpose()
        print(out)
        prediction=model.predict(out)
        print(prediction)
        if prediction==0:
            ans="can't geting loan"
        else:
            ans='you will get loan'
        print(ans)

    #return  ans

    #return HttpResponse(template.render())
    return render(request, 'result.html', {'ans': ans})
def about(request):
    return render(request,'about.html')

