from db import db
from typing import List
import uuid
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class EQNCustomerTransQAnsModel(db.Model):
    __tablename__ = "CustomerTransQAns"
    __table_args__ = {"schema": "EQN"}

    tran_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    eqn_ref_id = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    mobile_no = db.Column(db.String(50), nullable=False)

    @classmethod
    def find_by_ref_id(cls, _eqn_ref_id: str) -> "EQNCustomerTransQAnsModel":
        return cls.query.filter_by(eqn_ref_id=_eqn_ref_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
