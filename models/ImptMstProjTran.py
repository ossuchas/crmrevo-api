from db import db
from typing import List
import uuid
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class ImptMstProjTranModel(db.Model):
    __tablename__ = "ImptMstProjTran"
    __table_args__ = {"schema": "LOG"}

    ID = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    Created = db.Column(db.DateTime)
    Updated = db.Column(db.DateTime)
    CreatedByUserID	= db.Column(UUID(as_uuid=True))
    UpdatedByUserID	= db.Column(UUID(as_uuid=True))
    IsDeleted = db.Column(db.Boolean)
    ProjectID = db.Column(UUID(as_uuid=True))
    Import_Type = db.Column(db.String(20))
    Import_Status = db.Column(db.String(2))

    @classmethod
    def find_by_ref_id(cls, _id: str) -> "ImptMstProjTranModel":
        return cls.query.filter_by(ID=_id, Import_Status='P').first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
