from general_account import account


class SavingAccount(account):
    '''Subclass account'''

    def __init__(self, first_name: str, agency: int,
                 number_account: int, balance: float):
        super().__init__(first_name, agency, number_account, balance)

    def withdraw(self, value):
        '''retire amount to balance in saving account'''

        if self._balance < value:
            return print("You don't have enough balance for withdraw")
        else:
            self._balance -= value

    def balance_transfer(self, first_account: account,
                         second_account: account, value: float):
        '''Transfer values between accounts'''

        if self._balance < value:
            return print("You don't have enough balance for transfer")
        else:
            first_account._balance -= value
            second_account._balance += value
