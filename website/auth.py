from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)


@auth.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        
        """query the database"""
        
        user = User.query.filter_by(email=email).first()
        if user:
            if password == user.password:
                flash('Login successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for("views.create"))
            else:
                flash('Incorrect password', category='error')
        else: flash('Email does not exist', category='sucess')
        
    return render_template('login.html', user=current_user)

@auth.route('/signup', methods = ['POST', 'GET'])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash("This user already existed", category='error')       
        elif password != confirm_password:
            flash("Passwords do not match. Please try again.", category="error")
        else:            
            
            """ create user account and add to database"""
            
            new_user = User(email=email, firstname=firstname,password=password)
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Signup successful!", category="success")
            return redirect(url_for('views.create'))       
        
    return render_template('signup.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.welcome'))
    
