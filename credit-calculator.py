import math

#Solicitud de información inicial al cliente
print('What do you want to calculate?')
print('type "n" - for count of months,')
print('type "a" - for annuity monthly payment,')
print('type "p" - for credit principal:')
calc_choice = input()

if calc_choice == 'n':
    print('Enter the credit principal:')
    credit_principal = int(input())
    print('Enter monthly payment:')
    monthly_payment = int(input())
    print('Enter credit interest:')
    credit_interest = int(input())
    nominal_interest_rate = (credit_interest / (12 * 100))
    years = math.log(monthly_payment / (monthly_payment - nominal_interest_rate * credit_principal), 1 + nominal_interest_rate)
    months = years % 12
    if years <= 1:
        if months == 1:
            print('You need 1 year and a month to repay this credit!')
        elif months < 1:
            print('You need 1 year to repay this credit!')
    else:
        print(f'You need {years} years and {months} months to repay this credit!')
elif calc_choice == 'a':
    print('Enter the credit principal:')
    credit_principal = float(input())
    print('Enter the count of periods:')
    periods_count = float(input())
    print('Enter credit interest:')
    credit_interest = float(input())
    print(f'Your annuity payment = {annuity_payment}!')    
elif calc_choice == 'p':
    print('Enter monthly payment:')
    monthly_payment = float(input())
    print('Enter the count of periods:')
    periods_count = float(input())
    print('Enter credit interest:')
    credit_interest = float(input())
    print(f'Your credit principal = {principal_output}!')    
else:
    print('Enter a valid choice!')