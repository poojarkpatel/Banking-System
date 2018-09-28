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
			print("Account created")


			
		elif choice is 2:
			print("this is view account block")
		elif choice is 3:
			print("credit block")
		elif choice is 4:
			print("debit block")
		elif choice is 5:
			print("TRANSACTION")
		elif choice is 6:
			print("delete account")
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
		ifsc = input("1.Motera 2.Science City 3.Shahibaug \n Choose your Branch :-")
		if ifsc =='1':
			branchName = 'Motera'
		if ifsc =='2':
			branchName = 'ScienceCity'
		if ifsc =='3':
			branchName = 'Shahibaug'

		gender = input("1.Male 2.Female \n Choose your Gender :-")
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








		

