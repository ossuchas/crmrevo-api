from flask_restful import Resource, reqparse
# from flask_jwt_extended import (
#     jwt_required,
#     get_jwt_claims,
#     get_jwt_identity,
#     jwt_optional,
#     fresh_jwt_required,
# )
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    fresh_jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    jwt_required,
    get_raw_jwt,
)
from blacklist import BLACKLIST


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "store_id", type=int, required=True, help="Every item needs a store_id."
    )

    @jwt_required  # No longer needs brackets
    def get(self, name):
        return {"message": "Item not found."}, 404

    @jwt_required  # No longer needs brackets
    def post(self, name):
        try:
            jti = get_raw_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
            BLACKLIST.add(jti)
            return {'message': name}, 201
        except:
            return {"message": "An error occurred while inserting the item."}, 500

        # return {'message': 'xxxx'}, 201

