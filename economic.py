FaceValue = 10000000
CouponRate = 0.06
InterestPayment = FaceValue * CouponRate
MarketRate = 0.07
TimeToMaturity = 4

FacePresentValue = FaceValue / pow((1 + MarketRate), TimeToMaturity)
CarryingValue_Initial = FacePresentValue

for TimeHolded in range(1, TimeToMaturity + 1):
    # PresentValue = (FaceValue * pow((1 + CouponRate), 5)) / pow((1 + MarketRate), TimeHolded)
    InterestPresentValue = InterestPayment / pow((1 + MarketRate), TimeHolded)
    print("InterestPresentValue:", InterestPresentValue)
    CarryingValue_Initial += InterestPresentValue

print("CarryingValue_Initial:", CarryingValue_Initial)


TotalInterestExpense = 0
AmorisedAmount = 0
for TimeHolded in range(1, TimeToMaturity + 1):
    InterestExpnse = (CarryingValue_Initial + AmorisedAmount) * MarketRate
    print("Interest Expense:",InterestExpnse)
    AmorisedAmount += InterestExpnse - InterestPayment
    TotalInterestExpense += InterestExpnse

print("TotalInterestExpense:",TotalInterestExpense)
# a = FaceValue * pow((1+CouponRate),5)
# b = FaceValue * pow((1+MarketRate),5)
# print(a,b,a - b)

