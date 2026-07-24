from product import Product
from product_manager import ProductManager

def main():
    pm = ProductManager()

    pm.add_product(Product("Laptop", 1200, 5))
    pm.add_product(Product("Mouse", 25, 20))
    pm.add_product(Product("Keyboard", 45, 10))

    pm.show_products()
    print("Total inventory value:", pm.total_value())

if __name__ == "__main__":
    main()