from backend.database import init_db, SessionLocal, Customer, Product, Order, OrderItem
import datetime

def seed_data():
    db = SessionLocal()
    
    # Check if data already exists
    if db.query(Customer).first():
        print("Database already seeded.")
        db.close()
        return

    print("Seeding database with professional dummy data...")
    
    # Customers
    customers = [
        Customer(name="John Doe", email="john@example.com", country="USA"),
        Customer(name="Jane Smith", email="jane@example.com", country="Canada"),
        Customer(name="Alice Johnson", email="alice@example.com", country="UK"),
        Customer(name="Bob Brown", email="bob@example.com", country="Germany"),
        Customer(name="Charlie Davis", email="charlie@example.com", country="France")
    ]
    db.add_all(customers)
    db.commit()

    # Products
    products = [
        Product(name="iPhone 15 Pro", category="Electronics", price=1199.99, stock=45),
        Product(name="MacBook Air M3", category="Electronics", price=1299.00, stock=30),
        Product(name="Sony WH-1000XM5", category="Accessories", price=399.99, stock=85),
        Product(name="Dell UltraSharp 27", category="Electronics", price=599.00, stock=20),
        Product(name="Logitech MX Master 3S", category="Accessories", price=99.00, stock=110),
        Product(name="Keychron Q6 Pro", category="Accessories", price=199.00, stock=55),
        Product(name="iPad Pro 12.9", category="Electronics", price=1099.00, stock=25),
        Product(name="Samsung S23 Ultra", category="Electronics", price=1199.00, stock=40)
    ]
    db.add_all(products)
    db.commit()

    # Orders
    orders = [
        Order(customer_id=1, total=1199.49, date=datetime.datetime(2023, 10, 1)),
        Order(customer_id=2, total=1499.00, date=datetime.datetime(2023, 10, 5)),
        Order(customer_id=1, total=199.50, date=datetime.datetime(2023, 10, 10)),
        Order(customer_id=3, total=450.00, date=datetime.datetime(2023, 10, 12))
    ]
    db.add_all(orders)
    db.commit()

    # Order Items
    items = [
        OrderItem(order_id=1, product_id=1, quantity=1),
        OrderItem(order_id=1, product_id=3, quantity=1),
        OrderItem(order_id=2, product_id=2, quantity=1),
        OrderItem(order_id=3, product_id=3, quantity=1),
        OrderItem(order_id=4, product_id=4, quantity=1)
    ]
    db.add_all(items)
    db.commit()
    
    db.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    init_db()
    seed_data()
