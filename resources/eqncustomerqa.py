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
eqn_schema_info = EQNCustomerTransQAnsSchema()
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
    parser.add_argument("total_required_answer", type=int, required=True, help="This fields total required anaser. fields cannot blank allowed." )
    parser.add_argument("consent_ads_flag", type=str, required=True,
                        help="This consent Ads flag field cannot blank allowed.")
    parser.add_argument("consent_bc_flag", type=str, required=True,
                        help="This consent BC flag field cannot blank allowed.")
    parser.add_argument("channel_convenient", type=str)
    parser.add_argument("csseen_media", type=str)
    parser.add_argument("csbudget", type=str)
    parser.add_argument("csincome", type=str)
    parser.add_argument("family_income", type=str)
    parser.add_argument("proj_compare", type=str)
    parser.add_argument("products_interest", type=str)
    parser.add_argument("cspersona", type=str)
    # parser.add_argument("total_visit", type=str)
    parser.add_argument("reason_visit", type=str)
    # parser.add_argument("decision_maker", type=str)
    # parser.add_argument("probability", type=str)

    parser.add_argument("contradiction", type=str)
    parser.add_argument("buyornot", type=str)

    # Modified by Suchat S. 2020-06-03 Add new column from db
    parser.add_argument("age", type=int)
    parser.add_argument("occupation", type=str)
    parser.add_argument("marital_status", type=str)
    parser.add_argument("children_numb", type=int)
    parser.add_argument("objective_considering", type=str)
    parser.add_argument("housing_characteristics", type=str)
    parser.add_argument("online_media", type=str)
    parser.add_argument("offline_media", type=str)
    parser.add_argument("visit_route", type=str)
    parser.add_argument("deeplink_url", type=str)
    parser.add_argument("lcowner", type=str)

    parser.add_argument("other", type=str)
    parser.add_argument("comment", type=str)
    parser.add_argument("total_answer", type=int)
    parser.add_argument("total_question", type=int)
    parser.add_argument("submit_dttm", type=str)
    parser.add_argument("createdby", type=str)
    parser.add_argument("updatedby", type=str)

    # Add new column for improve E-QN System
    # Modified by Suchat S. 2020-10-18
    parser.add_argument("tran_type", type=str)
    parser.add_argument("revisit_flag", type=str)

    parser.add_argument("contact_ref_id", type=str)
    parser.add_argument("contact_ref_guid", type=str)

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
            customer.consent_ads_flag = data["consent_ads_flag"]
            customer.consent_bc_flag = data["consent_bc_flag"]
            customer.channel_convenient = data["channel_convenient"]
            customer.csseen_media = data["csseen_media"]
            customer.csbudget = data["csbudget"]
            customer.csincome = data["csincome"]
            customer.family_income = data["family_income"]
            customer.proj_compare = data["proj_compare"]
            customer.products_interest = data["products_interest"]
            customer.cspersona = data["cspersona"]
            # customer.total_visit = data["total_visit"]
            customer.reason_visit = data["reason_visit"]
            # customer.decision_maker = data["decision_maker"]
            # customer.probability = data["probability"]
            customer.contradiction = data["contradiction"]
            customer.buyornot = data["buyornot"]

            # Modified by Suchat S. 2020-06-03 Add new column from db
            customer.age = data["age"]
            customer.occupation = data["occupation"]
            customer.marital_status = data["marital_status"]
            customer.children_numb = data["children_numb"]
            customer.objective_considering = data["objective_considering"]
            customer.housing_characteristics = data["housing_characteristics"]
            customer.online_media = data["online_media"]
            customer.offline_media = data["offline_media"]
            customer.visit_route = data["visit_route"]
            customer.deeplink_url = data["deeplink_url"]
            customer.lcowner = data["lcowner"]

            customer.other = data["other"]
            customer.comment = data["comment"]
            customer.total_answer = data["total_answer"]
            customer.total_required_answer = data["total_required_answer"]
            customer.total_question= data["total_question"]
            customer.submit_dttm = data["submit_dttm"]
            customer.process_flag = "N"
            customer.createdby = data["createdby"]
            customer.updatedby = data["updatedby"]

            # Add new column for improve E-QN System
            # Modified by Suchat S. 2020-10-18
            customer.tran_type = data["tran_type"]
            customer.revisit_flag = data["revisit_flag"]

            customer.contact_ref_id = data["contact_ref_id"]
            customer.contact_ref_guid = data["contact_ref_guid"]
        else:
            customer = EQNCustomerTransQAnsModel(**data)
            customer.eqn_ref_id = applicationId

        # add to blacklist
        jti = get_raw_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
        BLACKLIST.add(jti)

        customer.save_to_db()

        return user_schema.dump(customer), 200


class EQNCustomerTransQAnsInfo(Resource):
    @jwt_required
    def get(self, tran_id: str):
        obj_eqn = EQNCustomerTransQAnsModel.find_by_tran_id(tran_id)
        if obj_eqn:
            # add to blacklist
            jti = get_raw_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
            BLACKLIST.add(jti)

            return eqn_schema_info.dump(obj_eqn), 200

        return {"message": "No Data Found"}, 404

