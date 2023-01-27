import json
from main import *
import datetime

PATH_USERS = './data/Users.json'
PATH_OFFERS = './data/Offers.json'
PATH_ORDERS = './data/Orders.json'


def load_data(path):
    with open(path, encoding='utf-8') as file:
        result = json.load(file)

    return result


def add_users_data():
    users_json = load_data(PATH_USERS)
    users_db = []

    for user in users_json:
        new_user = User(
            id=user['id'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            age=user['age'],
            email=user['email'],
            role=user['role'],
            phone=user['phone']
        )
        users_db.append(new_user)

    with app.app_context():
        db.session.add_all(users_db)
        db.session.commit()
        db.session.close()


def add_offers_data():
    offers_json = load_data(PATH_OFFERS)
    offers_db = []

    for offer in offers_json:
        new_offer = Offer(
            id=offer['id'],
            order_id=offer['order_id'],
            executor_id=offer['executor_id']
        )
        offers_db.append(new_offer)

    with app.app_context():
        db.session.add_all(offers_db)
        db.session.commit()
        db.session.close()


def add_orders_data():
    orders_json = load_data(PATH_ORDERS)
    orders_db = []

    for order in orders_json:
        start_date_ = order['start_date'].split('/')
        end_date_ = order['end_date'].split('/')

        new_order = Order(
            id=order['id'],
            name=order['name'],
            description=order['description'],
            start_date=datetime.date(int(start_date_[2]), int(start_date_[0]), int(start_date_[1])),
            end_date=datetime.date(int(end_date_[2]), int(end_date_[0]), int(end_date_[1])),
            address=order['address'],
            price=order['price'],
            customer_id=order['customer_id'],
            executor_id=order['executor_id']
        )
        orders_db.append(new_order)

    with app.app_context():
        db.session.add_all(orders_db)
        db.session.commit()
        db.session.close()


add_offers_data()
