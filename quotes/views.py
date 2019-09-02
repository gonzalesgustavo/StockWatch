from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StockForm

import requests
import json

# DB
from .models import Stock

# Config files to hold api_key
from config import conf

# Home Route


def index(request):
    # Check if method is a POST
    if request.method == 'POST':
        # Get ticker passed in
        ticker = request.POST['ticker']
        try:
            # Put together query string
            api_str = conf.reqManager(ticker)
            # GET: data
            api_get_request = requests.get(api_str)
            # Parse data
            api = json.loads(api_get_request.content)
            # catch errors from API or lack of ticker
            messages.success(request, ("Symbol was successfuly found!"))
        except Exception as e:
            # print error (testing)
            # print(e)
            # Return error as string
            api = "Error"
        # Render and pass infromaiton to the view
        return render(request, 'index.html', {'api_get': api})
    else:
        # render view with simple message
        return render(request, 'index.html', {'ticker': 'Enter A ticker Symbol...'})


def about(request):
    return render(request, 'about.html', {})


def stock_add(request):
    # Check if method is a POST
    if request.method == 'POST':
        # Get ticker passed in
        form = StockForm(request.POST or None)
        # check forms validity
        if form.is_valid():
            # Save
            form.save()
            # Add message
            messages.success(request, ("Stock was successfully saved"))
            # Redirect back to stock_add
            return redirect('stock_add')
    else:
        # Get all tickers from DB
        tickers = Stock.objects.all()
        ticker_array = []
        for ticker in tickers:
            ticker_array.append(ticker.symbol)
        try:
            q_ready_str = ",".join(ticker_array)
            api_str = conf.multTickManager(q_ready_str)
            api_get_request = requests.get(api_str)
            api_json = json.loads(api_get_request.content)
            api = []
            for item in api_json:
                api.append(api_json[item]['quote'])
            return render(request, 'stock_add.html', {'ticker': tickers, 'api': api})
        except Exception as e:
            return render(request, 'stock_add.html', {'ticker': tickers, 'api': 'error'})


# Delete symbol from DB
def delete_ticker(request, symbol_id):
    # Get item from DB based on id
    symbol = Stock.objects.get(pk=symbol_id)
    # Delete item
    symbol.delete()
    # Set a message (possibly a feature to add later)
    messages.success(request, ("Symbol has been deleted!"))
    # Redirect back to stock_add
    return redirect("stock_add")
