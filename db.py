class User:
	def __init__(self, username, password, credit=0):
		self.username = username
		self.password = password
		self.credit = int(credit)

	def __str__(self):
		return "{} {} {}".format(self.username, self.password, self.credit)

	def __repr__(self):
		return str(self)


class Database:
	def __init__(self):
		self.users = self.read()
		self.admin_password = "1234"

	def save(self):
		new_list = [str(user) for user in self.users]
		text = '\n'.join(new_list)
		with open("accounts.ck","w+") as f:
			f.write(text)

	def read(self):
		with open("accounts.ck","r") as f:
			text = f.read()
		lines = text.splitlines()
		return list([User(*line.split()) for line in lines])

	def find_user(self, username):
		for user in self.users:
			if user.username == username:
				return username
		return None

	def print_all(self, password):
		# check for admin password
		if self.admin_password==password:
			print('user name|password|credit')
			print('--------------------------')
			for user in self.users:
				print('{} | {} | {}'.format(user.username,user.password,user.credit))
			pass
		else:
			print('wrong password')
		

	def get_number_of_users(self, password):
		# check for admin password
		if self.admin_password==password:
			counter=0
			for user in self.users:
				counter+=1

			print('There are {} user in the system '.format(counter))
			pass
		else:
			print('wrong password')
		

	def get_total_amount_of_credits(self, password):
		# 1. check for admin password
		if self.admin_password==password:
			
			# 2. define sum = 0
			sum=0
			# 3. loop on all of self.users
			for i in self.read():
				sum+=i.credit
			print('The total sum of all user credit is : {} $noSeke'.format(sum))
		
		pass

	def user_exists(self, username):
		for user in self.users:
			
			if (user.username==username):
				print('user found! in database')
				return True
				
		else:
				
			print('user NOT found! in database')
			return False
             
	def username_matches_password(self, username, password):
		for user in self.users:
			# find the user with that username
			if user.username==username and user.password==password:
				print('password is matched in database')
				return True
						
		else : 
				print('password is not matched in database')
				return False
			
			

	def show_credit_of_user(self, username, password):
		# 1. check user exists
		if self.user_exists(username) and self.username_matches_password(username,password):
			for user in self.users:
				if user.username==username and user.password==password:
					
					print('The credit of this user is {} $noSeke'.format(user.credit))
		# 3. find the user and show credit
				
		
		
	def add_user(self, username, password):
		# 1. check user does not exist
		if (self.user_exists(username)):
		   print('User is already in a system!')
		else:
			print('user is not in the system adding new user')

		# 2. create a new User(username, password)
			new_user= User(username,password)
			
		# 3. append the new user to self.users
			self.users.append(new_user)
		# 4. don't forget to save() !
			self.save()
		

	def add_credit_to_user(self, money, username, password):
		# 1. check user does not exist
		# 2. create a new User(username, password)
		self.user_exists(username)
		
		# 3. search for the user
		for user in self.users:
			if user.username==username and user.password==password:
				user.credit+=money
				print(' your new credit balance is {} $noSeke'.format(user.credit))
			# 4. add money to user.credit
		# 5. print new credit
		self.save()
		# 6. don't forget to save() !
		pass

	def send_credit_from_user_to_user(self, money, username1, password1, username2):
		# 1. check user1 exists # 2. check user2 exists
		
		if self.user_exists(username1) and self.user_exists(username2) and self.username_matches_password(username1,password1):
			print('all the information is correct! checking available fund!')
			
			for user1 in self.users:
				if user1.username==username1:
					if user1.credit>=money:
						for user2 in self.users:
							if user2.username==username2:
								user1.credit-=money
								user2.credit+=money
								self.save()
								print('The new credit of {} is : '.format(user1.username))
								self.show_credit_of_user(username1,password1)
								
								print('Transfer is completed')
					else:
						 print('insufficient fund')
						 print('Transfer is INCOMPLETED please try again')

			
					 
				    		

				
