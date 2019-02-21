from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(255), nullable=False)

    def comfirm_password(self,password):
        return self.password == password
