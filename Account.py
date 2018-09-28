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