import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    products = []
    with open('products.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        elif source == 'sql':
            data = read_sql()
        else:
            return render_template('product_display.html', error='Wrong source')
    except (sqlite3.Error, OSError, ValueError, KeyError):
        return render_template('product_display.html', error='Error reading data')

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error='Product not found')
        data = [p for p in data if p['id'] == product_id]
        if not data:
            return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
