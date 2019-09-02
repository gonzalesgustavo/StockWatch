API_KEY = "ADD KEY HERE"
API_STR = "https://cloud.iexapis.com/stable/stock/"
API_STR_TWO = "https://cloud.iexapis.com/stable/stock/market/batch"


def reqManager(tiker):
    return f"{API_STR}{tiker}/quote?token={API_KEY}"


def multTickManager(tickers):
    return f"{API_STR_TWO}?symbols={tickers}&types=quote&token={API_KEY}"
