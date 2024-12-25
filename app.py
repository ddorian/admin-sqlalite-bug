
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy_lite import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import sqlalchemy as sa
app = Flask(__name__)

app.config["SQLALCHEMY_ENGINES"]={
        "default": "postgresql+psycopg://postgres:1@127.0.0.1:5432/myadmin",
}
app.config["DEBUG"] = True

db = SQLAlchemy(
    app,
)

class Model(DeclarativeBase):
    pass

# Create models
class User(Model):
    __tablename__ = "users"
    id = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)



admin = Admin(app, name='microblog')
# Add administrative views here

with app.app_context():
    admin.add_view(ModelView(User, db.session))

if __name__ == "__main__":
    with app.app_context():
        Model.metadata.create_all(db.engine)
        db.session.execute(sa.text("alter database myadmin set idle_in_transaction_session_timeout=3000;"))
    app.run()
