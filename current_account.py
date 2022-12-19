from general_account import account


class CurrentAccount(account):
    '''subclass of account'''

    def __init__(self, first_name: str, agency: int,
                 number_account: int, balance: float, limit=1000):
        '''constructor subclass account'''

        super().__init__(first_name, agency, number_account, balance)
        self._limit = limit

    def withdraw(self, value):
        '''retire amount to balance in current account'''

        if self._balance + self._limit < value:
            return print("You don't have enough balance for withdraw")
        else:
            self._balance -= value

    def balance_transfer(self, first_account: account,
                         second_account: account, value: float):
        '''Transfer values between accounts'''

        if self._balance + self._limit < value:
            return print("You don't have enough balance for transfer")
        else:
            first_account._balance -= value
            second_account._balance += value
