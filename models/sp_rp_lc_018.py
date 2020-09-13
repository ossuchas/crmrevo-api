from db import db


class sp_rp_lc_018(db.Model):
    __tablename__ = "AP2SP_RP_LC_018"

    ID = db.Column(db.String(50), primary_key=True)
    ProjectID = db.Column(db.String(50))

    def sp_get_info(self):
        sql_statement = """ 
        SELECT ID, ProjectID 
        FROM PRJ.Unit 
        WHERE ProjectID = '76B1B40F-74C7-43E3-B0A6-26D5B9FACD6D'
        AND UnitNo = 'A10A236'
        """
        obj = db.session.execute(sql_statement).fetchone()
        return obj
