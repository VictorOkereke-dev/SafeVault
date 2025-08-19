from flask import Flask, request, jsonify
from app.auth import generate_token, role_required
from app.validators import is_valid_email, is_strong_password
from app.db import query_user_by_email

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not is_valid_email(email) or not is_strong_password(password):
        return jsonify({'error': 'Invalid credentials'}), 400

    user = query_user_by_email(email)
    if user and user['password'] == password:
        token = generate_token(user['id'], user['role'])
        return jsonify({'token': token})
    return jsonify({'error': 'Authentication failed'}), 401

@app.route('/admin', methods=['GET'])
@role_required('admin')
def admin_dashboard():
    return jsonify({'message': 'Welcome, Admin!'})

