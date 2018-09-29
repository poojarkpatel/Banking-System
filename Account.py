from Person import Person
from random import randint
class Account:
	def __init__(self,name,address,date,month,year,branchName,gender,accountType):
		Person.__init__(self,name,address,date,month,year,gender)
		self.__branchName = branchName
		self.__accountType = accountType
		self.__ifsc = self.__getIfsc(self.__branchName)
		self.__accountNumber = randint(10000000,99999999)
		self.__balance = 10000


	def __getIfsc(self,branchName):
		ifscCodes = {'Motera':'1','ScienceCity':'2','shahibaug':'3'}
		return ifscCodes[branchName]

	def getAccountNumber(self):
		return self.__accountNumber

	def viewAccount(self):
		print("\n\n\nYour Account Details: ")
		print(f"Account Number :- {self.__accountNumber}")
		print(f"IFSC :- {self.__ifsc}")
		print(f"Branch Name:- {self.__branchName}")
		print(f"Name :- {self._name}")
		print(f"Gender :- {self._gender}")
		print(f"Address:- {self._address}")
		print(f"Date :- {self._date}")
		print(f"Month :- {self._month}")
		print(f"Year :- {self._year}")
		print(f"Balance :- {self.__balance}")
		exit = input("Press enter to exit :- ")

	def getMyIfsc(self):
		return self.__ifsc


	def credit(self):
		print("\n\n\nCredit ")
		amount = int(input("Enter the amount to be credited :- "))
		self.__balance += amount
		print(f"Your balance is :- {self.__balance}")
		exit = input("Press enter to exit :- ")

	def debit(self):
		print("\n\n\nDebit ")
		amount = int(input("Enter the amount to be debited :- "))
		self.__balance -= amount
		print(f"Your balance is :- {self.__balance}")
		exit = input("Press enter to exit :- ")

	def transaction(self,amount,var):
		if var == 'debit':
			self.__balance -= amount
		if var == 'credit':
			self.__ifsc += amount


	def clearAccount(self):
		self._name = ''
		self._address = ''
		self._date = ''
		self._month = ''
		self._year = ''
		self._gender = ''
		self.__accountNumber = ''
		self.__ifsc = ''
		self.__branchName =''
		self.__balance = ''
		

	def deleteAccount(self,name,date,month,year,accountNo,ifscCode):
		isvalid = True
		if self._name != name:
			return False
		if self._date != date:
			return False
		if self._month!= month:
			return False
		if self._year!= year:
			return False
		if self.__accountNumber != accountNo:
			return False
		if self.ifscCode != ifscCode:
			return False
		if isvalid True:
			return True
			self.clearAccount()





