import pyshorteners as shorten
import time

print("\n----------------------------------------------------------------------------")
print("                   Welcome to ZumTheZazaKing's URL Shortener!                 ")




def main():

	print("----------------------------------------------------------------------------")

	time.sleep(2)

	url = input("Enter the url you would like to shorten:\n")

	x = shorten.Shortener().tinyurl.short(url)

	print("----------------------------------------------------------------------------")

	time.sleep(1)

	print("Processing...")

	print("----------------------------------------------------------------------------")

	time.sleep(2)

	print("Here is your shortened url: ", x)

	print("----------------------------------------------------------------------------")


while True:

	main()
	time.sleep(2)
	if str(input("""Would you like to repeat the program?
(Type Y(Yes) or N(No)):
""")).strip().upper() != "Y":
	  print("\nGoodbye!\n")
	  time.sleep(1)
	  break