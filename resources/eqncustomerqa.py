import traceback
from flask_restful import Resource, reqparse
from flask import request
from datetime import datetime
from flask_jwt_extended import (
    jwt_required,
    get_raw_jwt
)
from blacklist import BLACKLIST


from models.eqncustomerqa import EQNCustomerTransQAnsModel
from schemas.eqncustomerqa import EQNCustomerTransQAnsSchema

user_schema = EQNCustomerTransQAnsSchema(only=("tran_id", "eqn_ref_id"))
user_list_schema = EQNCustomerTransQAnsSchema(many=True)


class EQNCustomerTransQAns(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("first_name", type=str, required=True, help="This first_name field cannot blank allowed")
    parser.add_argument("last_name", type=str, required=True, help="This last_name field cannot blank allowed.")
    parser.add_argument("email", type=str, required=True, help="This email field cannot blank allowed.")
    parser.add_argument("mobile_no", type=str, required=True, help="This mobile no. field cannot blank allowed.")
    parser.add_argument("createdby", type=str)
    parser.add_argument("updatedby", type=str)

    @jwt_required  # No longer needs brackets
    def post(self, applicationId):
        if EQNCustomerTransQAnsModel.find_by_ref_id(applicationId):
            # add to blacklist
            jti = get_raw_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
            BLACKLIST.add(jti)

            return {"message": "E-QN Ref Id with '{}' already exists.".format(applicationId)}, 400

        data = EQNCustomerTransQAns.parser.parse_args()

        customer = EQNCustomerTransQAnsModel(**data)
        customer.eqn_ref_id = applicationId

        # add to blacklist
        jti = get_raw_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
        BLACKLIST.add(jti)

        customer.save_to_db()

        return user_schema.dump(customer), 200
        # return {'message':'success'}, 200

    def put(self, applicationId):
        return {'message': 'save'}, 200


