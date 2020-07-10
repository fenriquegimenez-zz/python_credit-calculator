import math

user_choice = input('What do you want to calculate?\n'
                    'type "n" - for count of months,\n' 
                    'type "a" - for annuity monthly payment,\n'
                    'type "p" - for credit principal:')

if user_choice == 'n':
    credit_principal = int(input('Enter the credit principal:'))
    monthly_payment = int(input('Enter monthly payment:'))
    credit_interest = float(input('Enter credit interest:'))
    nominal_interest_rate = (credit_interest / (12 * 100))
    total_months = math.ceil(math.log(monthly_payment / (monthly_payment 
    - nominal_interest_rate * credit_principal), 
    1 + nominal_interest_rate))
    years = total_months // 12
    months = round(total_months % 12)
    if years <= 1:
        if years == 1:
            if months == 1:
                print('You need a year and a month to repay this credit!')
            elif months < 1:
                print('You need a year to repay this credit!')
            else:
                print(f'You need a year and {months} month to repay this credit!')
        elif years < 1:
            print(f'You need {months} months to repay this credit!')
    else:
        if months <= 0:
            print(f'You need {years} years to repay this credit!')
        else:
            print(f'You need {years} years and {months} months to repay this credit!')
elif user_choice == 'a':
    credit_principal = int(input('Enter the credit principal:'))
    periods_count = int(input('Enter the count of periods:'))
    credit_interest = float(input('Enter credit interest:'))
    nominal_interest_rate = (credit_interest / (12 * 100))
    annuity_payment = int(math.ceil(credit_principal * ((nominal_interest_rate 
    * (1 + nominal_interest_rate) ** periods_count) 
    / (((1 + nominal_interest_rate) ** periods_count) - 1))))
    print(f'Your annuity payment = {annuity_payment}!')    
elif user_choice == 'p':
    monthly_payment = float(input('Enter monthly payment:'))
    periods_count = float(input('Enter the count of periods:'))
    credit_interest = float(input('Enter credit interest:'))
    nominal_interest_rate = (credit_interest / (12 * 100))
    principal_output = (monthly_payment / ((nominal_interest_rate * 
    (1 + nominal_interest_rate) ** periods_count) / (((1 + nominal_interest_rate) 
    ** periods_count) - 1)))
    print(f'Your credit principal = {round(principal_output)}!')    
else:
    print('Enter a valid choice!')