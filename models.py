from flask_login import UserMixin
from app import db, login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Genre(db.Model):
    __tablename__ = 'Genre'

    def __init__(self, name):
        self.name = name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return self.name
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class Lang(db.Model):
    __tablename__ = 'Lang'
    def __init__(self, lang_code, lang_name):
        self.lang_code = lang_code
        self.lang_name = lang_name

    id = db.Column(db.Integer, primary_key=True)
    lang_code = db.Column(db.String(2))
    lang_name = db.Column(db.String(100))

    def __repr__(self):
        return self.lang_name

    def save(self):
        db.session.add(self)
        db.session.commit()

class Book(db.Model):
    __tablename__ = 'Book'
    def __init__(self, title, author, price, description, image_url, stock, publisher, genre_id, language_id):
        self.title = title
        self.author = author
        self.price = price
        self.description = description
        self.image_url = image_url
        self.stock = stock
        self.publisher = publisher
        self.genre_id = genre_id
        self.language_id = language_id

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    author = db.Column(db.String(40))
    price = db.Column(db.Float)
    description = db.Column(db.String(1000))
    image_url = db.Column(db.String(500))
    stock = db.Column(db.Integer)
    publisher = db.Column(db.String(100))
    genre_id = db.Column(db.Integer, db.ForeignKey('Genre.id'))
    language_id = db.Column(db.Integer, db.ForeignKey('Lang.id'))

    def __repr__(self):
        return self.title

    def save(self):
        db.session.add(self)
        db.session.commit()

class Comment(db.Model):
    __tablename__ = 'Comment'
    def __init__(self, full_name, content, book_id):
        self.full_name = full_name
        self.content = content
        self.book_id = book_id

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable = False)
    content = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    book_id = db.Column(db.Integer, db.ForeignKey('Book.id'))

    def __repr__(self):
        return self.full_name

    def save(self):
        db.session.add(self)
        db.session.commit()

class User(db.Model, UserMixin):
    __tablename__ = 'User'
    def __init__(self, name, surname, email, username, password, is_active, is_superuser):
        self.name = name 
        self.surname = surname
        self.email = email 
        self.username = username 
        self.password = password
        self.is_active = is_active
        self.is_superuser = is_superuser

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    surname = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    username = db.Column(db.String(30), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default = False)
    is_superuser = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return self.username

    def save(self):
        db.session.add(self)
        db.session.commit()
    
