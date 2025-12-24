import os
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

products = [
    {
        "id": "prod_001",
        "name": "QuantumCore X1 Laptop",
        "price": 1299.99,
        "description": "Next-gen computing with quantum-inspired processing. 32GB RAM, 2TB SSD, 17\" OLED display.",
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
        "category": "COMPUTERS",
        "rating": 4.8
    },
    {
        "id": "prod_002",
        "name": "NeuraSync Pro Headphones",
        "price": 349.99,
        "description": "AI-powered noise cancellation with neural audio processing. 40hr battery life.",
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
        "category": "AUDIO",
        "rating": 4.9
    },
    {
        "id": "prod_003",
        "name": "AeroDrone X200",
        "price": 899.99,
        "description": "4K cinematic drone with obstacle avoidance and 5km range. Includes 3 batteries.",
        "image": "https://images.unsplash.com/photo-1473968512647-3e447244af8f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
        "category": "DRONES",
        "rating": 4.6
    },
    {
        "id": "prod_004",
        "name": "SmartVision AR Glasses",
        "price": 599.99,
        "description": "Augmented reality glasses with holographic display and voice control.",
        "image": "https://images.unsplash.com/photo-1713869807794-961c3429ad59?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
        "category": "WEARABLES",
        "rating": 4.7
    },
    {
        "id": "prod_005",
        "name": "PowerBeam Wireless Charger",
        "price": 79.99,
        "description": "Multi-device wireless charging station with 15W fast charging for each port.",
        "image": "https://images.unsplash.com/photo-1591290619618-904f6dd935e3?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
        "category": "ACCESSORIES",
        "rating": 4.5
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/check-shipping', methods=['POST'])
def check_shipping():
    product_id = request.form.get('product_id', '')
    zip_code = request.form.get('zip_code', '').strip()

    selected_product = None
    for prod in products:
        if prod['id'] == product_id:
            selected_product = prod
            break

    lower = zip_code.lower()
    forbidden_substrings = [
        "flag", "bash", "sh ", " sh", "python", "perl",
        "nc", "wget", "curl"
    ]
    forbidden_chars = ["`"]

    if len(zip_code) > 80:
        result = f"Standard shipping available for {zip_code}."
        return render_template(
            'index.html',
            products=products,
            shipping_result=result,
            selected_product=selected_product
        )

    if any(s in lower for s in forbidden_substrings):
        result = f"Standard shipping available for {zip_code}."
        return render_template(
            'index.html',
            products=products,
            shipping_result=result,
            selected_product=selected_product
        )

    if any(c in zip_code for c in forbidden_chars):
        result = f"Standard shipping available for {zip_code}."
        return render_template(
            'index.html',
            products=products,
            shipping_result=result,
            selected_product=selected_product
        )

    cmd = f"grep {zip_code} /etc/services"
    output = os.popen(cmd).read()

    if not output.strip():
        output = f"Standard shipping available for {zip_code}."

    return render_template(
        'index.html',
        products=products,
        shipping_result=output,
        selected_product=selected_product
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
