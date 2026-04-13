menu = {
    "Atomic Habits" : 1000,
    "The Alchemist":2000,
    "Rich Dad Poor Dad": 4000,
    "Think Like a Monk" :5000,
    "The Power of Now" : 8000,      
    "To Kill a Mockingbird" : 9000,
    "The Psychology of Money" :1050,
    "The Hobbit" :2020,
    "contact" : 9423664445
}

print("Welcome to May Bookstore! How can I help you?")
print("Available Books and Prices:")

price=0
book = input("Enter the name of the book you want to order: ")
if book in menu:
    price = menu[book]
    print(f"Your order is '{book}' \nThe price is: {price} INR")

else:
    print("Sorry, the book you ordered is not available in our libry.")


additional_order = input("Do you want to order another book? (yes/no): ")
book_2 =input("enter your second order book")

if book_2 in menu:
    price +=menu[book_2]
    print(f"you successfully placed the order {book_2}and price is{price}")
    
