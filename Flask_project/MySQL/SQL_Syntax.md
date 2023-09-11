
# SELECT


Select query for a specific columns

`SELECT column, another_column, … FROM mytable;`

EXAMPLE:
SELECT * FROM Customers;


## SELECT DINSTINCT

The `SELECT DISTINCT` statement is used to return only distinct (different) values.

### SELECT DISTINCT Syntax

`SELECT DISTINCT _column1_, _column2, ..._`
`FROM _table_name_;`

## The SQL SELECT INTO Statement

The `SELECT INTO` statement copies data from one table into a new table.

### SELECT INTO Syntax

Copy all columns into a new table:

SELECT *  
INTO _newtable_ [IN _externaldb_]  
FROM _oldtable
WHERE _condition;

Copy only some columns into a new table:

SELECT _column1_, _column2_, _column3_, ...  
INTO _newtable_ [IN _externaldb_]  
FROM _oldtable  
WHERE _condition;

The new table will be created with the column-names and types as defined in the old table. You can create new column names using the `AS` clause.

### TIP: Selecting the last entry to view/modify the record

For this, you can use ORDER BY DESC LIMIT.

Query to select last record and update it :

`update DemoTable
`set Name='Robert'
`order by Id DESC limit 1;



---

#### SQL SELECT INTO Examples

- The following SQL statement creates a backup copy of Customers:

SELECT * INTO CustomersBackup2017  
FROM Customers;

- The following SQL statement uses the `IN` clause to copy the table into a new table in another database:

SELECT * INTO CustomersBackup2017 IN 'Backup.mdb'  
FROM Customers;

- The following SQL statement copies only a few columns into a new table:

SELECT CustomerName, ContactName INTO CustomersBackup2017  
FROM Customers;

- The following SQL statement copies only the German customers into a new table:

SELECT * INTO CustomersGermany  
FROM Customers  
WHERE Country = 'Germany';

- The following SQL statement copies data from more than one table into a new table:

SELECT Customers.CustomerName, Orders.OrderID  
INTO CustomersOrderBackup2017  
FROM Customers  
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

**Tip:** `SELECT INTO` can also be used to create a new, empty table using the schema of another. Just add a `WHERE` clause that causes the query to return no data:

SELECT * INTO _newtable_  
FROM _oldtable_  
WHERE 1 = 0;

# Queries with constraints

Select query with constraints

`SELECT column, another_column, … FROM mytable **WHERE _condition_ AND/OR _another_condition_ AND/OR …**;`

![[Pasted image 20230731160646.png]]

![[Pasted image 20230731160721.png]]

## The SQL WHERE Clause

The `WHERE` clause is used to filter records.

It is used to extract only those records that fulfill a specified condition.

### WHERE Syntax

`SELECT _column1_, _column2, ... 
`FROM _table_name_
`WHERE _condition_;

**Note:** The `WHERE` clause is not only used in `SELECT` statements, it is also used in `UPDATE`, `DELETE`, etc.!

## The SQL AND, OR and NOT Operators

The `WHERE` clause can be combined with `AND`, `OR`, and `NOT` operators.

### AND Syntax

`SELECT _column1_, _column2, ..._  
`FROM _table_name_  
`WHERE _condition1_ AND _condition2_ AND _condition3 ..._;

### OR Syntax

`SELECT _column1_, _column2, ..._  
`FROM _table_name_  
`WHERE _condition1_ OR _condition2_ OR _condition3 ..._;

### NOT Syntax

`SELECT _column1_, _column2, ..._  
`FROM _table_name_  
`WHERE NOT _condition_;

## The SQL ORDER BY Keyword

he `ORDER BY` keyword is used to sort the result-set in ascending or descending order.

The `ORDER BY` keyword sorts the records in ascending order by default. To sort the records in descending order, use the `DESC` keyword.

### ORDER BY Syntax

`SELECT _column1_, _column2, ..._  
`FROM _table_name_  
`ORDER BY _column1, column2, ..._ ASC|DESC;

## Limiting results to a subset

Another clause which is commonly used with the `ORDER BY` clause are the `LIMIT` and `OFFSET` clauses, which are a useful optimization to indicate to the database the subset of the results you care about.  
The `LIMIT` will reduce the number of rows to return, and the optional `OFFSET` will specify where to begin counting the number rows from.

