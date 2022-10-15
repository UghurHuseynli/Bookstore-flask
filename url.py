from flask import flash, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user
from app import app
from models import *
from forms import *

@app.route("/")
def index():
    books = Book.query.all()
    return render_template('index.html', books = books)


@app.route("/product")
@login_required
def product():
    book = {}
    return render_template('product.html', book=book)

@app.route('/book/<int:book_id>', methods=["GET", "POST"])
@login_required
def book(book_id):
    form = CommetForm(request.form)
    if request.method == "POST" and form.validate():
        my_comment = Comment(full_name = form.full_name.data, content = form.content.data, book_id = book_id)
        my_comment.save()
        flash('Şərhiniz əlavə edildi', 'success')
        return redirect(url_for('book', book_id = book_id))
    else:
        books = Book.query.all()
        book = Book.query.filter(Book.id == book_id).first()
        genre = Genre.query.filter(Genre.id == book.genre_id).first()
        lang = Lang.query.filter(Lang.id == book.language_id).first()
        comments = Comment.query.filter(Comment.book_id == book_id).all()
        return render_template('book.html', book = book, genre = genre, lang = lang, books = books, form = form, comments = comments)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        password_ = generate_password_hash(form.password.data)
        user = User(name = form.name.data, surname = form.surname.data, email = form.email.data, username = form.username.data, password = password_, is_active= True, is_superuser= False)
        user.save()
        flash('Qeydiyyatdan uğurla keçdiniz', 'success')
        return redirect(url_for('login'))
    else:
        return render_template('register.html', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter(User.username == form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Hesabınıza daxil oldunuz', 'success')
            return redirect(url_for('index'))
        else:
            flash('İstifadəçi adı və ya parol yanlışdır', 'danger')
    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Hesabdan çıxış edildi', 'success')
    return redirect(url_for('index'))