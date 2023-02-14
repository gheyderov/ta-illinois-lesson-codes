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


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    company = db.Column(db.String(100))
    message = db.Column(db.String(255))
    is_subscribe = db.Column(db.Boolean)

    def __init__(self, name, email, company, message, is_subscribe):
        self.name = name
        self.email = email
        self.company = company
        self.message = message
        self.is_subscribe = is_subscribe

    def __repr__(self):
        return self.email

    def save(self):
        db.session.add(self)
        db.session.commit()
        



class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    image = db.Column(db.String(100), nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable = False)


    def __init__(self, title, description, price, image, category_id):
        self.title = title
        self.description = description
        self.price = price
        self.image = image
        self.category_id = category_id

    def __repr__(self):
        return self.title

    def save(self):
        db.session.add(self)
        db.session.commit()


class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    product = db.relationship('Product', backref = 'category')

    def __init__(self, name) -> None:
        self.name = name
        
    def __repr__(self):
        return self.name

    def save(self):
        db.session.add(self)
        db.session.commit()