import math
# request user to input which calculation they would like to do by selecting between either an investment or a body
# dispaly that a user must select between a nond and investment option
# how the user capitalises their selection should not affect how the program proceeds
# assume that amounts should be denominated in dollars
print("Choose either \"investment\" or \"bond\" from the menu below to proceed: ")
print("Investment   -   to calculate the amount of interest you'll earn on your investment")
print("Bond         -   to calculate the amount you'll have to pay on a home loan")
calculator_type = input("Selection Type:  ")

# if user selects an investment, request user to input the different data required to calculate their interest on their investment
if calculator_type.lower() == "investment":
    deposit_amount = float(input("What is the amount you would like to deposit: "))
    interest_rate = float(input("Enter the interest rate as a percentage (without including the \"%\" symbol): "))

    # assuming that users can enter partial years to represent months, and so casting the number of years to a float
    number_years = float(input("Enter the number of years you plan on investing: "))

    # request the user to select the type of interest they would like to calculate (between simple or compound interest).
    # use the input information above to calculate the interest amount based on their interest type selection using a nested if and elif statement
    interest_type = input("Select whether you would like \"simple\" or \"compound\" interest: ")
    if interest_type.lower() == "simple":
        simple_interest = round(deposit_amount * (1 + (interest_rate/100)*number_years),2)
        print(f"The total future value of your investment if simple interest is applied is: ${simple_interest}")
    elif interest_type.lower() == "compound":
        compound_interest = round(deposit_amount * math.pow((1 +interest_rate/100),number_years))
        print(f"The total future value of your investment if compound interest is applied is: ${compound_interest}")

#if user selects a bond, request user to input the different data required to calculate the interest on their bond
elif calculator_type.lower() == "bond":
    pv_house = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the annual interest rate as a percentage (without including the \"%\" symbol): "))

    # casting to integer as assuming that users must enter full months (i.e. can't show partial months to represent days)
    repayment_months = int(input("Enter the number of months you plan to repay the bond: "))

    # calculate the amount that will have to be repaid on a home loan each month
    monthly_repayment_amount = round(((interest_rate/100)/12 * pv_house)/(1 - (1 + (interest_rate/100)/12)**(-repayment_months)),2)
    print(f"The amount that you will have to repay each month for the bond is: ${monthly_repayment_amount}")
else:
    print("Invalid input: Neither the investment or bond option was selected. Please select either \"investment\" or \"bond\" from the menu to proceed. ")  
