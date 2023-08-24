from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Default_Image = "https://tinyurl.com/demo-cupcake"
class Cupcake(db.Model):
    """Cupcake Table"""
    __tablename__ = "cupcakes"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    flavor = db.Column(db.Text, nullable = False)
    size = db.Column(db.Text, nullable = False)
    rating = db.Column(db.Text, nullable = False)
    image = db.Column(db.Text, nullable = False, default = Default_Image)

    def _dict(self):
        """Serialize cupcake info to a dictionary"""
        return {
            "id": self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.size,
            "image":self.image,
        }

def connect_db(app):
    db.app = app
    db.init_app(app)