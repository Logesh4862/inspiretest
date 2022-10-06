import re
from django.shortcuts import render
from django.http import JsonResponse
from numpy import ndarray
from predict.models import CleanedData
from django.views.generic import ListView, View
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB



class HomePage(ListView):
    template_name = 'index.html'
    model = CleanedData
    context_object_name = 'news'
    paginate_by = 8
    queryset = CleanedData.objects.all().order_by('record_date')

class FindCategory(View):

    def get(self, request):
        return render(request, "category.html", {})
    
    def post(self, request):
        content = request.POST['content']
        category = self.PrepareModel(content)
        if type(category) is ndarray:
            return render(request, 'category.html', context={'category': category[0].upper(), 'holder':content})
        elif type(category) is str:
            return render(request, 'category.html', context={'category': category, 'holder':content})
        else:
            return render(request, 'category.html', context={'category': None, 'holder':''})

    
    def PrepareModel(self, content):
        try:
            dataSet = pd.DataFrame(list(CleanedData.objects.values('snippet', 'category__name')))
            x = dataSet["snippet"].values.astype('U')
            y = dataSet["category__name"].values.astype('U')
            cv = CountVectorizer()
            X = cv.fit_transform(x)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
        except Exception as e:
            print(e)
            print("Failed Prepare Trained Data")
        else:
            model = MultinomialNB()
            model.fit(X_train,y_train)
            input_data = cv.transform([content]).toarray()
            output = model.predict(input_data)
            return(output if output else 'Unable to Predict')