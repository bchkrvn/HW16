import json
from app import *
import datetime

PATH_USERS = './data/Users.json'
PATH_OFFERS = './data/Offers.json'
PATH_ORDERS = './data/Orders.json'


# Step 2
# Этот файл был предназначен для передачи данных из json в БД


def load_data(path) -> list[dict]:
    """
    Загружает данные из json по пути path
    :param path: путь
    :return: list[dict]
    """
    with open(path, encoding='utf-8') as file:
        result = json.load(file)

    return result


def add_users_data():
    """
    Загружает из json в БД пользователей
    """
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
    """
        Загружает из json в БД офферы
    """
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
    """
        Загружает из json в БД заказы
    """
    orders_json = load_data(PATH_ORDERS)
    orders_db = []

    for order in orders_json:
        new_order = Order(
            id=order['id'],
            name=order['name'],
            description=order['description'],
            start_date=datetime.datetime.strptime(order['start_date'], "%m/%d/%Y").date(),
            end_date=datetime.datetime.strptime(order['end_date'], "%m/%d/%Y").date(),
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