Select query with limited rows:

`SELECT column, another_column, … FROM mytable WHERE _condition(s)_ ORDER BY column ASC/DESC **LIMIT num_limit OFFSET num_offset**;`


# Multi-table queries with JOINs

## Inner Join

Tables that share information about a single entity need to have a _primary key_ that identifies that entity _uniquely_ across the database. One common primary key type is an auto-incrementing integer (because they are space efficient), but it can also be a string, hashed value, so long as it is unique.

Using the `JOIN` clause in a query, we can combine row data across two separate tables using this unique key. The first of the joins that we will introduce is the `INNER JOIN`.

Select query with INNER JOIN on multiple tables

`SELECT column, another_table_column, … FROM mytable **INNER JOIN another_table ON mytable.id = another_table.id** WHERE _condition(s)_ ORDER BY column, … ASC/DESC LIMIT num_limit OFFSET num_offset;`

The `INNER JOIN` is a process that matches rows from the first table and the second table which have the same key (as defined by the `ON` constraint) to create a result row with the combined columns from both tables.

![[Pasted image 20230731163630.png]]

## LEFT JOIN

The `LEFT JOIN` keyword returns all records from the left table (table1), and the matching records from the right table (table2). The result is 0 records from the right side, if there is no match.

### LEFT JOIN Syntax

SELECT _column_name(s)_  
FROM _table1_  
LEFT JOIN _table2  
ON _table1.column_name_ = _table2.column_name_;

![[Pasted image 20230731163758.png]]

### RIGHT JOIN Syntax

The `RIGHT JOIN` keyword returns all records from the right table (table2), and the matching records from the left table (table1). The result is 0 records from the left side, if there is no match.

### RIGHT JOIN Syntax

SELECT _column_name(s)_  
FROM _table1_  
RIGHT JOIN _table2  
ON _table1.column_name_ = _table2.column_name_;

![[Pasted image 20230731163836.png]]

## SQL FULL OUTER JOIN Keyword

The `FULL OUTER JOIN` keyword returns all records when there is a match in left (table1) or right (table2) table records.

**Tip:** `FULL OUTER JOIN` and `FULL JOIN` are the same.

### FULL OUTER JOIN Syntax

SELECT _column_name(s)_  
FROM _table1_  
FULL OUTER JOIN _table2  
ON _table1.column_name_ = _table2.column_name_WHERE _condition_;

![[Pasted image 20230731163946.png]]

## JOINS SUMMARY

Like the `INNER JOIN` these three new joins have to specify which column to join the data on.  
When joining table A to table B, a `LEFT JOIN` simply includes rows from A regardless of whether a matching row is found in B. The `RIGHT JOIN` is the same, but reversed, keeping rows in B regardless of whether a match is found in A. Finally, a `FULL JOIN` simply means that rows from both tables are kept, regardless of whether a matching row exists in the other table.

When using any of these new joins, you will likely have to write additional logic to deal with `NULL`s in the result and constraints.


# UNION

## The SQL UNION Operator

The `UNION` operator is used to combine the result-set of two or more `SELECT` statements.

- Every `SELECT` statement within `UNION` must have the same number of columns
- The columns must also have similar data types
- The columns in every `SELECT` statement must also be in the same order

### UNION Syntax

SELECT _column_name(s)_ FROM _table1_  
UNION  
SELECT _column_name(s)_ FROM _table2_;

### UNION ALL Syntax

The `UNION` operator selects only distinct values by default. To allow duplicate values, use `UNION ALL`:

SELECT _column_name(s)_ FROM _table1_  
UNION ALL  
SELECT _column_name(s)_ FROM _table2_;

**Note:** The column names in the result-set are usually equal to the column names in the first `SELECT` statement.

## SQL UNION With WHERE

The following SQL statement returns the German cities (only distinct values) from both the "Customers" and the "Suppliers" table:

### Example

SELECT City, Country FROM Customers  
WHERE Country='Germany'  
UNION  
SELECT City, Country FROM Suppliers  
WHERE Country='Germany'  
ORDER BY City;

## SQL UNION ALL With WHERE

The following SQL statement returns the German cities (duplicate values also) from both the "Customers" and the "Suppliers" table:

### Example

