from flask import Blueprint, render_template, request
import re

sac_email_condition = "^[a-z]+(2[3-9]|[3-9][0-9])+[@]+(my.sevkoleji.k12.tr)"
koc_email_condition = "^[a-z]+(202[3-9]|20[3-9][0-9])+[@]+(stu.koc.k12.tr)"

auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    return render_template('login.html')#"<p>Login</p>"


@auth.route('/logout')
def logout():
    return render_template('logout.html')#"<p>Log Out</p>"


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('confirm_password')

        if len(username) <= 3:
            pass
        elif re.search(pattern=sac_email_condition, string=email) == False:
            pass
        elif re.search(pattern=koc_email_condition, string=email) == False:
            pass
        elif len(password1) < 7:
            pass
        elif password1 != password2:
            pass
        else:
            #add user to db
            pass



        

    return render_template('register.html')#"<p>Register</p>"