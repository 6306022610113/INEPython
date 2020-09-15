def main():
    try:
        hours = int(input('How many hours did you work? '))

        pay_rate = float(input('Enter you horly pay rate: '))

        gross_pay = hours * pay_rate

        print('Gross pay: $', format(gross_pay, ',.2f'), sep='')
    except ValueError as err:
        print(err)

main()