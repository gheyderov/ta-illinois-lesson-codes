from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    last_name = db.Column(db.String(100), nullable = False)
    blog = db.relationship('Blog', backref = 'user')

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __repr__(self):
        return self.name

    def save(self):
        db.session.add(self)
        db.session.commit()


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(100), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id

    def __repr__(self):
        return self.title

    def save(self):
        db.session.add(self)
        db.session.commit()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    image = db.Column(db.String(100), nullable = False)


    def __init__(self, title, description, price, image):
        self.title = title
        self.description = description
        self.price = price
        self.image = image

    def __repr__(self):
        return self.title

    def save(self):
        db.session.add(self)
        db.session.commit()