from faker import Faker
from api.models import Customer, Product, Order, OrderItem
import random
from decimal import Decimal

fake = Faker()

def create_customers(num=50):
    for _ in range(num):
        Customer.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            phone=fake.phone_number(),
            address=fake.street_address(),
            city=fake.city(),
            state=fake.state(),
            zip_code=fake.zipcode()
        )

def create_products(num=30):
    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Toys']
    for _ in range(num):
        Product.objects.create(
            name=fake.catch_phrase(),
            description=fake.paragraph(),
            price=Decimal(random.uniform(5, 500)),
            sku=fake.unique.bothify('SKU-#####'),
            category=random.choice(categories),
            is_active=random.choice([True, False])
        )

def create_orders(num=100):
    customers = list(Customer.objects.all())
    products = list(Product.objects.all())
    
    for _ in range(num):
        customer = random.choice(customers)
        order = Order.objects.create(
            customer=customer,
            order_date=fake.date_time_this_year(),
            total_amount=Decimal('0.00'),
            status=random.choice(['pending', 'processing', 'shipped', 'delivered', 'cancelled']),
            payment_method=random.choice(['Credit Card', 'PayPal', 'Bank Transfer', 'Cash'])
        )
        
        # Add 1-5 products to the order
        order_items = random.sample(products, k=random.randint(1, 5))
        total_amount = Decimal('0.00')
        
        for product in order_items:
            quantity = random.randint(1, 5)
            unit_price = product.price
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                unit_price=unit_price
            )
            total_amount += unit_price * quantity
        
        order.total_amount = total_amount
        order.save()

def generate_all_data():
    print("Creating customers...")
    create_customers()
    
    print("Creating products...")
    create_products()
    
    print("Creating orders...")
    create_orders()
    
    print("Fake data generation complete!")