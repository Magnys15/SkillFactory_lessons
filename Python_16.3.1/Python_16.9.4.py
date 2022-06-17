from Python_Rec import Customer, CustomerNew

guest_list = []
num_of_customers = int(input("Введите кол-во новых посетителей: "))

for i in range(num_of_customers):
    # nc = Customer.add_new_customer()
    guest_list.append(Customer.add_new_customer())

print(guest_list)


num_of_customers = int(input("Введите кол-во новых посетителей: "))
for i in range(num_of_customers):
    guest_list.append(CustomerNew.add_new_customer())


print(guest_list)
for i in range(len(guest_list)):
    print(guest_list[i].__str__())

