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
# use a while loop to request the user to try again if they do not select from the options provided
# Create a try and except handling within a while loop to print an error message if the user enters a value that is not a float (which is invalid)
# and request to try again until the user enters valid float number inputs. This is done wherever a float is required as the input
while True:
    if calculator_type.lower() == "investment":
        while True:
            try:
                deposit_amount = float(input("What is the amount you would like to deposit: "))
                if deposit_amount >= 0:  
                    break
                else:
                    print ("Error: Invalid input. The amount cannot be less than 0. Please try again")
            except ValueError:
                print("Invalid input: The value entered is not a number nor a float. Please try again.")

        while True:
            try:
                # Assuming interest rates can be negative in the case of real interest (i.e. where nominal- inflation) and so no defensive handling
                interest_rate = float(input("Enter the interest rate as a percentage (without including the \"%\" symbol): "))
                break
            except ValueError:
                print("Invalid input: The value entered is not a number nor a float. Please try again.")

        while True:
            # assuming that users can enter partial years to represent months, and so casting the number of years to a float
            try:
                number_years = float(input("Enter the number of years you plan on investing: "))
                if number_years>= 0:  
                    break
                else:
                    print ("Error: Invalid input. The number of years cannot be a negative number. Please try again.")
            except ValueError:
                 print("Invalid input: The value entered is not a number nor a float. Please try again.")
            
        # request the user to select the type of interest they would like to calculate (between simple or compound interest).
        # use the input information above to calculate the interest amount based on their interest type selection using a nested if and elif statement
        # create a while loop to request the user to try again if they do not select from the options provided.
        while True:
            interest_type = input("Select whether you would like \"simple\" or \"compound\" interest: ")
            if interest_type.lower() == "simple":
                simple_interest = round(deposit_amount * (1 + (interest_rate/100)*number_years),2)
                print(f"The total future value of your investment if simple interest is applied is: ${simple_interest}")
                break
            elif interest_type.lower() == "compound":
                compound_interest = round(deposit_amount * math.pow((1 +interest_rate/100),number_years))
                print(f"The total future value of your investment if compound interest is applied is: ${compound_interest}")
                break
            else: 
                print("Invalid input: Neither the \"simple\" or \"compound\" option was selected. Please try again.")
        break

    # if user selects a bond, request user to input the different data required to calculate the interest on their bond
    # Create a try and except handling within a while loop to print an error message if the user enters a value that is not a float (which is invalid)
    # and request to try again until the user enters valid float number inputs. This is done wherever a float is required as the input.
    elif calculator_type.lower() == "bond":
        while True:
            try:
                pv_house = float(input("Enter the present value of the house: "))
                if pv_house >= 0:  
                    break
                else:
                    print ("Error: Invalid input. The amount cannot be less than 0. Please try again")
            except ValueError:
                print("Invalid input: The value entered is not a number nor a float. Please try again.")

        while True:
            try:
                interest_rate = float(input("Enter the annual interest rate as a percentage (without including the \"%\" symbol): "))
                break
            except ValueError:
                print("Invalid input: The value entered is not a number nor a float. Please try again.")

        # casting to integer as assuming that users must enter full months (i.e. can't show partial months to represent days)
        # Create a try and except handling within a while loop to print an error message if the user enters a value that is not an integer, which is inavlid.
        while True:
            try:
                repayment_months = int(input("Enter the number of months you plan to repay the bond: "))
                if repayment_months >= 0: 
                    break
                else:
                    print ("Error: Invalid input. The number of months cannot be a negative number. Please try again.")
            except ValueError:
                print("Invalid input: The value entered is not an integer. Please try again.")

        # calculate the amount that will have to be repaid on a home loan each month
        monthly_repayment_amount = round(((interest_rate/100)/12 * pv_house)/(1 - (1 + (interest_rate/100)/12)**(-repayment_months)),2)
        print(f"The amount that you will have to repay each month for the bond is: ${monthly_repayment_amount}")
        break

    else:
        calculator_type = input("Invalid input: Neither the investment or bond option was selected. Please try again: ")