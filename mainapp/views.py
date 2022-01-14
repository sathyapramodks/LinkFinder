from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import datetime
import pandas as pd

# Create your views here.
def redirection(request):
    gsheet_id = '1JfZE3m-C_VEIfrdvJ97b5GjXXyTo6MVcfGxguRxhgbw'
    sheet_name = 'Sheet1'

    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheet_id, sheet_name)

    df = pd.read_csv(gsheet_url)

    datetime.datetime.now().day
    date = [str(datetime.datetime.now().day), str(datetime.datetime.now().month), str(datetime.datetime.now().year)]
    # date = [str(12),str(1),str(2022)]
    def change_month(date):
        if(date[1] == '1'):
            date[1] = 'Jan'
        elif(date[1] == '2'):
            date[1] = 'Feb'
        elif(date[1] == '3'):
            date[1] = 'Mar'
        elif(date[1] == '4'):
            date[1] = 'Apr'
        return date

    date = change_month(date)
    #print(date)
    new_date = "-".join(date)
    #print(new_date)

    value = df[df['Date'] == new_date]
    value.shape[0]
    if(value.shape[0]):
        #print(value.iloc[0]['Meet Link'])
        return redirect(value.iloc[0]['Meet Link'])
    else:
        #print('''No byts class today 
        #    or 
        #    Link not yet updated
        #    Check back later''')
        return render(request, 'index.html', {'date':new_date})