from app import db, Product
import csv

db.create_all()

with open('products.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        p = Product(
            name=row['name'],
            category=row['category'],
            price=float(row['price']),
            description=row['description'],
            image_url=row['image_url']
        )
        db.session.add(p)

db.session.commit()
print("Database seeded!")
