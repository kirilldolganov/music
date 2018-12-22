from app import app
from models import Genre
from models import Label
from models import Record
from models import Stock
from flask import jsonify
from flask import request
from app import db
import json

#api's for genre
@app.route('/api/genre', methods=['GET'])
def api_genre_get():
    genres = Genre.query.all()
    genres_json = [{"id": genre.id, "name": genre.name}
                  for genre in genres]
    return jsonify(genres_json)

@app.route('/api/genre/<id>', methods=['GET'])
def api_genre_get_id(id):
    genres = Genre.query.filter_by(id=id)
    if not genres:
        abort(404)
    genre = genres[0]
    genre_json = {"id": genre.id, "name": genre.name}
    return jsonify(genre_json)

@app.route('/api/genre', methods=['POST'])
def api_genre_insert():
    new_genre = request.get_json()
    genre = Genre(id=new_genre['id'], name=new_genre['name'])
    db.session.add(genre)
    db.session.commit()
    genre_json = {"id": genre.id, "name": genre.name}
    return jsonify(genre_json)

@app.route('/api/genre/<id>', methods=['DELETE'])
def api_genre_delete(id):
    genres = Genre.query.filter_by(id=id)
    if not genres:
        abort(404)
    genre = genres[0]
    db.session.delete(genre)
    db.session.commit()
    return jsonify()

@app.route('/api/genre/<id>', methods=['PUT'])
def api_genre_update(id):
    updated_genre = request.get_json()
    genres_to_update = Genre.query.filter_by(id=id)
    data = json.loads(request.get_data())
    genre_to_update = genres_to_update[0]
    genre_to_update = db.session.query(Genre).filter_by(id = id).first()
    genre_to_update.name = data['name']
    db.session.commit()
    return jsonify(genre_to_update.to_dict())

#api's for label
@app.route('/api/label', methods=['GET'])
def api_label_get():
    labels = Label.query.all()
    labels_json = [{"id": label.id, "name": label.name}
                  for label in labels]
    return jsonify(labels_json)

@app.route('/api/label/<id>', methods=['GET'])
def api_label_get_id(id):
    labels = Label.query.filter_by(id=id)
    if not labels:
        abort(404)
    label = labels[0]
    label_json = {"id": label.id, "name": label.name}
    return jsonify(label_json)

@app.route('/api/label', methods=['POST'])
def api_label_insert():
    new_label = request.get_json()
    label = Label(id=new_label['id'], name=new_label['name'])
    db.session.add(label)
    db.session.commit()
    label_json = {"id": label.id, "name": label.name}
    return jsonify(label_json)

@app.route('/api/label/<id>', methods=['DELETE'])
def api_label_delete(id):
    labels = Label.query.filter_by(id=id)
    if not labels:
        abort(404)
    label = labels[0]
    db.session.delete(label)
    db.session.commit()
    return jsonify()

@app.route('/api/label/<id>', methods=['PUT'])
def api_label_update(id):
    updated_label = request.get_json()
    labels_to_update = Label.query.filter_by(id=id)
    data = json.loads(request.get_data())
    label_to_update = labels_to_update[0]
    label_to_update = db.session.query(Label).filter_by(id = id).first()
    label_to_update.name = data['name']
    db.session.commit()
    return jsonify(label_to_update.to_dict())

#api's for record
@app.route('/api/record', methods=['GET'])
def api_record_get():
    records = Record.query.all()
    records_json = [{"id": record.id, "name": record.name, "label": record.label, "genre": record.label, "price": record.price}
                  for record in records]
    return jsonify(records_json)

@app.route('/api/record/<id>', methods=['GET'])
def api_record_get_id(id):
    records = Record.query.filter_by(id=id)
    if not records:
        abort(404)
    record = records[0]
    records_json = {"id": record.id, "name": record.name, "label": record.label, "genre": record.label, "price": record.price}
    return jsonify(records_json)

@app.route('/api/record', methods=['POST'])
def api_record_insert():
    new_record = request.get_json()
    record = Record(id=new_record['id'], name=new_record['name'], label=new_record['label'], genre=new_record['genre'], price=new_record['price'])
    db.session.add(record)
    db.session.commit()
    record_json = {"id": record.id, "name": record.name, "label": record.label, "genre": record.label, "price": record.price}
    return jsonify(record_json)

@app.route('/api/record/<id>', methods=['DELETE'])
def api_record_delete(id):
    records = Record.query.filter_by(id=id)
    if not records:
        abort(404)
    record = records[0]
    db.session.delete(record)
    db.session.commit()
    return jsonify()

@app.route('/api/record/<id>', methods=['PUT'])
def api_record_update(id):
    updated_record = request.get_json()
    records_to_update = Record.query.filter_by(id=id)
    data = json.loads(request.get_data())
    record_to_update = records_to_update[0]
    record_to_update = db.session.query(Record).filter_by(id = id).first()
    record_to_update.name = data['name']
    record_to_update.label = data['label']
    record_to_update.genre = data['genre']
    record_to_update.price = data['price']
    db.session.commit()
    return jsonify(record_to_update.to_dict())

#api's for stock
@app.route('/api/stock', methods=['GET'])
def api_stock_get():
    stocks = Stock.query.all()
    stocks_json = [{"id": stock.id, "amount": stock.amount}
                  for stock in stocks]
    return jsonify(stocks_json)

@app.route('/api/stock/<id>', methods=['GET'])
def api_stock_get_id(id):
    stocks = Stock.query.filter_by(id=id)
    if not stocks:
        abort(404)
    stock = stocks[0]
    stock_json = {"id": stock.id, "amount": stock.amount}
    return jsonify(stock_json)

@app.route('/api/stock', methods=['POST'])
def api_stock_insert():
    new_stock = request.get_json()
    stock = Stock(id=new_stock['id'], amount=new_stock['amount'])
    db.session.add(stock)
    db.session.commit()
    stock_json = {"id": stock.id, "amount": stock.amount}
    return jsonify(stock_json)

@app.route('/api/stock/<id>', methods=['DELETE'])
def api_stock_delete(id):
    stocks = Stock.query.filter_by(id=id)
    if not stocks:
        abort(404)
    stock = stocks[0]
    db.session.delete(stock)
    db.session.commit()
    return jsonify()

@app.route('/api/stock/<id>', methods=['PUT'])
def api_stock_update(id):
    updated_stock = request.get_json()
    stocks_to_update = Stock.query.filter_by(id=id)
    data = json.loads(request.get_data())
    stock_to_update = stocks_to_update[0]
    stock_to_update = db.session.query(Stock).filter_by(id = id).first()
    stock_to_update.amount = data['amount']
    db.session.commit()
    return jsonify(stock_to_update.to_dict())