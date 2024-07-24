from flask import Blueprint, request, jsonify
from .models import User, Trip

main = Blueprint('main', __name__)


@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(**data)
    user.save()
    return jsonify(user.to_json()), 201


@main.route('/users/<userId>', methods=['GET'])
def get_user(userId):
    user = User.objects(userId=userId).first()
    if user:
        return jsonify(user.to_json()), 200
    return jsonify({"error": "User not found"}), 404


@main.route('/users/<userId>', methods=['PUT'])
def update_user(userId):
    data = request.get_json()
    user = User.objects(userId=userId).first()
    if user:
        user.update(**data)
        return jsonify(user.to_json()), 200
    return jsonify({"error": "User not found"}), 404


@main.route('/users/<userId>', methods=['DELETE'])
def delete_user(userId):
    user = User.objects(userId=userId).first()
    if user:
        user.delete()
        return jsonify({"success": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

# Similar routes for trips
