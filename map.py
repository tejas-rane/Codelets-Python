income = [10, 30, 75]

def doubleMoney(dollars):
    return dollars * 2

newIncome = list(map(doubleMoney, income))
print(newIncome)