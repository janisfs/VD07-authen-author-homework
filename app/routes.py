from flask import render_template, url_for, flash, redirect
from flask_login import current_user, login_required
from app import app, db, bcrypt
from app.forms import EditProfileForm
from app.models import User

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route("/profile/edit", methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        current_user.password = hashed_password
        db.session.commit()
        flash('Ваш профиль был обновлен!', 'success')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('edit_profile.html', form=form)
