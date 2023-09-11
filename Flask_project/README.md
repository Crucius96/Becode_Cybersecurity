# Flask Project

[Here to redirect to the explanation and methodologies used for the project](https://github.com/Crucius96/Becode-Projects/blob/master/Flask_project/explanation.md)

## Problem statement:
The company Hackers Poulette™ sells DIY kits and accessories for Rasperri Pi. They want to allow their users to contact their technical support. Your mission is to develop a Python script that displays a contact form and processes its response: sanitization, validation, and then sending feedback to the user.

## Performance criteria:
*Backend: PYTHON programming (introduction to logical structures).
* Implementation of POST and GET methods.
* Implementation of templates with Jinja.
* If the user makes an error, the form should be returned to them with valid responses preserved in their respective input fields.
* Ideally, display error messages near their respective fields.
* The form will perform server-side:
	- Sanitization: neutralizing any harmful encoding (<script>).
	- Validation: mandatory fields + valid email.
* If sanitization and validation are successful, a "Thank you for contacting us." page will be displayed, summarizing all the encoded information.
* Implementation of the honeypot anti-spam technique.
* NO NEED FOR JAVASCRIPT OR CSS.

#### Form fields
- First name & last name. 
- Email.
- Country (list).
- Message. 
- Gender (M/F) (Radio box).
- 3 possible subjects (Repair, Order, Others) (checkboxes). 
All fields are mandatory, except for the subject (in this case, the value should be "Others").
