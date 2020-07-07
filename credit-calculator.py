#Solicitud de información inicial al cliente
print('What do you want to calculate?')
print('type "n" - for count of months,')
print('type "a" - for annuity monthly payment,')
print('type "p" - for credit principal:')
calc_choice = input()

if calc_choice == 'n':
    print('Enter the credit principal:')
    credit_principal = float(input())
    print('Enter monthly payment:')
    monthly_payment = float(input())
    print('Enter credit interest:')
    credit_interest = float(input())
    if years <= 1:
        print(f'You need 1 year and {months} to repay this credit!')
    else:
        print(f'You need {years} years and {months} to repay this credit!')
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