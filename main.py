from flask import Flask, render_template, url_for, flash
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '\xb9K\xe7\x05\x92\x83\x14Fq!\xf1\x85\xdc'

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')
@app.route("/register", methods=['GET', 'POST'])
def register():
    # form = RegistrationForm()
    # if form.validate_on_submit():
    #     flash(f"Account successfully created for {form.firstname.data}!!", 'success')
    #     return redirect(url_for('home')) 
    return render_template('register.html') 

if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")