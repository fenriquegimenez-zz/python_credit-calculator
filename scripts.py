print('Enter the credit principal:')
credit_principal = int(input())
print('What do you want to calculate?')
print('type "m" - for count of months \ntype "p" - for monthly payment:')
type_of_calculation = input()
print('Enter the count of months:')
monthly_payment = int(input())


def credit_calculator(principal, calc, month):
    if calc == 'm':
        return round(principal / monthly_payment)
    if calc == 'p':
        return round(principal / month)
    print('It takes ')
