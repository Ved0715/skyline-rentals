from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from app.models.user import User
from app import db

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                current_user_id = get_jwt_identity()
                user = db.session.get(User, current_user_id)
                
                if not user or user.role != 'admin':
                    return jsonify(msg="Admins only!"), 403
                    
                return fn(*args, **kwargs)
            except Exception as e:
                return jsonify(msg="Authorization error", error=str(e)), 500
        return decorator
    return wrapper
