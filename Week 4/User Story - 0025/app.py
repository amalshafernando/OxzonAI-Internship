from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html') 

@app.route('/form', methods = ['POST', 'GET'])
def form():
    if request.method == 'POST':
        # Get the form data
        form_data = request.form
        # Ensure form_data is passed correctly to the template as user_data
        return render_template("form.html", user_data=form_data)
    else:
        # If the method is GET (e.g., direct access to '/success'), return a valid response.
        return "Invalid request method. Please submit the form."    

if __name__ == '__main__':
    app.run(debug=True)
