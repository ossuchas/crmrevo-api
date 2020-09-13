import traceback
from flask_restful import Resource, reqparse
from flask import request
from datetime import datetime
from flask_jwt_extended import (
    jwt_required,
    get_raw_jwt
)
from blacklist import BLACKLIST
import json


from models.eqncustomerqa import EQNCustomerTransQAnsModel


class sp_rp_lc_018(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument("projectid", type=str, required=True, help="Project Id field cannot blank allowed")
    # parser.add_argument("unitno", type=str, required=True, help="Unit NO. cannot blank allowed")

    @classmethod
    def get(cls):
        objs = EQNCustomerTransQAnsModel().get_info_test_id()
        keys = ['ID', 'ProjectID']
        res = [{k: v for k, v in zip(keys, obj)} for obj in objs]
        return res, 200

