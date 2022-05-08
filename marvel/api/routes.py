from urllib import response
from flask import Blueprint, request, jsonify
from marvel.helpers import token_required
from marvel.models import db, Character, character_schema, characters_schema
api = Blueprint('api', __name__, url_prefix='/api')

@api.route("/getdata")
def getdata():
    return {"some": "value", "foo":"bar"}

@api.route('/characters', methods=['POST'])
@token_required
def create_character(current_user_token):
    name = request.json['name']
    description = request.json['description']
    character_token = current_user_token.token

    print (f'TESTER: {current_user_token.token}')

    character = Character(name,description,user_token = character_token)

    db.session.add(character)
    db.session.commit()

    response = character_schema.dump(character)
    return jsonify(response)

@api.route('/characters', methods = ['GET'])
@token_required
def get_characters(current_user_token):
    owner = current_user_token.token
    characters = Character.query.filter_by(user_token = owner).all()
    response = characters_schema.dump(characters)
    return jsonify(response)

@api.route('/characters/<id>', methods = ['GET'])
@token_required
def get_character(current_user_token, id):
    owner = current_user_token.token
    if character:
        print('Your character is: {character.name}')
        character = Character.query.get(id)
        response = character_schema.dump(character)
        return jsonify(response)
    else:
        return jsonify({'that better not have been a DC character...'})


@api.route('/characters/<id>', methods = ['POST', 'PUT'])
@token_required
def update_character(current_user_token, id):
    character = Character.query.get(id)
    print(character)
    character.name = request.json['name']
    character.description = request.json['description']
    character.user_token = current_user_token.token

    db.session.commit()
    response = character_schema.dump(character)
    return jsonify(response)


@api.route('/characters/<id>', methods = ['DELETE'])
@token_required
def delete_character(current_user_token, id):
    character = Character.query.get(id)
    db.session.delete(character)
    db.session.commit()
    return jsonify(response)
