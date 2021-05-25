import math

help(math.ceil)

math.ceil(1.63)

def loan_emi(amount, duration, rate, down_payment = 0):
    loan_amount = amount - down_payment
    emi = loan_amount*rate*((1+rate)**duration)//(((1+rate)**duration)-1)
    emi = math.ceil(emi)
    return emi

emi_1 = loan_emi(1260000,8*12,0.1/12,300000)

emi_1

emi_2 = loan_emi(1260000,10*12,0.08/12)
emi_2

if emi_1 < emi_2:
    print("Option 1 has the lower EMI: ${}".format(emi_1))
else:
    print("Option 2 has the lower EMI: ${}".format(emi_2))

# amount = input("Enter loan amount: ")
# duration = input("Enter loan duration: ")
# rate = input("Enter rate of interest: ")
# down_payment = input("Enter down payment: ")


def loan_emi(amount, duration, rate, down_payment = 0):
    loan_amount = amount - down_payment
    emi = (loan_amount*rate*((1+rate)**duration))//(((1+rate)**duration)-1)
    emi = math.ceil(emi)
    return emi

emi = loan_emi(500000,30*12,0.025/12,10000)

emi

Now let's see one more question 

# Q: Shaun is currently paying back a home loan for a house he bought a few years ago. The cost of the house was $800,000. Shaun made a down payment of 25% of the price. He financed the remaining amount using a 6-year loan with an interest rate of 7% per annum (compounded monthly). Shaun is now buying a car worth $60,000, which he is planning to finance using a 1-year loan with an interest rate of 12% per annum. Both loans are paid back in EMIs. What is the total monthly payment Shaun makes towards loan repayment?

cost_of_house = 800000
loan_down_payment = 0.25*cost_of_house
loan_duration = 6*12
interest_rate = 0.07/12

emi_homeloan = loan_emi(amount = cost_of_house, duration = loan_duration, rate = interest_rate, down_payment = loan_down_payment)
print("EMI for home loan is ${}.".format(emi_homeloan))

cost_of_car = 60000
loan_down_payment = 0
loan_duration = 1*12
interest_rate = 0.12/12

emi_car_loan = loan_emi(amount = cost_of_car, duration = loan_duration, rate = interest_rate, down_payment = loan_down_payment)
print("EMI for car loan is ${}.".format(emi_car_loan))

print("Shawn makes a total monthly payment of ${} towards loan repayments.".format(emi_homeloan+emi_car_loan))


Q: If you borrow $100,000 using a 10-year loan with an interest rate of 9% per annum, what is the total amount you end up paying as interest?

loan_amount = 100000
loan_down_payment = 0
loan_duration = 10*12
interest_rate = 0.09/12

emi_loan_with_interest = loan_emi(amount = loan_amount, duration = loan_duration, rate = interest_rate, down_payment = loan_down_payment)
print("EMI for the loan is ${}.".format(emi_loan_with_interest))

print("I will make a total monthly payment of ${} towards loan repayment.".format(emi_loan_with_interest))

loan_amount = 15000
loan_down_payment = 0
loan_duration = 6*12
interest_rate = 0.02/12

emi_loan_1 = loan_emi(amount = loan_amount, duration = loan_duration, rate = interest_rate, down_payment = loan_down_payment)
print("EMI for the loan is ${}.".format(emi_loan_1))

print("I will make a total monthly payment of ${} towards loan repayment.".format(emi_loan_1))

loan_amount = 15000
loan_down_payment = 0
loan_duration = 3*12
interest_rate = 0.02/12

emi_loan_2 = loan_emi(amount = loan_amount, duration = loan_duration, rate = interest_rate, down_payment = loan_down_payment)
print("EMI for the loan is ${}.".format(emi_loan_2))

print("I will make a total monthly payment of ${} towards loan repayment.".format(emi_loan_2))

excess_interest = (emi_loan_2 - emi_loan_1)
excess_interest

def loan_emi(amount, duration, rate, down_payment = 0):
    loan_amount = amount - down_payment
    try:
        emi = (loan_amount*rate*((1+rate)**duration))//(((1+rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount/duration
    emi = math.ceil(emi)
    return emi

loan_amount = 100000
loan_down_payment = 0
loan_duration = 10*12
interest_rate = 0.00/12

emi_loan_without_interest = loan_emi(amount = loan_amount, duration = loan_duration, rate = interest_rate, down_payment = loan_down_payment)
print("EMI for the loan is ${}.".format(emi_loan_without_interest))

print("I will make a total monthly payment of ${} towards loan repayment.".format(emi_loan_without_interest))

total_excess_interest = (emi_loan_with_interest - emi_loan_without_interest)*10*12
print("The total excess interest is ${}.".format(total_excess_interest))

# Documenting fuctions using Docstrings

We can add some documentation within our function using a docstring. A docstring is simply a string that appears as the first statement within the function body, and is used by the help function. A good docstring describes what the function does, and provides some explanation about the arguments.

def loan_emi(amount, duration, rate, down_payment = 0):
    """Calculates the equal monthly installment (EMI) for a loan.
    
    Arguments:
        amount : Total amount to be spent (loan + down payment)
        duration: Duration of the loan (in months)
        rate: Rate of interest (monthly)
        down_payment(optional): Optional initial payment (Deducted from the loan amount)
    """
    loan_amount = amount - down_payment
    try:
        emi = (loan_amount*rate*((1+rate)**duration))//(((1+rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount/duration
    emi = math.ceil(emi)
    return emi

help(loan_emi)
