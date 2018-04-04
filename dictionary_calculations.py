stocks ={
    'GOOG': 5.54,
    'FB':76.80,
    'AMAZON':10.10,
    'APPLE':99.0,
    'test':100.12
}


min = min(zip(stocks.values(), stocks.keys()))
print(min)