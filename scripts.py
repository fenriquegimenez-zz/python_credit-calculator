import math

print('Enter the credit principal:')
credit_principal = int(input())
print('What do you want to calculate?')
print('Type "m" for count of months \nType "p" - for monthly payment:')
calc_type = input()

if calc_type == 'm':
    print('Enter the monthly payment:')
    user_monthly_payment = int(input())
    credit_repay = credit_principal / user_monthly_payment
    if credit_repay == 1:
        print(f'It takes 1 month to repay the credit')
    elif credit_repay > 1:
        print(f'It takes {math.ceil(credit_repay)} months to repay the credit')
elif calc_type == 'p':
    print('Enter the count of months:')
    user_duration = int(input())
    monthly_payment = math.ceil(credit_principal / user_duration)
    last_payment = credit_principal - (user_duration - 1) * monthly_payment
    print(
        f'Your monthly payment = {monthly_payment} with last payment = {last_payment}')