SELECT City, Country FROM Customers  
WHERE Country='Germany'  
UNION ALL  
SELECT City, Country FROM Suppliers  
WHERE Country='Germany'  
ORDER BY City;

## Another UNION Example

The following SQL statement lists all customers and suppliers:

### Example

SELECT 'Customer' AS Type, ContactName, City, Country  
FROM Customers  
UNION  
SELECT 'Supplier', ContactName, City, Country  
FROM Suppliers;

Notice the "AS Type" above - it is an alias. [SQL Aliases](https://www.w3schools.com/sql/sql_alias.asp) are used to give a table or a column a temporary name. An alias only exists for the duration of the query. So, here we have created a temporary column named "Type", that list whether the contact person is a "Customer" or a "Supplier".

# SQL NULL Values

## How to Test for NULL Values?

It is not possible to test for NULL values with comparison operators, such as =, <, or <>.

We will have to use the `IS NULL` and `IS NOT NULL` operators instead.

### IS NULL Syntax

SELECT _column_names  
_FROM _table_name_  
WHERE _column_name_ IS NULL;

### IS NOT NULL Syntax

SELECT _column_names  
_FROM _table_name_  
WHERE _column_name_ IS NOT NULL;


# SQL Aliases

SQL aliases are used to give a table, or a column in a table, a temporary name.

Aliases are often used to make column names more readable.

An alias only exists for the duration of that query.

An alias is created with the `AS` keyword.

### Alias Column Syntax

SELECT _column_name_ AS _alias_name_  
FROM _table_name;_

### Alias Table Syntax

SELECT _column_name(s)_  
FROM _table_name_ AS _alias_name;

# SQL FUNCTIONS

## The SQL MIN() and MAX() Functions

The `MIN()` function returns the smallest value of the selected column.

The `MAX()` function returns the largest value of the selected column.

### MIN() Syntax

SELECT MIN(_column_name_)  
FROM _table_name_  
WHERE _condition_;

### MAX() Syntax

SELECT MAX(_column_name_)  
FROM _table_name_  
WHERE _condition_;

### SQL COUNT()

The `COUNT()` function returns the number of rows that matches a specified criterion.

SELECT COUNT(_column_name_)  
FROM _table_name_  
WHERE _condition_;

The `AVG()` function returns the average value of a numeric column. 

### AVG() Syntax

SELECT AVG(_column_name_)  
FROM _table_name_  
WHERE _condition_;

The `SUM()` function returns the total sum of a numeric column. 

### SUM() Syntax

SELECT SUM(_column_name_)  
FROM _table_name_  
WHERE _condition_;

# SQL GROUP BY Statement

## The SQL GROUP BY Statement

The `GROUP BY` statement groups rows that have the same values into summary rows, like "find the number of customers in each country".

The `GROUP BY` statement is often used with aggregate functions (`COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()`) to group the result-set by one or more columns.

### GROUP BY Syntax

SELECT _column_name(s)_  
FROM _table_name_  
WHERE _condition_  
GROUP BY _column_name(s)  
ORDER BY _column_name(s);

## The SQL HAVING Clause

The `HAVING` clause was added to SQL because the `WHERE` keyword cannot be used with aggregate functions.

### HAVING Syntax

SELECT _column_name(s)_  
FROM _table_name_  
WHERE _condition_  
GROUP BY _column_name(s)  
HAVING _condition  
ORDER BY _column_name(s);


# Using SQL Variables in Queries

## Problem

You want to save a value from a query so you can refer to it in a subsequent query.

## Solution

Use a SQL variable to store the value for later use.

## Discussion

As of MySQL 3.23.6, you can assign a value returned by a `SELECT` statement to a variable, then refer to the variable later in your **mysql** session. This provides a way to save a result returned from one query, then refer to it later in other queries. The syntax for assigning a value to a SQL variable within a `SELECT` query is `@`_`var_name`_ `:=` _`value`_, where _`var_name`_ is the variable name and _`value`_ is a value that you’re retrieving. The variable may be used in subsequent queries wherever an expression is allowed, such as in a `WHERE` clause or in an `INSERT` statement.

A common situation in which SQL variables come in handy is when you need to issue successive queries on multiple tables that are related by a common key value. Suppose you have a `customers` table with a `cust_id` column that identifies each customer, and an `orders` table that also has a `cust_id` column to indicate which customer each order is associated with. If you have a customer name and you want to delete the customer record as well as all the customer’s orders, you need to determine the proper `cust_id` value for that customer, then delete records from both the `customers` and `orders` tables that match the ID. One way to do this is to first save the ID value in a variable, then refer to the variable in the `DELETE` statements:

mysql> **`SELECT @id := cust_id FROM customers WHERE cust_id='`**_`customer name`_**`';`**
mysql> **`DELETE FROM customers WHERE cust_id = @id;`**
mysql> **`DELETE FROM orders WHERE cust_id = @id;`**
# Order of Execution of a Query

## 1. `FROM` and `JOIN`s

The `FROM` clause, and subsequent `JOIN`s are first executed to determine the total working set of data that is being queried. This includes subqueries in this clause, and can cause temporary tables to be created under the hood containing all the columns and rows of the tables being joined.

## 2. `WHERE`

Once we have the total working set of data, the first-pass `WHERE` constraints are applied to the individual rows, and rows that do not satisfy the constraint are discarded. Each of the constraints can only access columns directly from the tables requested in the `FROM` clause. Aliases in the `SELECT` part of the query are not accessible in most databases since they may include expressions dependent on parts of the query that have not yet executed.

## 3. `GROUP BY`

The remaining rows after the `WHERE` constraints are applied are then grouped based on common values in the column specified in the `GROUP BY` clause. As a result of the grouping, there will only be as many rows as there are unique values in that column. Implicitly, this means that you should only need to use this when you have aggregate functions in your query.

## 4. `HAVING`

If the query has a `GROUP BY` clause, then the constraints in the `HAVING` clause are then applied to the grouped rows, discard the grouped rows that don't satisfy the constraint. Like the `WHERE` clause, aliases are also not accessible from this step in most databases.

## 5. `SELECT`

Any expressions in the `SELECT` part of the query are finally computed.

## 6. `DISTINCT`

Of the remaining rows, rows with duplicate values in the column marked as `DISTINCT` will be discarded.

## 7. `ORDER BY`

If an order is specified by the `ORDER BY` clause, the rows are then sorted by the specified data in either ascending or descending order. Since all the expressions in the `SELECT` part of the query have been computed, you can reference aliases in this clause.

## 8. `LIMIT` / `OFFSET`

Finally, the rows that fall outside the range specified by the `LIMIT` and `OFFSET` are discarded, leaving the final set of rows to be returned from the query.

# SQL INSERT INTO SELECT

When inserting data into a database, we need to use an `INSERT` statement, which declares which table to write into, the columns of data that we are filling, and one or more rows of data to insert. In general, each row of data you insert should contain values for every corresponding column in the table. You can insert multiple rows at a time by just listing them sequentially.

Insert statement with values for all columns

`INSERT INTO mytable VALUES (value_or_expr, another_value_or_expr, …), (value_or_expr_2, another_value_or_expr_2, …), …;`

In some cases, if you have incomplete data and the table contains columns that support default values, you can insert rows with only the columns of data you have by specifying them explicitly.

Insert statement with specific columns

`INSERT INTO mytable **(column, another_column, …)** VALUES (value_or_expr, another_value_or_expr, …), (value_or_expr_2, another_value_or_expr_2, …), …;`

In these cases, the number of values need to match the number of columns specified. Despite this being a more verbose statement to write, inserting values this way has the benefit of being forward compatible. For example, if you add a new column to the table with a default value, no hardcoded `INSERT` statements will have to change as a result to accommodate that change.

In addition, you can use mathematical and string expressions with the values that you are inserting.  
This can be useful to ensure that all data inserted is formatted a certain way.

Example Insert statement with expressions

`INSERT INTO boxoffice **(movie_id, rating, sales_in_millions)** VALUES (1, 9.9, 283742034 / 1000000);`

### Examples

1. The following SQL statement copies "Suppliers" into "Customers" (the columns that are not filled with data, will contain NULL):

INSERT INTO Customers (CustomerName, City, Country) SELECT SupplierName, City, Country FROM Suppliers;

2.  The following SQL statement copies "Suppliers" into "Customers" (fill all columns):

INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)  
SELECT SupplierName, ContactName, Address, City, PostalCode, Country FROM Suppliers;

