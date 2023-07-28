

from flask import Flask, render_template, request      # redirect, url_for  (better not in order to not to have arguments passed in the URL)

from markupsafe import escape

import re

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def contact_form():
    if request.method == 'POST':
        
        # Check if the honeypot field is filled (i.e., filled by a bot)
        if request.form['bot_field']:
            return render_template('confirmation.html')

        
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        country = request.form['country']
        message = request.form['message']
        gender = request.form['gender']
        subject = request.form.getlist('subject') # Get multiple checkboxes as a list
        
         # Sanitization (remove any harmful characters)
        first_name = sanitize_input(first_name)
        last_name = sanitize_input(last_name)
        message = sanitize_message(message)
        email = valid_email(email)
        
        if not (first_name and last_name and email and country and message):
            return render_template("index.html", error="All fields are mandatory!", countries=["Italy","Belgium","Spain","Germany","Portugal","France"], 
                                   first_name=first_name, 
                                   last_name=last_name, 
                                   email=email, country=country, 
                                   message=message, 
                                   gender=gender, 
                                   subject=subject)   # error="All fields are mandatory!" is for jinja to be used
        
        
        if email == False:
            return render_template("index.html", error="All fields are mandatory!", countries=["Italy","Belgium","Spain","Germany","Portugal","France"], 
                                   first_name=first_name, 
                                   last_name=last_name, 
                                   email=email, country=country, 
                                   message=message, 
                                   gender=gender, 
                                   subject=subject)
        
        return render_template("confirmation.html", first_name=first_name, last_name=last_name, email=email, country=country, message=message, gender=gender, subject=subject)
        
    return render_template("index.html", countries=["Italy","Belgium","Spain","Germany","Portugal","France"])




def sanitize_input(input_data):
    # Remove whitespace beggining and tail [strip()], and replacing special chars [escape()]
    to_sanitize = re.sub(r'[^a-zA-Z0-9\s]', '', input_data)
    to_sanitize = escape(to_sanitize)
    return to_sanitize


def sanitize_message(input_message):
    # To remove potential malicious script into the "message" field
    to_sanitize = re.sub(r'[^\w\s.,:?!+\-@()]+', '', input_message)    # to_sanitize = escape(input_message)
    return to_sanitize



def valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email))
    



if __name__ == "__main__":
    app.run(debug=True)
    