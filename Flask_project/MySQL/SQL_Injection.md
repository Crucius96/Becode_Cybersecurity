# SQL Injection

> **SQL injection (SQLi)** 
 
 A web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. It generally allows an attacker to view data that they are not normally able to retrieve. This might include data belonging to other users, or any other data that the application itself is able to access. 
 **In many cases, an attacker can modify or delete this data, causing persistent changes to the application's content or behavior.**

<br/>
_______________________________________________________________________________

### Prevention of injections

Preventing SQL injection is crucial for the security of your applications and databases. 

To protect against SQL injection there are many ways, you can follow these best practices:


 **Parameterized Statements (Prepared Statements):**
    Use parameterized queries or prepared statements with bound parameters. This method ensures that the SQL statement and the user's input data are treated separately, preventing any direct manipulation of the SQL query. Most modern programming languages and frameworks provide support for parameterized statements.

**Error Handling:**
    Be cautious with error messages returned to users. Avoid displaying detailed error messages that might reveal sensitive information about your database structure. Instead, log errors securely for debugging purposes.


 **Input Validation:**
    Always validate and sanitize user input. Ensure that the input adheres to the expected format and doesn't contain any malicious characters. Use whitelisting or regular expressions to validate user input.


  **Use an ORM (Object-Relational Mapping):**
    Consider using an ORM that automatically handles SQL queries. ORM libraries help abstract the database interactions and can provide additional security against SQL injection.


  	Escaping User Input:
    If you can't use parameterized statements or stored procedures, escape user input properly before using it in an SQL query. Most programming languages offer functions or libraries to escape user input for SQL queries.
	 exp: **Sanitizing HTML:** This can be done using the `MarkupSafe.escape()` method. 


    Principle of Least Privilege:
    Ensure that the database user account used by your application has the least privilege necessary. This way, even if an SQL injection occurs, the attacker's access will be limited.
    In order to make your MySQL more secure, consider the following:

	- Only grant your users the privileges necessary to accomplish their tasks (e.g., don’t use GRANT ALL if that’s not necessary)
	    
	- Avoid running MySQL as "root" user because any user with the FILE privilege is able to cause the server to create files as root.
	- |File access on server host
	    
	- Consider running mysqld as an ordinary unprivileged user.
	    
	- Do not grant PROCESS or SUPER privileges to users who are not administrators. The PROCESS privilege allows the user to view all processes running in MySQL. 
	The SUPER privilege, among other things, enables server configuration changes, enables use of the CREATE SERVER, ALTER SERVER and DROP SERVER statements,and also enables use of the KILL statement letting the user kill statements belonging to other accounts. Bear in mind that MySQL reserves an extra connection for users who have the SUPER privilege. The SUPER privilege also lets a user control replication servers.


    Web Application Firewalls (WAF):
    Implement a Web Application Firewall to filter and monitor HTTP requests for suspicious patterns. A WAF can help detect and block potential SQL injection attempts.

	- Blacklists:  Blacklists are lists of known malicious IP addresses or domains. If the WAF sees a request from a blacklisted IP address or domain, it will block the request.


	- Whitelists:  Whitelists are lists of known safe IP addresses or domains. If the WAF sees a request from a whitelisted IP address or domain, it will allow the request.
    
    - Blocking malicious requests through "**Signature matching**" : Signature matching involves comparing the HTTP request to a list of known malicious patterns.

	- Alerting administrators to suspicious activity.

	- a WAF is not perfect. It is designed to prevent malicious requests from reaching your SQL database, but it is not foolproof. A clever attacker might be able to bypass the WAF and get access to your database.

	That is why it is important to implement other security measures, such as strong passwords and access controls, in addition to using a WAF.


Many more....

    Regular Updates and Patching:
    Keep your database management system and application frameworks up-to-date with the latest security patches to mitigate known vulnerabilities.


    Security Testing:
    Perform regular security testing, including penetration testing and code reviews, to identify and address potential vulnerabilities.
<br/>

___________________________________________________________________

### How to detect SQL injection vulnerabilities

The majority of SQL injection vulnerabilities can be found quickly and reliably using Burp Suite's [web vulnerability scanner](https://portswigger.net/burp/vulnerability-scanner).

SQL injection can be detected manually by using a systematic set of tests against every entry point in the application. This typically involves:

- Submitting the single quote character `'` and looking for errors or other anomalies.
- Submitting some SQL-specific syntax that evaluates to the base (original) value of the entry point, and to a different value, and looking for systematic differences in the resulting application responses.
- Submitting Boolean conditions such as `OR 1=1` and `OR 1=2`, and looking for differences in the application's responses.
- Submitting payloads designed to trigger time delays when executed within a SQL query, and looking for differences in the time taken to respond.
- Submitting [OAST](https://portswigger.net/burp/application-security-testing/oast) payloads designed to trigger an out-of-band network interaction when executed within a SQL query, and monitoring for any resulting interactions.