3. The following SQL statement copies only the German suppliers into "Customers":

INSERT INTO Customers (CustomerName, City, Country) 
SELECT SupplierName, City, Country FROM Suppliers  
WHERE Country='Germany';

# SQL UPDATE

In addition to adding new data, a common task is to update existing data, which can be done using an `UPDATE` statement. Similar to the `INSERT` statement, you have to specify exactly which table, columns, and rows to update. In addition, the data you are updating has to match the data type of the columns in the table schema.

Update statement with values

`UPDATE mytable SET column = value_or_expr, other_column = another_value_or_expr, … WHERE condition;`

The statement works by taking multiple column/value pairs, and applying those changes to each and every row that satisfies the constraint in the `WHERE` clause.

### Example

The following SQL statement updates the first customer (CustomerID = 1) with a new contact person _and_ a new city.

UPDATE Customers  
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'  
WHERE CustomerID = 1;

### Warning

Most people working with SQL **will** make mistakes updating data at one point or another. Whether it's updating the wrong set of rows in a production database, or accidentally leaving out the `WHERE` clause (which causes the update to apply to _all_ rows), you need to be extra careful when constructing `UPDATE` statements.

One helpful tip is to always write the constraint first and test it in a `SELECT` query to make sure you are updating the right rows, and only then writing the column/value pairs to update.

