
cappuccino = 5.00
sandwich = 7.00
iced_tea = 3.00

customer_name = input("Enter customer name: ")
menu_item = input("Enter menu item: ")
quantity_ordered = int(input("Enter quantity ordered: "))

if menu_item == "cappuccino":
    price = cappuccino
elif menu_item == "sandwich":
    price = sandwich
elif menu_item == "iced tea":
    price = iced_tea
else:
    print(f"Sorry, we don't have {menu_item} on the menu.")
    exit()

total_cost = price * quantity_ordered

print(f"Customer {customer_name} is buying {quantity_ordered} {menu_item}. Total cost: ${total_cost:.2f}")
