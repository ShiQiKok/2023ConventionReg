from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import pandas as pd

# Create your views here.
def index(request):
    excel_file_path = "./Registration Data.xlsx"
    df = pd.read_excel(excel_file_path)
    church_df = pd.read_excel(excel_file_path, sheet_name="church")
    churches = church_df.iloc[:, 0].to_list()
    names = df.iloc[:, 4].to_list()
    template = loader.get_template("home/index.html")
    
    context = {
        'churches': churches,
        'participants': names
    }

    return render(request, "home/index.html", context)

