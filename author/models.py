from blog_with_flask import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(60))
    email = db.Column(db.String(30), unique=True)
    username = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(60))
    is_author = db.Column(db.Boolean)

    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, fullname, email,
                 username, password, is_author=False):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email
        self.is_author = is_author

    def __repr__(self):
        return '<Author {}>'.format(self.username)

