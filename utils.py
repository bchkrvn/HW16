from app import User, Order, Offer


def get_json_one_user(user: User) -> dict:
    """
    Превращает объект User в json
    :param user: User
    :return: dict
    """
    user_json = {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "age": user.age,
        "email": user.email,
        "role": user.role,
        "phone": user.phone
    }

    return user_json


def get_json_users(users: list[User]) -> list:
    """
    Превращает список объектов User в обычный список
    :param users: list[User]
    :return: list[dict]
    """
    users_json = [{
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "age": user.age,
        "email": user.email,
        "role": user.role,
        "phone": user.phone
    } for user in users]

    return users_json


def get_json_one_order(order: Order) -> dict:
    """
    Превращает объект Order в dict
    :param order: Order
    :return: dict
    """
    order_json = {
        "id": order.id,
        "name": order.name,
        "description": order.description,
        "start_date": order.start_date,
        "end_date": order.end_date,
        "address": order.address,
        "price": order.price,
        "customer_id": order.customer_id,
        "executor_id": order.executor_id
    }

    return order_json


def get_json_orders(orders: list[Order]) -> list:
    """
    Превращает несколько объектов Order в обычный лист
    :param orders: list[Order]
    :return: list[dict]
    """
    orders_json = [{
        "id": order.id,
        "name": order.name,
        "description": order.description,
        "start_date": order.start_date,
        "end_date": order.end_date,
        "address": order.address,
        "price": order.price,
        "customer_id": order.customer_id,
        "executor_id": order.executor_id
    } for order in orders]

    return orders_json


def get_json_one_offer(offer: Offer) -> dict:
    """
    Превращает объект Offer в dict
    :param offer: Offer
    :return: dict
    """
    offer_json = {
        "id": offer.id,
        "order_id": offer.order_id,
        "executor_id": offer.executor_id
    }

    return offer_json


def get_json_offers(offers: list[Offer]) -> list:
    """
    Превращает список объектов Offer в обычный список
    :param offers: list[Offer]
    :return: list[dict]
    """
    offers_json = [{
        "id": offer.id,
        "order_id": offer.order_id,
        "executor_id": offer.executor_id
    } for offer in offers]

    return offers_json
