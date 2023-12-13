import pandas as pd
import numpy as np

sellPrice = 2400
cost = 1500
profit = sellPrice - cost
demand=[10, 15, 20]
probability = [0.3, 0.6,0.1]

def calc_tables(probability, result, resultSum, sellPrice, cost, profit, demand, lost_profit):
    temp=[]
    for i in range(len (demand)):
        for j in range(len(demand)):
            soldPerMonth = min(demand[i], demand[j]) # Продано за місяць
            # Не продано за місяць
            notSoldPerMonth = max(0, demand[i] - demand[j])
            expectedIncome = profit * soldPerMonth # очікубаний чистий дохід
            expectedIncomeWithLost = expectedIncome - cost * notSoldPerMonth + lost_profit * \
                notSoldPerMonth # Очікуваний дохід з рахуванням витрат та втрати при непродажу
            temp.append([
                probability[j],
                demand[i], # Зробено розчинника за місяць demand [j], # Попит розчинника за місять
                soldPerMonth,
                max( 0, demand[j] -demand[i]),
                notSoldPerMonth, # Не продано за місяць
                expectedIncome,
                expectedIncomeWithLost, # Очікуємий дохід з врахуванням витрат
                expectedIncome * probability[j],
                expectedIncomeWithLost * probability[j],
            ])
        lastElement = len(temp[0])
        for i in range(0, len(temp), len (demand)) :
            temp_slice = temp[i:1+len (demand)]
            expectedIncomeSum = np.sum(temp_slice, axis=0)[lastElement-2]
            expectedIncomeSumWithLost = np.sum(
                temp_slice, axis=0) [lastElement-1]
        resultSum.append([expectedIncomeSum, expectedIncomeSumWithLost])
        result.append (temp)

    


result =[]
expectedIncomeSum = []
calc_tables(probability, result, expectedIncomeSum, sellPrice, cost, profit, demand,0)
def print_tables(result, demand, expectedIncomeSum):
    for i in range(len(result)):
        df = pd.DataFrame(result[i], columns=["Ймовірність", "Зроблено за місяць", "Попит за місяць",
"Продано за місяць"
"Не продано за місяць", "Незадоволений попит", "Очікуваний чистий дохід", "Дохід з врахуванням витрат"])
        print (df)
        for i in range(len (demand)):
            print("Очікуваний дохід:", expectedIncomeSum[i][0])
            print ("Очікуваний дохід з урахуванням витрат",
                    expectedIncomeSum [1][1])
        maxExpectedProfit = np.max(expectedIncomeSum, axis=0)[0]
        print ("Максимальний дохід: ", maxExpectedProfit)
        maxExpectedProfitWithLost = np.max(expectedIncomeSum, axis=0)[1]
        print( "Максимальний дохід з врахуванням ризику: ", maxExpectedProfitWithLost)
print_tables (result, demand, expectedIncomeSum)
    