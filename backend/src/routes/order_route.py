from flask import Blueprint, jsonify, request
import src.controllers.order_controller as controller
from src.middleware import token_helper
from backend import http_code

order_bp = Blueprint("order_bp", __name__, url_prefix="api/orders")

@order_bp.before_request
def protect():
    error = token_helper()
    if error:
        return error
    

@order_bp.route("/", methods=["POST"])
def create_order():
    try:
        order_dict = request.get_json()

        if not order_dict:
            return jsonify({"error": "Invalid or empty JSON"}), http_code.HTTP_CODE_BAD_REQUEST

        order = controller.order_from_dict(order_dict)
        add_order = controller.add_order(order)

        return jsonify(controller.order_to_dict(add_order)), http_code.HTTP_CODE_CREATED

    except ValueError as e:
        return jsonify({"error": str(e)}), http_code.HTTP_CODE_BAD_REQUEST

    except Exception as e:
        return jsonify({"error": "Internal server error"}), http_code.HTTP_CODE_SERVER_ERROR      


@order_bp.route("/user/<user_id>", methods=["GET"])
def get_orders_by_user(user_id): 
    try:
        orders_by_user = controller.get_all_order_by_user(user_id)
        
        if not orders_by_user:
            return jsonify({"error": "אין הזמנות"}), http_code.HTTP_CODE_CREATED
        
        orders = [controller.order_to_dict(order) for order in orders_by_user]
        return jsonify(orders), http_code.HTTP_CODE_CREATED


    except Exception as e:
        return jsonify({"error": "Internal server error"}), http_code.HTTP_CODE_SERVER_ERROR        