from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import datetime

import utils

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///services.db"

db = SQLAlchemy(app)


# Step 1
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50))
    phone = db.Column(db.String(50), nullable=False)


class Offer(db.Model):
    __tablename__ = 'offer'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    order = relationship('Order')
    user = relationship('User')


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    description = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String(50))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    customer = relationship('User', foreign_keys=[customer_id])
    executor = relationship('User', foreign_keys=[executor_id])


# Step 3
@app.get("/users/")
def users():
    with app.app_context():
        with db.session.begin():
            users_q = db.session.query(User).all()
            result = utils.get_json_users(users_q)

    return result


@app.get("/users/<int:id_>")
def user_id(id_):
    try:
        with app.app_context():
            with db.session.begin():
                user_q = db.session.query(User).get(id_)
                result = utils.get_json_one_user(user_q)

        return result

    except AttributeError:
        return dict


# Step 4
@app.get("/orders/")
def orders():
    with app.app_context():
        with db.session.begin():
            orders_q = db.session.query(Order).all()
            result = utils.get_json_orders(orders_q)

    return result


@app.get("/orders/<int:id_>")
def order_id(id_):
    try:
        with app.app_context():
            with db.session.begin():
                order_q = db.session.query(Order).get(id_)
                result = utils.get_json_one_order(order_q)

        return result

    except AttributeError:
        return dict()


# Step 5
@app.get("/offers/")
def offers():
    with app.app_context():
        with db.session.begin():
            offers_q = db.session.query(Offer).all()
            result = utils.get_json_offers(offers_q)

    return result


@app.get("/offers/<int:id_>")
def offers_id(id_):
    try:
        with app.app_context():
            with db.session.begin():
                offers_q = db.session.query(Offer).get(id_)
                result = utils.get_json_one_offer(offers_q)

        return result
    except AttributeError:
        return dict()


# Step 6
@app.post('/users')
def add_user():
    user = request.json

    try:
        new_user = User(
            first_name=user['first_name'],
            last_name=user['last_name'],
            age=user['age'],
            email=user['email'],
            role=user['role'],
            phone=user['phone']
        )

        with app.app_context():
            db.session.add(new_user)
            db.session.commit()
            db.session.close()

        return 'Пользователь добавлен'

    except KeyError:
        return 'Неправильный json'


@app.put('/users/<int:id_>')
def change_user(id_):
    try:
        user_json = request.json
        with app.app_context():
            with db.session.begin():
                user = db.session.query(User).get(id_)
                user.first_name = user_json['first_name']
                user.last_name = user_json['last_name']
                user.age = user_json['age']
                user.email = user_json['email']
                user.role = user_json['role']
                user.phone = user_json['phone']
                db.session.add(user)

        return 'Пользователь обновлен'

    except AttributeError:
        return 'Неверный id'

    except KeyError:
        return 'Неверный json'


@app.delete('/users/<int:id_>')
def delete_user(id_):
    try:
        with app.app_context():
            with db.session.begin():
                user = db.session.query(User).get(id_)
                db.session.delete(user)

        return 'Пользователь удален'

    except:
        return 'Неверный id'


# Step 7
@app.post('/orders')
def add_order():
    order = request.json

    try:
        new_order = Order(
            name=order['name'],
            description=order['description'],
            start_date=datetime.datetime.strptime(order['start_date'], "%m/%d/%Y").date(),
            end_date=datetime.datetime.strptime(order['end_date'], "%m/%d/%Y").date(),
            address=order['address'],
            price=order['price'],
            customer_id=order['customer_id'],
            executor_id=order['executor_id']
        )

        with app.app_context():
            db.session.add(new_order)
            db.session.commit()
            db.session.close()

        return 'Заказ добавлен'

    except KeyError:
        return 'Неправильный json'


@app.put('/orders/<int:id_>')
def change_order(id_):
    try:
        order_json = request.json
        with app.app_context():
            with db.session.begin():
                order = db.session.query(Order).get(id_)
                order.name = order_json['name']
                order.description = order_json['description']
                order.start_date = datetime.datetime.strptime(order_json['start_date'], "%m/%d/%Y").date()
                order.end_date = datetime.datetime.strptime(order_json['end_date'], "%m/%d/%Y").date()
                order.address = order_json['address']
                order.price = order_json['price']
                order.customer_id = order_json['customer_id']
                order.executor_id = order_json['executor_id']
                db.session.add(order)

        return 'Заказ обновлен'

    except AttributeError:
        return 'Неверный id'

    except KeyError:
        return 'Неверный json'


@app.delete('/orders/<int:id_>')
def del_order(id_):
    try:
        with app.app_context():
            with db.session.begin():
                user = db.session.query(Order).get(id_)
                db.session.delete(user)

        return 'Заказ удален'

    except:
        return 'Неверный id'


# Step 8
@app.post('/offers')
def add_offer():
    offer = request.json

    try:
        new_offer = Offer(
            order_id=offer['order_id'],
            executor_id=offer['executor_id']
        )

        with app.app_context():
            db.session.add(new_offer)
            db.session.commit()
            db.session.close()

        return 'Оффер добавлен'

    except KeyError:
        return 'Неправильный json'


@app.put('/offers/<int:id_>')
def change_offer(id_):
    try:
        offer_json = request.json
        with app.app_context():
            with db.session.begin():
                offer = db.session.query(Offer).get(id_)
                offer.order_id = offer_json['order_id']
                offer.executor_id = offer_json['executor_id']

                db.session.add(offer)

        return 'Оффер обновлен'

    except AttributeError:
        return 'Неверный id'

    except KeyError:
        return 'Неверный json'


@app.delete('/offers/<int:id_>')
def del_offer(id_):
    try:
        with app.app_context():
            with db.session.begin():
                offer = db.session.query(Offer).get(id_)
                db.session.delete(offer)

        return 'Заказ удален'

    except:
        return 'Неверный id'


if __name__ == '__main__':
    app.run(debug=True)
