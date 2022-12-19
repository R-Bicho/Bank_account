from abc import ABC, abstractmethod


class account(ABC):
    '''
    General account for create another accounts like
    current account and saving account
    '''

    def __init__(self, first_name: str, agency: int,
                 number_account: int, balance: float):
        '''Contructor general accounts'''
        self._first_name = first_name
        self._agency = agency
        self._number_account = number_account
        self._balance = balance

    @abstractmethod
    def withdraw(self, value: float):
        '''retire amount to balance'''
        ...

    @abstractmethod
    def balance_transfer(self, first_account,
                         second_account, value):
        '''Transfer values between accounts'''
        ...

    def deposit(self, value: float):
        '''Add amount to balance'''
        self._balance += value

    def extract(self):
        '''Details of account, like balance, name, agency'''
        print(f'Name: {self._first_name}')
        print(f'Agency: {self._agency}')
        print(f'Number Account: {self._number_account}')
        print(f'Balance: {self._balance}')
