from Python_Rec import Customer

customers = []


def new_customers():
    number_of_customers = int(input("Введите число новых посетителей: "))
    for i in range(number_of_customers):
        nc = Customer(input("Введите имя клиента: "),
                      input("Введите имя клиента: "))
        customers.append(nc)


def show_customers():
    for customer in customers:
        print(f'Клиент: {customer.name}. Баланс: {customer.balance}')


new_customers()
show_customers()
