products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    reverse = True if sort_order == 'desc' else False
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=reverse)
    return sorted_products


def display_products(products_list):
    for i, (product_name, price) in enumerate(products_list, 1):
        print(f"{i}. {product_name} - ${price}")

def display_categories():
    for i, category in enumerate(products.keys(), 1):
        print(f"{i}. {category}")
    while True:
        category_choice_input = input("Please enter the category number to select the category:")
        if category_choice_input.isdigit():
            category_choice = int(category_choice_input)
            if 1 <= category_choice <= len(products):
                return category_choice - 1  # 返回用户选择的类别索引
            else:
                print("Invalid category number.")
                return None  # 对于无效类别返回 None
        else:
            print("Invalid input. Please enter a number.")
            return None  # 对于非数字输入返回 None

def add_to_cart(cart, product, quantity):
    product_name, price = product
    # 检查是否购物车已有该商品，如果有则增加数量
    for i, item in enumerate(cart):
        if item[0] == product_name:
            cart[i] = (product_name, price, item[2] + quantity)
            return
    # 没有找到该商品，则添加新商品
    cart.append((product_name, price, quantity))

def display_cart(cart):
    print("\nYour shopping cart contains the following items:")
    total_cost = 0
    for i, item in enumerate(cart, 1):
        product_name, price, quantity = item
        subtotal = price * quantity
        total_cost += subtotal
        print(f"{product_name} - ${price} x {quantity} = ${subtotal}")
    print(f"Total cost: ${total_cost}")

def generate_receipt(name, email, cart, total_cost, address):
    print("\nReceipt")
    print("-------")
    print(f"Name: {name}")
    print(f"Mail: {email}")
    print("\nGoods purchased:")
    for item in cart:
        product_name, price, quantity = item
        subtotal = price * quantity
        print(f"{product_name} - ${price} x {quantity} = ${subtotal}")
    print(f"\nTotal: ${total_cost}")
    print(f"Address: {address}")
    print("\nYour goods will be delivered within 3 days. Payment will be collected upon successful delivery.")

def validate_name(name):
    parts = name.strip().split()
    if len(parts) < 2:
        return False
    for part in parts:
        if not part.isalpha():
            return False
    return True

def validate_email(email):
    return '@' in email

def main():
    cart = []
    total_cost = 0

    while True:
        name = input("Please enter your full name (first and last name): ")
        if validate_name(name):
            break
        else:
            print("Invalid name. Make sure you include first and last names, and only letters.")

    while True:
        email = input("Please enter your email address: ")
        if validate_email(email):
            break
        else:
            print("Invalid email address. Make sure to include the '@' symbol.")

    while True:
        print("\nAvailable product categories:")
        category_index = display_categories()  # 返回类别索引
        category_list = list(products.keys())
        selected_category = category_list[category_index]
        products_list = products[selected_category]
        while True:
            print(f"\nProducts in category '{selected_category}':")
            display_products(products_list)
            print("\nOptions:")
            print("1. Select products to buy")
            print("2. Sort items by price")
            print("3. Return to category selection")
            print("4. Finish shopping")
            option = input("Select an option: ")
            if option == '1':
                product_number_input = input("Please enter the product number you want to buy: ")
                if product_number_input.isdigit():
                    product_number = int(product_number_input)
                    if 1 <= product_number <= len(products_list):
                        selected_product = products_list[product_number - 1]
                        while True:
                            quantity_input = input("Please enter the purchase quantity: ")
                            if quantity_input.isdigit():
                                quantity = int(quantity_input)
                                add_to_cart(cart, selected_product, quantity)
                                print(f"{quantity} {selected_product[0]} have been added to the cart.")
                                break
                            else:
                                print("Invalid quantity. Please enter a number.")
                    else:
                        print("Invalid product number.")
                else:
                    print("Invalid input. Please enter a number.")
            elif option == '2':
                sort_order_input = input("Please select sort order: 'asc' for ascending or 'desc' for descending\nPlease enter options: ")
                if sort_order_input in ['asc', 'desc']:
                    sort_order = int(sort_order_input)
                    products_list = display_sorted_products(products_list, sort_order_input)
                    print("\nSorted products:")
                    display_products(products_list)
                else:
                    print("Invalid option.")
            elif option == '3':
                break
            elif option == '4':
                if cart:
                    display_cart(cart)
                    total_cost = sum(price * quantity for (product_name, price, quantity) in cart)
                    print(f"\nTotal: ${total_cost}")
                    address = input("Please enter your shipping address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our platform. We hope you can buy our products next time. Have a nice day!")
                return
            else:
                print("Invalid option.")

if __name__ == "__main__":
    main()