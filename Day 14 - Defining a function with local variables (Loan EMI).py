Question :
Radha is planning to buy a house that costs $1,260,000. She considering two options to finance her purchase:

Option 1: Make an immediate down payment of $300,000, and take loan 8-year loan with an interest rate of 10% per annum (compounded monthly) for the remaining amount.

Option 2: Take a 10-year loan with an interest rate of 8% per annum (compounded monthly) for the entire amount. Both these loans have to be paid back in equal monthly installments (EMIs). Which loan has a lower EMI among the two?

Since we need to compare the EMIs for two loan options, defining a function to calculate the EMI for a loan would be a great idea. The inputs to the function would be cost of the house, the down payment, duration of the loan, rate of interest etc.

We'll build this function step by step.

def loan_emi(amount):
    emi = amount//12
    print("The EMI is ${}.".format(emi))
loan_emi(1260000)
The emi is $105000.
loan_emi(960000)
The emi is $80000.
Lets now add a second argument which is the duration of the loan.

def loan_emi(amount, duration):
    emi = amount//duration
    print("The EMI is ${}.".format(emi))
loan_emi(1260000,10*12)
The emi is $10500.
loan_emi(1260000,8*12)
The emi is $13125.
Return Values : It is used to return and store the result in variables for easier comparision. This is done using the return statement.

def loan_emi(amount, duration):
    emi = amount//duration
    return emi
emi_1 = loan_emi(75000,6*12)
emi_2 = loan_emi(36000,6*12)
emi_1
1041
emi_2
500
emi_1-emi_2
541
Now let's add the downpayment into our function. We can make it as a optional argument by giving it a value of 0.

def loan_emi(amount, duration, down_payment = 0):
    loan_amount = amount - down_payment
    emi = loan_amount//duration
    return emi
emi_1 = loan_emi(75000,6*12,30000)
emi_2 = loan_emi(36000,6*12,10000)
emi_3 = loan_emi(55000,6*12)
emi_1
625
emi_2
361
emi_3
763
Now let's add the interest calculation into the function. Interest is calculated as (Pr(1+n)^n)/((1+r)^n-1).

def loan_emi(amount, duration, rate, down_payment = 0):
    loan_amount = amount - down_payment
    emi = loan_amount*rate*((1+rate)**duration)//(((1+rate)**duration)-1)
    return emi
emi_1 = loan_emi(1260000,8*12,0.1/12,300000)
emi_1
14567.0
emi_2 = loan_emi(1260000,10*12,0.08/12)
emi_2
15287.0
