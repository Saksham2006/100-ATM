class ATM:
    def __init__(self, card, pin):
        self.card = card
        self.pin = pin
    
    def func(self):
        response = '0'
        bal = 50

        if response == '0':
            response = input(str('Welcome to the ATM App, please choose your action.\n1. Withdraw\n2. Deposit\n3. View Balance\n\nEnter your response.'))

        if response == '1':
            withdraw = input('How much would you like to withdraw?')
            if int(withdraw) <= 0:
                print('Invalid amount')
            else:
                bal = bal - int(withdraw)
                if bal <= 0:
                    print('You do not have enough money in your card, cancelling transaction.')
                    bal = bal + int(withdraw)
                else:
                    print(f'Transaction successful, you now have ${bal} left in your account')
                    response = '0'

        if response == '2':
            deposit = input('How much would you like to deposit?')
            digit = deposit.isdigit()
            if deposit == '':
                print('Invalid amount')
                response = '2'
            elif digit == False:
                print('Invalid amount')
                response = '2'
            elif int(deposit) <= 0:
                print('Invalid amount')
                response = '2'
            else:
                bal = bal + int(deposit)
                print(f'Transaction successful, you now have ${bal} in your account')
                response = '0'

        if response == '3':
            print(f'You have ${bal} in your account')
            response = '0'

        if (int(response) > 3):
            print('Invalid response')
            response = '0'
        
        if (int(response) < 0):
            print('Invalid response')
            response = '0'

card = input('Enter your card number - ')
pin = input('Enter the pin - ')

digitcard = card.isdigit()
digitpin = pin.isdigit()

if digitcard == True and digitpin == True:
    atm = ATM(card, pin)
    atm.func()

else:
    print('Your Card Number or Pin is is not a digit')