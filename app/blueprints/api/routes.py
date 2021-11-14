from app.blueprints.auth.models import User
from .import bp as api
from flask import jsonify, request
from app import db
from app.blueprints.main.models import Post
import json

# TEST ROUTE
@api.route('/poster', methods=['POST'])
def get_poster():
    """
    [POST] /api/poster
    """
    data = json.loads(request.data.decode('utf-8'))
    u = User.query.filter_by(email=data['user_email']).first()
    print(u)
    # posts = [p.to_dict() for p in Post.query.all()]
    return jsonify({ 'message': 'work PLEASSEEE' })
    # return jsonify({posts})
# TEST ROUTE






# All posts
@api.route('/posts', methods=['GET'])
def get_posts():
    """
    [GET] /api/posts
    """
    posts = [p.to_dict() for p in Post.query.all()]
    print(posts[0])
    return jsonify({ 'messages':posts })

# Single posts


@api.route('/post/<id>', methods=['GET'])
def get_post(id):
    print(id)
    """
    [GET] /api/post/<id>
    """
    return jsonify(Post.query.get_or_404(id).to_dict())

# Create new post


@api.route('/posts', methods=['POST'])
def create_post():
    """
    [POST] /api/posts
    """
    p = Post()
    p.from_dict(request.json)
    p.save()
    return jsonify({'message': 'CREATED POST'})
    # return jsonify(post.to_dict())


# Updating existing posts


@api.route('/post/<id>', methods=['PUT'])
def update_post(id):
    """
    [PUT] /api/post/<id>
    """
    post = Post.query.get(id)
    post.from_dict(request.json)
    db.session.commit()
    return jsonify(post.to_dict())

# Delete existing posts


@api.route('/post/<id>', methods=['DELETE'])
def delete_post(id):
    """
    [DELETE] /api/posts
    """
    post = Post.query.get(id)
    post.delete()
    return jsonify([p.to_dict() for p in Post.query.all()])


###########################################
############# User API Routes #############
###########################################
@api.route('/users', methods=['GET'])
def get_users():
    """
    [GET] /api/users
    """
    users = [u.to_dict() for u in User.query.all()]
    return jsonify({ 'users':users })
