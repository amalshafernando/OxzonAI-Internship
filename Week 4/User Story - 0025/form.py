from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for CSRF protection

# Define the form using Flask-WTF
class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        # Retrieve form data after validation
        form_data = {
            'name': form.name.data,
            'email': form.email.data,
            'address': form.address.data
        }
        # Pass data to the index.html template
      #  return render_template("index.html", form_data=form_data)
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