# The SQL DELETE Statement

When you need to delete data from a table in the database, you can use a `DELETE` statement, which describes the table to act on, and the rows of the table to delete through the `WHERE` clause.

Delete statement with condition

`DELETE FROM mytable WHERE condition;`

If you decide to leave out the `WHERE` constraint, then _all_ rows are removed, which is a quick and easy way to clear out a table completely (if intentional).

# SQL CREATE TABLE Statement

When you have new entities and relationships to store in your database, you can create a new database table using the `CREATE TABLE` statement.

Create table statement w/ optional table constraint and default value

`CREATE TABLE IF NOT EXISTS mytable ( column _DataType_ _TableConstraint_ DEFAULT _default_value_, another_column _DataType_ _TableConstraint_ DEFAULT _default_value_, … );`

The structure of the new table is defined by its _table schema_, which defines a series of columns. Each column has a name, the type of data allowed in that column, an _optional_ table constraint on values being inserted, and an optional default value.

If there already exists a table with the same name, the SQL implementation will usually throw an error, so to suppress the error and skip creating a table if one exists, you can use the `IF NOT EXISTS` clause.

### Example

The following example creates a table called "Persons" that contains five columns: PersonID, LastName, FirstName, Address, and City:

CREATE TABLE Persons (  
    PersonID int,  
    LastName varchar(255),  
    FirstName varchar(255),  
    Address varchar(255),  
    City varchar(255)  
);

The PersonID column is of type int and will hold an integer.

The LastName, FirstName, Address, and City columns are of type varchar and will hold characters, and the maximum length for these fields is 255 characters.

## Create Table Using Another Table

A copy of an existing table can also be created using `CREATE TABLE`.

The new table gets the same column definitions. All columns or specific columns can be selected.

If you create a new table using an existing table, the new table will be filled with the existing values from the old table.

### Syntax

CREATE TABLE _new_table_name_ AS  
    SELECT _column1, column2,..._  
    FROM _existing_table_name_  
    WHERE ....;

The following SQL creates a new table called "TestTables" (which is a copy of the "Customers" table): 

### Example

CREATE TABLE TestTable AS  
SELECT customername, contactname  
FROM customers;

### Table Data Types

|   |   |
|---|---|
|Data type|Description|
|`INTEGER`, `BOOLEAN`|The integer datatypes can store whole integer values like the count of a number or an age. In some implementations, the boolean value is just represented as an integer value of just 0 or 1.|
|`FLOAT`, `DOUBLE`, `REAL`|The floating point datatypes can store more precise numerical data like measurements or fractional values. Different types can be used depending on the floating point precision required for that value.|
|`CHARACTER(num_chars)`, `VARCHAR(num_chars)`, `TEXT`|The text based datatypes can store strings and text in all sorts of locales. The distinction between the various types generally amount to underlaying efficiency of the database when working with these columns.<br><br>Both the CHARACTER and VARCHAR (variable character) types are specified with the max number of characters that they can store (longer values may be truncated), so can be more efficient to store and query with big tables.|
|`DATE`, `DATETIME`|SQL can also store date and time stamps to keep track of time series and event data. They can be tricky to work with especially when manipulating data across timezones.|
|`BLOB`|Finally, SQL can store binary data in blobs right in the database. These values are often opaque to the database, so you usually have to store them with the right metadata to requery them.|

