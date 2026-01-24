from flask import Blueprint, jsonify, request
import src.controllers.user_controller as controller
from src.middleware import password_helper, token_helper
from backend import http_code

import os

user_list = [{"name":"Avi", "email":"avi.mail.com"},{"name":"David", "email":"david.mail.com"},{"name":"Avi", "email":"avi.mail.com"}]

users_bp = Blueprint("users_bp", __name__, url_prefix="/api/users")

@users_bp.route("/register", ["POST"])
def user_register():
    try:
        secret_key_user = os.getenv("USER_CODE")
        secret_key_admin = os.getenv("ADMIN_CODE")
        user_dict = request.get_json()
        role_code = user_dict.get("role_password")
        password_res = user_dict.get("password")
        password_res = user_dict.get("password")
        if password_res:
            user_dict['password'] = password_helper.hash_password(password_res)
        else:
            raise ValueError("Password is missing")
        user_dict['password'] = password_helper.hash_password(password_res)

        user = controller.user_from_dict(user_dict)
        if user.role == 'regular' and role_code == secret_key_admin:
            return({"error": "קוד משתמש לא תקין"})
        if user.role == 'admin' and role_code == secret_key_user:
           return({"error": "קוד משתמש לא תקין"})
        
        add_user = controller.add_user(user)
        if add_user:
            return jsonify(controller.user_to_dict(user)), http_code.HTTP_CODE_CREATED

    except ValueError as e:
        return jsonify({"error": str(e)}), http_code.HTTP_CODE_SERVER_ERROR
    
    except Exception as e:
        return jsonify({"error": "Internal server error"}), http_code.HTTP_CODE_SERVER_ERROR  
    

@users_bp.route("/login", ["POST"])
def user_login():
    try:
        email = request.json.get("email")
        password = request.json.get("password")
        if password:
            password_res = password_helper.hash_password(password_res)
        else:
            raise ValueError("Password is missing")
        verify_password = password_helper.verify_password(plain_password=password, hashed_password=password_res)
        res = controller.user_login(email_login=email, password_login=password_res)

        if res and verify_password:
            token = token_helper(res)
            # return jsonify({"user":controller.user_to_dict(res), "token": token }), http_code.HTTP_CODE_CREATED
            return jsonify(controller.user_to_dict(res), token ), http_code.HTTP_CODE_CREATED

    except ValueError as e:
        return jsonify({"error": str(e)}), http_code.HTTP_CODE_INVALID_DATA
    
    except Exception as e:
        return jsonify({"error": "Internal server error"}), http_code.HTTP_CODE_SERVER_ERROR  



#/api/users