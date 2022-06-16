from db import Database
import cv


def main():
	database = Database()
	while True:
		choice = input(cv.MENU)
		if choice == '1':
			admin = input(cv.ADMIN_PASS)
			database.print_all(admin)
						
		elif choice == '2':
			admin = input(cv.ADMIN_PASS)
			database.get_number_of_users(admin)
		elif choice == '3':
			admin = input(cv.ADMIN_PASS)
			database.get_total_amount_of_credits(admin)
		elif choice == '4':
			username = input(cv.GET_USERNAME)
			password = input(cv.GET_PASSWORD)
			database.show_credit_of_user(username, password)
		elif choice == '5':
			username = input(cv.NEW_USERNAME)
			password = input(cv.GET_PASSWORD)
			database.add_user(username, password)
		elif choice == '6':
			username = input(cv.GET_USERNAME)
			password = input(cv.GET_PASSWORD)
			money = int(input(cv.AMOUNT))
			database.add_credit_to_user(money, username, password)
		elif choice == '7':
			money = int(input(cv.AMOUNT_SEND))
			username1 = input(cv.GET_USERNAME)
			password1 = input(cv.GET_PASSWORD)
			username2 = input(cv.TO_USERNAME)
			database.send_credit_from_user_to_user(money, username1, password1, username2)
		elif choice == '8':
			print('Thanks for using my program')
			break


if __name__ == '__main__':
	main()