## Table Constraints

|   |   |
|---|---|
|Constraint|Description|
|`PRIMARY KEY`|This means that the values in this column are unique, and each value can be used to identify a single row in this table.|
|`AUTOINCREMENT`|For integer values, this means that the value is automatically filled in and incremented with each row insertion. Not supported in all databases.|
|`UNIQUE`|This means that the values in this column have to be unique, so you can't insert another row with the same value in this column as another row in the table. Differs from the `PRIMARY KEY` in that it doesn't have to be a key for a row in the table.|
|`NOT NULL`|This means that the inserted value can not be `NULL`.|
|`CHECK (expression)`|This allows you to run a more complex expression to test whether the values inserted are valid. For example, you can check that values are positive, or greater than a specific size, or start with a certain prefix, etc.|
|`FOREIGN KEY`|This is a consistency check which ensures that each value in this column corresponds to another value in a column in another table.  <br>  <br>For example, if there are two tables, one listing all Employees by ID, and another listing their payroll information, the `FOREIGN KEY` can ensure that every row in the payroll table corresponds to a valid employee in the master Employee list.|

# SQL ALTER TABLE Statement

## Adding columns (ADD)

The syntax for adding a new column is similar to the syntax when creating new rows in the `CREATE TABLE` statement. You need to specify the data type of the column along with any potential table constraints and default values to be applied to both existing _and_ new rows. In some databases like MySQL, you can even specify where to insert the new column using the `FIRST` or `AFTER` clauses, though this is not a standard feature.

Altering table to add new column(s)

`ALTER TABLE mytable
`ADD column _DataType OptionalTableConstraint_ DEFAULT default_value;`

### Example

The following SQL adds an "Email" column to the "Customers" table:

ALTER TABLE Customers  
ADD Email varchar(255);

## RENAME COLUMN

To rename a column in a table, use the following syntax:

ALTER TABLE _table_name_  
RENAME COLUMN _old_name_ to _new_name_;

## REMOVING COLUMNS (DROP)

Dropping columns is as easy as specifying the column to drop, however, some databases (including SQLite) don't support this feature. Instead you may have to create a new table and migrate the data over.

Altering table to remove column(s)

`ALTER TABLE mytable
`DROP column_to_be_deleted;`

### Example

The following SQL deletes the "Email" column from the "Customers" table:

ALTER TABLE Customers  
DROP COLUMN Email;
## Renaming the table (RENAME TO)

If you need to rename the table itself, you can also do that using the `RENAME TO` clause of the statement.

Altering table name

`ALTER TABLE mytable 
`RENAME TO new_table_name;`

# The SQL DROP TABLE Statement

The `DROP TABLE` statement is used to drop an existing table in a database.

### Syntax

DROP TABLE _table_name_;

Additionally:

`DROP TABLE IF EXISTS mytable;`

Like the `CREATE TABLE` statement, the database may throw an error if the specified table does not exist, and to suppress that error, you can use the `IF EXISTS` clause.

In addition, if you have another table that is dependent on columns in table you are removing (for example, with a `FOREIGN KEY` dependency) then you will have to either update all dependent tables first to remove the dependent rows or to remove those tables entirely.
# ALTER COLUMN DATATYPE

The `ALTER COLUMN` command is used to change the data type of a column in a table.

The following SQL changes the data type of the column named "BirthDate" in the "Employees" table to type year:

#### Example

`ALTER TABLE Employees  
`ALTER COLUMN BirthDate year;

#### Other syntaxes

**SQL Server / MS Access:**

ALTER TABLE _table_name_  
ALTER COLUMN _column_name datatype_;

**My SQL / Oracle (prior version 10G):**

ALTER TABLE _table_name_  
MODIFY COLUMN _column_name datatype_;

**Oracle 10G and later:**

ALTER TABLE _table_name_  
MODIFY _column_name datatype_;