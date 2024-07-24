from flask import Blueprint, request, jsonify
from .models import User, Trip
from .utils import serialize_doc, json_response

main = Blueprint('main', __name__)

@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(**data)
    user.save()
    return json_response(serialize_doc(user.to_mongo().to_dict())), 201

@main.route('/users/<userId>', methods=['GET'])
def get_user(userId):
    user = User.objects(userId=userId).first()
    if user:
        return json_response(serialize_doc(user.to_mongo().to_dict())), 200
    return jsonify({"error": "User not found"}), 404

@main.route('/users/<userId>', methods=['PUT'])
def update_user(userId):
    data = request.get_json()
    user = User.objects(userId=userId).first()
    if user:
        user.update(**data)
        user.reload()  # reload the document to get the updated data
        return json_response(serialize_doc(user.to_mongo().to_dict())), 200
    return jsonify({"error": "User not found"}), 404

@main.route('/users/<userId>', methods=['DELETE'])
def delete_user(userId):
    user = User.objects(userId=userId).first()
    if user:
        user.delete()
        return jsonify({"success": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404