"""
api.py  
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Todo

api = Blueprint('api', __name__)


@api.route('/hello/<string:name>/')
def say_hello(name):
    response = {'msg': "Hello {}".format(name)}
    return jsonify(response)


@api.route('/todos', methods=('GET', 'POST'))
def todos():
    if request.method == 'GET':
        todos = Todo.query.all()
        return jsonify({'todos': [t.to_dict() for t in todos]})
    elif request.method == 'POST':
        data = request.get_json()
        todo = Todo(
            name=data['name'],
            description=data['description'],
            completed=data['completed'],
        )
        db.session.add(todo)
        db.session.commit()
        return jsonify(todo.to_dict()), 201


@api.route('/todos/<int:id>', methods=('GET', 'PUT'))
def todo(id):
    if request.method == 'GET':
        todo = Todo.query.get(id)
        return jsonify({'todo': todo.to_dict()})
    elif request.method == 'PUT':
        data = request.get_json()
        todo = Todo.query.get(id)

        todo.name = data['name']
        todo.description = data['description']
        todo.completed = data['completed']

        db.session.commit()

        return jsonify(todo.to_dict()), 201
