stocks ={
    'GOOG': 5.54,
    'FB':76.80,
    'AMAZON':10.10,
    'APPLE':99.0,
    'test':100.12
}

val = min(zip(stocks.values(),stocks.keys()))
print(val)

val = max(zip(stocks.values(),stocks.keys()))
print(val)

val = sorted(zip(stocks.values(),stocks.keys()))
print(val)

