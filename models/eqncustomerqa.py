from db import db
from typing import List
import uuid
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime


class EQNCustomerTransQAnsModel(db.Model):
    __tablename__ = "CustomerTransQAns"
    __table_args__ = {"schema": "EQN"}

    tran_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    contact_ref_id = db.Column(db.String(255), nullable=True)
    contact_ref_guid = db.Column(UUID(as_uuid=True), nullable=True)
    eqn_ref_id = db.Column(db.String(255), nullable=False)
    projectid = db.Column(db.String(20), nullable=False)
    project_name = db.Column(db.String(255), nullable=False)
    title_name = db.Column(db.String(50), nullable=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    mobile_no = db.Column(db.String(50), nullable=False)
    consent_ads_flag = db.Column(db.String(2), nullable=False, default="N")
    consent_bc_flag = db.Column(db.String(2), nullable=False, default="N")
    channel_convenient = db.Column(db.String(5))
    csseen_media = db.Column(db.String(2000))
    csbudget = db.Column(db.String(200))
    csincome = db.Column(db.String(200))
    family_income = db.Column(db.String(200))
    proj_compare = db.Column(db.String(255))
    products_interest = db.Column(db.String(2000))
    cspersona = db.Column(db.String(2000))
    # total_visit = db.Column(db.String(100))
    reason_visit = db.Column(db.String(2000))
    # decision_maker = db.Column(db.String(255))
    # probability = db.Column(db.String(100))

    contradiction = db.Column(db.String(255))
    buyornot = db.Column(db.String(255))

    # Modified by Suchat S. 2020-06-03 Add new column from db
    age = db.Column(db.Integer)
    occupation = db.Column(db.String(255))
    marital_status = db.Column(db.String(255))
    children_numb = db.Column(db.Integer)
    objective_considering = db.Column(db.String(2000))
    housing_characteristics = db.Column(db.String(2000))
    online_media = db.Column(db.String(2000))
    offline_media = db.Column(db.String(2000))
    visit_route = db.Column(db.String(2000))

    deeplink_url = db.Column(db.String(2000))

    lcowner = db.Column(db.String(50))

    other = db.Column(db.String(2000))

    comment = db.Column(db.String(2000))
    total_answer = db.Column(db.Integer, default=0)
    total_question = db.Column(db.Integer, default=0)
    submit_dttm = db.Column(db.String(20))
    process_flag = db.Column(db.String(1), default='N')
    # created = db.Column(db.DateTime, default=datetime.now())
    createdby = db.Column(db.String(50), default='flaskapi')
    # updated = db.Column(db.DateTime, default=datetime.now())
    updatedby = db.Column(db.String(50), default='flaskapi')

    # Add new column for improve E-QN System
    # Modified by Suchat S. 2020-10-18
    tran_type = db.Column(db.String(2), default='A')
    revisit_flag = db.Column(db.String(2), default='N')
    total_required_answer = db.Column(db.Integer, default=0)

    OpportunityID = db.Column(UUID(as_uuid=True))

    @classmethod
    def find_by_ref_id(cls, _eqn_ref_id: str) -> "EQNCustomerTransQAnsModel":
        return cls.query.filter_by(eqn_ref_id=_eqn_ref_id).first()

    @classmethod
    def find_by_tran_id(cls, _tran_id: str) -> "EQNCustomerTransQAnsModel":
        return cls.query.filter_by(tran_id=_tran_id).first()

    @classmethod
    def get_info_test_id(cls):
        sql_statement = """
           EXECUTE sp_kai_test @FileName = 0
           """
        return db.session.execute(sql_statement).fetchall()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
