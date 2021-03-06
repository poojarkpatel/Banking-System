from Account import Account
class BankingSystem:

	def __init__(self):
		self.__accountsDict = {}



	def displayMenu(self):
		print("===============BANKING SYSTEM===================")
		print("1. ADD ACCOUNT")
		print("2. VIEW ACCOUNT")
		print("3. CREDIT")
		print("4. DEBIT")
		print("5. TRANSACTION")
		print("6. DELETE ACCOUNT")
		print("7. EXIT")
		self.__choice = int(input("Enter your choice :- "))
		self.__performOPerations(self.__choice)
		self.displayMenu()


	def __performOPerations(self,choice):
		if choice is 1:
			name,address,date,month,year,branchName,gender,accountType = self.__getUserDetails()
			bankAccount = Account(name,address,date,month,year,branchName,gender,accountType)
			self.__accountsDict[bankAccount.getAccountNumber()] = bankAccount
			bankAccount.viewAccount()
			
		elif choice is 2:
			self.accountNumber = int(input("Enter your account number :- "))
			bankAccount = self.__accountsDict[self.accountNumber]
			bankAccount.viewAccount()
		elif choice is 3:
			self.accountNumber = int(input("Enter your account Number :- "))
			bankAccount = self.__accountsDict[self.accountNumber]
			ifsc = input("Enter your ifsc code :- ")
			if bankAccount.getMyIfsc() == ifsc:
				bankAccount.credit()

		elif choice is 4:
			self.accountNumber = int(input("Enter your account Number :- "))
			bankAccount = self.__accountsDict[self.accountNumber]
			ifsc = input("Enter your ifsc code :- ")
			if bankAccount.getMyIfsc() == ifsc:
				bankAccount.debit()
			
		elif choice is 5:
			self.senderAccountNumber = int(input("Enter sender's account Number :- "))
			senderBankAccount = self.__accountsDict[self.senderAccountNumber]
			self.senderIfsc =  input("Enter sender's ifsc code :- ")
			amount = int(input("Enter the amount to be transferred :-"))
			self.receiverAccountNumber = int(input("Enter beneficiary's account Number :- "))
			receiverBankAccount = self.__accountsDict[self.receiverAccountNumber]
			self.receiverIfsc =  input("Enter sender's ifsc code :- ")
			if senderBankAccount.getMyIfsc() == self.senderIfsc:
				senderBankAccount.transaction(amount,'debit')
			if receiverBankAccount.getMyIfsc() == self.receiverIfsc:
				receiverBankAcccount.transaction(amount,'credit')
			print("Transaction successfull")

		elif choice is 6:
			name = input("Enter your name :-")
			date = int(input("Enter date :-"))
			month = int(input("Enter month :-"))
			year = int(input("Enter year :-"))
			ifsc = input("Enter ifsc :-")
			self.accountNumber = int(input("Enter your account number :- "))
			bankAccount = self.__accountsDict[self.accountNumber]
			valid = bankAccount.deleteAccount(name,date,month,year,self.accountNumber,ifsc)
			if valid:
				self.__accountsDict.pop(self.accountNumber)
				del bankAccount
				print("Account deleted.")

		elif choice is 7:
			raise SystemExit
		else:
			print("invalid input")

	def __getUserDetails(self):
		name = input("Enter your name :- ")
		address = input("Enter your address :- ")
		date = int(input("Enter date :- "))
		month = int(input("Enter month :- "))
		year = int(input("Enter year :- "))
		ifsc = input("1.Motera 2.Science City 3.Shahibaug \n Choose your Branch :- ")
		if ifsc =='1':
			branchName = 'Motera'
		if ifsc =='2':
			branchName = 'ScienceCity'
		if ifsc =='3':
			branchName = 'Shahibaug'

		gender = input("1.Male 2.Female \n Choose your Gender :- ")
		if gender =='1':
			gender = 'Male'
		if gender =='2':
			gender = 'Female'


		accountType = input("1.Current 2.Savings \n Choose your Account Type :- ")
		if accountType is "1":
			accountType = "Current" 
		elif accountType is "2":
			accountType = "Savings"

		return name,address,date,month,year,branchName,gender,accountType








		

