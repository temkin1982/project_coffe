from flask import Blueprint, jsonify, request

user_list = [{"name":"Avi", "email":"avi.mail.com"},{"name":"David", "email":"david.mail.com"},{"name":"Avi", "email":"avi.mail.com"}]

users_bp = Blueprint("users_bp", __name__, url_prefix="/api/users")

@users_bp.route("/", ["GET"])
def get_users():
    return jsonify(user_list)


#/api/users