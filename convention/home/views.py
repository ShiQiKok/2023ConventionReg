from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Create your views here.
def index(request):



    load_sheet()


    template = loader.get_template("home/index.html")
    return HttpResponse(template.render())


def load_sheet():
   
    # Set up credentials
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(".\convention-registration-0dc415e4d876.json", scope)
    client = gspread.authorize(creds)

    # Open the Google Sheet using its title
    sheet_title = "Registration - Name Card List"
    worksheet = client.open(sheet_title).sheet1  # You can replace "sheet1" with the name of your specific worksheet

    # Get all values from the worksheet
    all_values = worksheet.get_all_values()

    # Print the values
    for row in all_values:
        print(row)
