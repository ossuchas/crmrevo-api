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
    parser.add_argument("projectid", type=str, required=True, help="This Project Idf ield cannot blank allowed")
    parser.add_argument("project_name", type=str, required=True, help="This Project Name field cannot blank allowed")
    parser.add_argument("title_name", type=str)
    parser.add_argument("first_name", type=str, required=True, help="This first_name field cannot blank allowed")
    parser.add_argument("last_name", type=str, required=True, help="This last_name field cannot blank allowed.")
    parser.add_argument("email", type=str, required=True, help="This email field cannot blank allowed.")
    parser.add_argument("mobile_no", type=str, required=True, help="This mobile no. field cannot blank allowed.")
    parser.add_argument("csseen_media", type=str)
    parser.add_argument("csbudget", type=str)
    parser.add_argument("csincome", type=str)
    parser.add_argument("family_income", type=str)
    parser.add_argument("proj_compare", type=str)
    parser.add_argument("products_interest", type=str)
    parser.add_argument("cspersona", type=str)
    parser.add_argument("total_visit", type=str)
    parser.add_argument("reason_visit", type=str)
    parser.add_argument("decision_maker", type=str)
    parser.add_argument("probability", type=str)
    parser.add_argument("comment", type=str)
    parser.add_argument("submit_dttm", type=str)
    parser.add_argument("createdby", type=str)
    parser.add_argument("updatedby", type=str)

    # @jwt_required  # No longer needs brackets
    # def post(self, applicationId):
    #     if EQNCustomerTransQAnsModel.find_by_ref_id(applicationId):
    #         # add to blacklist
    #         jti = get_raw_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
    #         BLACKLIST.add(jti)
    #
    #         return {"message": "E-QN Ref Id with '{}' already exists.".format(applicationId)}, 400
    #
    #     data = EQNCustomerTransQAns.parser.parse_args()
    #
    #     customer = EQNCustomerTransQAnsModel(**data)
    #     customer.eqn_ref_id = applicationId
    #
    #     # add to blacklist
    #     jti = get_raw_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
    #     BLACKLIST.add(jti)
    #
    #     customer.save_to_db()
    #
    #     return user_schema.dump(customer), 200

    @jwt_required  # No longer needs brackets
    def post(self, applicationId):
        data = EQNCustomerTransQAns.parser.parse_args()

        customer = EQNCustomerTransQAnsModel.find_by_ref_id(applicationId)

        if customer:
            customer.eqn_ref_id = applicationId
            customer.projectid = data["projectid"]
            customer.project_name = data["project_name"]
            customer.title_name = data["title_name"]
            customer.first_name = data["first_name"]
            customer.last_name = data["last_name"]
            customer.email = data["email"]
            customer.mobile_no = data["mobile_no"]
            customer.csseen_media = data["csseen_media"]
            customer.csbudget = data["csbudget"]
            customer.csincome = data["csincome"]
            customer.family_income = data["family_income"]
            customer.proj_compare = data["proj_compare"]
            customer.products_interest = data["products_interest"]
            customer.cspersona = data["cspersona"]
            customer.total_visit = data["total_visit"]
            customer.reason_visit = data["reason_visit"]
            customer.decision_maker = data["decision_maker"]
            customer.probability = data["probability"]
            customer.comment = data["comment"]
            customer.submit_dttm = data["submit_dttm"]
            customer.process_flag = "N"
            customer.createdby = data["createdby"]
            customer.updatedby = data["updatedby"]
        else:
            customer = EQNCustomerTransQAnsModel(**data)
            customer.eqn_ref_id = applicationId

        # add to blacklist
        jti = get_raw_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
        BLACKLIST.add(jti)

        customer.save_to_db()

        return user_schema.dump(customer), 200
