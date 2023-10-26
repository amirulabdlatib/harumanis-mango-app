from django.shortcuts import render
from joblib import load
from django.conf import settings
import os
import pickle
import pandas as pd

model_path = os.path.join(settings.BASE_DIR, 'saveModel', 'rf_model.pkl')

# Create your views here.
def index(request):

    context ={'result':None}

    if request.method=='POST':

        with open(model_path,'rb') as file:
            ml_model = pickle.load(file) 

        weight=request.POST.get('weight')
        length=request.POST.get('length')
        circumference=request.POST.get('circumference')

        input_data = pd.DataFrame({
            'Weight': [weight],
            'Length': [length],
            'Circumference': [circumference]
        })

        mango_result = ml_model.predict(input_data)

        if mango_result == 0:
            y_preds = 'Grade A'
        elif mango_result == 1:
            y_preds = 'Grade B'
        else:
            y_preds ='Grade C'
        
        context['result'] = y_preds

    return render(request,'myapp/index.html',context=context)

