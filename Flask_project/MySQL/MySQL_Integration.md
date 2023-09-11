# MySQL Integration


> [Set up MySQL into flask .py](https://www.freecodecamp.org/news/connect-python-with-sql/), in this link I found the easiest explanation on how to integrate DataBase into a Webapp.

In alternative there is this other way that personally I find more complicated:
[FULL TUTORIAL HOW TO SET UP MYSQL](https://hevodata.com/learn/flask-mysql/)
 - this is with PHP - APACHE.


____________________________________________________

#### Create a Database where to store the data that we will be collecting

Using MySQL WorkBench or The Command line Client.


______________________________________________________________


#### Now Let's implement it in on our Flask file (Flask Project)

	 Pip install MySQL-connector-python

 or 

	pip install mysql-connector
	

> That we will be using in order to connectthe DB to our webapp.


___________________________________________________

> Let's update the "app.py" and import the module just installed

	import mysql.connector

>

	mysql_config = {
	
	    'user': '<username>',
	
	    'password': '<password>',
	
	    'host': 'localhost',
	
	    'database': '<name_of_DB>',
	
	}
	
	conn = mysql.connector.connect(**mysql_config)
	
	cursor = conn.cursor()

<br/>

- add "mysql_config" dictionary that will contain the credential details needed to connect to MySQL DB.
- We establish the connection using: `mysql.connector.connect(**mysql_config)`. The double asterisk `**` is used to unpack the dictionary and pass its key-value pairs as keyword arguments to the `connect` function.
- `cursor` is created to interact with the database using SQL queries.


______________________________________________________________________

>Let's then update the "contact_form"  route. 


#### And the integration of the DB is done! Everytime the form will be filled,  the datas will be automatically stored in MySQL DB in our localhost.
