# Explanation of the project

>First thing we need to do is to Install flask:

	  pip install Flask 

> Create a virtual environment in a folder of the Project (Flask_project), this is optional, but in my opinion a good practice.

	 python -m venv venv

 the second "venv" is the name of the virtual env created.

> To activate the Venv created, go to dir created and: 

	.\venv\Script\activate

Inside the project folder we will have venv folder now.

___________________________

<br/>

----------------------------
### Creating the Pytho file

>We will use VScode for this project.
>First thing to do is to use python interpreter of the virtual env created.
>Then create a PYTHON file were we will import the module Flask
	
	from flask import Flask

	app = Flask(__name__)

	@app.route('/')

	def home():
		
		return "Helllo World!"

	if __name__ == "__main__":
		app.run()

With this, if we run the file in terminal we will have a localhost webaddress and we can see the string "Hello World!"

______________________________________

<br/>

_________________________________________


> Lets create an HTML file as our base page with:
> - a "Form" to fill;
> - with a honeypot input for potential bots;
> - jinja2 templating as requested. (where we use " {% %} ")

<br/>


	<html lang="en">
	
	<head>
	
	    <meta charset="UTF-8">
	
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	
	    <title>Contact page</title>
	
	    <style>
	
	        body{
	
	            text-align:center;
	
	        }
	
	    </style>
	
	</head>
	
	<body>
	
	    <h1>This is the Home Page!</h1>
	
	  
	
	    <form method="post">
	
	        First name: <input name="first_name" required value="{{ first_name }}"/>  <!-- "required" is neede if we make mandatory to fill the field.-->
	
	        Last name: <input name="last_name" required value="{{ last_name }}"/>
	
	        <br/><br/>
	
	        Email: <input type="email" name="email" required value="{{ email }}"/>
	
	        Country: <select name="country" required>      <!-- for a list we will use the 'select' method, with 'options' under-->
	
	            {% for country in countries %}
	
	            <option value="{{country}}">{{country}}</option>
	
	            {% endfor %}
	
	            <!-- <option value="italy">Italy</option>
	
	            <option value="belgium">Belgium</option>
	
	            <option value="germany">Germany</option>
	
	            <option value="netherlands">Netherlands</option>
	
	            <option value="spain">Spain</option>
	
	            <option value="portugal">Portugal</option> -->
	
	        </select>
	
	        <br/><br/>
	
	        Message: <input name="message" required value="{{ message }}"/>
	
	        <br/><br/>
	
	        Gender: <input type="radio" name="gender" value="Male" required {% if gender == "Male" %}checked{% endif %}/> Male
	
	                <input type="radio" name="gender" value="Woman" {% if gender == "Woman" %}checked{% endif %} required/> Woman
	
	        <br/><br/>
	
	        Subject: <input type="checkbox" name="subject" value="Repair" {% if "Repair" in subject %}checked{% endif %}> Repair
	
	                 <input type="checkbox" name="subject" value="Order" {% if "Order" in subject %}checked{% endif %}> Order
	
	                 <input type="checkbox" checked name="subject" value="Other" {% if "Other" in subject %}checked{% endif %}> Other
	
	  
	
	        <br/><br/>
	
	        <button type="submit">Submit</button>
	
	  
	
	        <!-- Honeypot anti-spam technique -->
	
	        <input type="text" name="bot_field" style="display: none;">
	
	    </form>
	
	  
	
	</body>
	
	</html>


________________________________
[Here for the HTML file](https://github.com/Crucius96/Becode-Projects/blob/master/Flask_project/templates/index.html)

<br/>
_______________________
  
### Now back to our python file

<br/>

>Let's implement the necessary functions such as : 
>- render_template  =  used to render to the designated HTML page.
>- request  =  used to request a GET to the web.
>- re  =  RegEx for sanitization and validation.
>- escape  =  for sanitization.
  
	from flask import Flask, render_template, request      # redirect, url_for  (better not in order to not to have arguments passed in the URL)
	
	  
	
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
	
	                                   subject=subject)   # error="All fields are mandatory!" is for jinja to be used
	
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
	
	    to_sanitize = re.sub(r'[^\w\s.,:?!+\-@()]+', '', input_message)    # to_sanitize = escape(input_message)
	
	    return to_sanitize
	
	  
	  
	  
	
	def valid_email(email):
	
	    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
	
	    return bool(re.match(email_pattern, email))
	
	  
	  
	  
	
	if __name__ == "__main__":
	
	    app.run(debug=True)

[Here for the python file](https://github.com/Crucius96/Becode-Projects/blob/master/Flask_project/app.py)

<br/>

_______________________________________________________

<br/>

### Then finally we will create a confirmation HTML where the user will be redirected ONLY if the inputs passes the "sanitization and validation" of the form

[Here for the confirmation HTML](https://github.com/Crucius96/Becode-Projects/blob/master/Flask_project/templates/confirmation.html)

<br/>

_____________________________________________________

<br/>

### Implement Sanitization and Validation of the form
<br/>

		Sanitization 

<br/>

>It is primarily focused on preventing security vulnerabilities, such as **Cross-Site Scripting (XSS)** attacks, where malicious code is injected into the application. Sanitization ensures that any user-submitted data is safe to use and display.
 	Common sanitization techniques include: 
 > - Removing or escaping special characters that can be used for code injection (e.g., `<`, `>`, `&`).
>- Removing HTML tags or using HTML escaping to prevent HTML injection.
>- Limiting input length to prevent buffer overflow attacks.

_Sanitization should be performed on all user input before storing it in a database, displaying it on web pages, or using it in any other context where it may be executed or rendered._


	The MarkupSafe library, which comes bundled with Flask. The MarkupSafe library provides the escape() function. For example, the `<` character is replaced with `&lt;`, and the `>` character is replaced with `&gt;`. This prevents the special characters from being interpreted as HTML or XML tags, which makes it more difficult for attackers to exploit XSS vulnerabilities.

<br/>

_____________________________

<br/>

		Validation

<br/>

> Validation is the process of checking if user input adheres to certain rules or criteria, ensuring that the data is valid and appropriate for the application's requirements.
> Common validation checks include:
>
>- Ensuring required fields are not empty.
>- Validating email addresses, ensuring they match a specific format (e.g., `user@example.com`).
>- Verifying that numerical input is within a specific range or meets specific criteria (e.g., positive integer).
>- Validating dates, phone numbers, and other specific formats.
>- Checking for the presence of spam or bot-like behavior (e.g., using honeypot fields).

_Validation can occur on the client-side (using JavaScript) to provide immediate feedback to the user and improve the user experience. However, client-side validation is not sufficient for security, as malicious users can bypass it. Therefore, server-side validation (in our Python script) is essential to ensure the integrity of the data._

##### Sanitization focuses on security, while validation focuses on data correctness. Both processes are necessary to handle user input effectively and securely.

