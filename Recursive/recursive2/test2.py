#Recursive Exercise 2
houses = ["Nadech's House", "Yaya's House", "Aj.Nest's House", "Mario's House"]
def deliver_products_recursively(houses):
    #Worker doin his work -> Base case == 1
    if len(houses) == 1:
        house = houses[0]
        print("Delivering products to=")