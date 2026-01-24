from flask import Blueprint, jsonify, request
import src.controllers.coffee_controller as controller
from src.middleware import token_helper
from backend import http_code

import os

coffee_bp = Blueprint("coffee_bp", __name__, url_prefix="api/coffee")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
IMAGES = os.path.join(BASE_DIR, 'images')

@coffee_bp.before_request
def protect():
    error = token_helper()
    if error:
        return error
    

@coffee_bp.route("/", methods=["POST"])
def add_coffee():
    try:
        # Получаем JSON (если multipart/form-data — используем form)
        coffee_dict = request.form.to_dict()

        if not coffee_dict:
            return jsonify({"error": "Invalid or empty JSON"}), http_code.HTTP_CODE_BAD_REQUEST

        # Получаем картинку
        image = request.files.get('image')
        if not image or not image.filename.strip():
            return jsonify({"error": "No image uploaded"}), http_code.HTTP_CODE_INVALID_DATA

        # Обработка файла
        # Приводим имя файла к безопасному формату (убираем опасные символы и пути)
        filename = secure_filename(image.filename)

        # rsplit(".", 1) — разделяет строку справа по последней точке.
        # '1' означает: сделать только одно разделение, чтобы получить расширение файла.
        # [-1] берёт последний элемент списка — само расширение (например: "png").
        ext = filename.rsplit(".", 1)[-1].lower()

        ALLOWED_EXT = {"jpg", "jpeg", "png", "webp"}
        if ext not in ALLOWED_EXT:
            return jsonify({"error": "Unsupported image format"}), http_code.HTTP_CODE_BAD_REQUEST

        image_filename = f"{uuid.uuid4().hex}.{ext}"
        os.makedirs(IMAGES, exist_ok=True)
        image_path = os.path.join(IMAGES, image_filename)

        try:
            image.save(image_path)
        except Exception:
            return jsonify({"error": "Не удалось сохранить изображение"}), http_code.HTTP_CODE_SERVER_ERROR

        # Добавляем имя файла в объект
        coffee_dict["image"] = image_filename

        # Создаём объект кофе
        coffee = controller.coffee_from_dict(coffee_dict)

        created_coffee = controller.add_coffee(coffee)
        if not created_coffee:
            return jsonify({"error": "Failed to create coffee"}), http_code.HTTP_CODE_SERVER_ERROR

        return jsonify(controller.coffee_to_dict(created_coffee)), http_code.HTTP_CODE_CREATED

    except ValueError as e:
        return jsonify({"error": str(e)}), http_code.HTTP_CODE_BAD_REQUEST

    except Exception:
        return jsonify({"error": "Internal server error"}), http_code.HTTP_CODE_SERVER_ERROR