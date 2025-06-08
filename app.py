from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    price = db.Column(db.Float)
    description = db.Column(db.String(200))
    image_url = db.Column(db.String(200))

@app.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'category': p.category,
        'price': p.price,
        'description': p.description,
        'image_url': p.image_url
    } for p in products])

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('query', '').lower()
    matching = Product.query.filter(Product.name.ilike(f'%{query}%')).all()
    if not matching:
        return jsonify({'message': 'No products found.', 'products': []})
    return jsonify({
        'message': f"Found {len(matching)} products.",
        'products': [{
            'id': p.id,
            'name': p.name,
            'category': p.category,
            'price': p.price,
            'description': p.description,
            'image_url': p.image_url
        } for p in matching]
    })

if __name__ == '__main__':
    app.run(debug=True)
