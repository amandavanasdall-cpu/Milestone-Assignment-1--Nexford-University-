class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.active = True  

    # Create a new product
    def create_product(self):
        print(f"{self.name} has been created.")

    # Update product details
    def update_product(self, new_name, new_price):
        self.name = new_name
        self.price = new_price
        print(f"Product has been updated to {self.name}.")

    # Suspend product
    def suspend_product(self):
        self.active = False
        print(f"{self.name} has been suspended.")   

    # Remove Product
    def remove_product(self):
        print(f"{self.name} has been removed from the catalog.")    