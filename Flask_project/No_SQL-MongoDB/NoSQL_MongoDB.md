> Essentially same concept of SQL but different approach. Instead of having a Schema in our DataBase (with table and different types of data), all our data will be within a DATABASE that inside contains a COLLECTION, lastly 
> this contains our mix of datas.

Find [video tutorial here](https://www.youtube.com/watch?v=XF1_MlZ5l6M)

DATABASE --->  COLLECTION --->    DATA.

1. Language used is JavaScript. 
2. The data inside the Collections are in JSON format.

______________________________________

### JSON (JavaScript Object Notation)

> A file format widely used because easy for both humans to read and write and for machines to parse and generate. It is often used for transmitting data between a server and a web application, as well as for configuration files and data storage. JSON is language-agnostic, which means it can be used with many programming languages.

Basic Commands:
### To create a database

we will just use the command "use" and then the name of the db, if not existing, it will automatically create once we will insert some data on it.

	use "name_db"

<br/>

Then we will add the name of the COLLECTION (aka a Table):

	name_db> db.name_collection.insertOne()

in every query, we recall "db" to tell that query is to actual db.
Then we type the name of the collection, if not existing it will then be created automatically.

<br/>

> Then we type the function we want to query: 
> INSERT - FIND - UPDATE - REPLACE - DELETE


______________________________

### To insert data
 
	db.name_collection.insertOne()   or  db.name_collection.insertMany()

InsertOne = is used to insert data in the collection, but a singular data (with its attributes if present, exp. name: Alan, then [age, city, address, country] these are attributes. )

InsertMany = is used insert multiple data in a single query.

______________________________

### To Find data

We simply recall the function `.find()`  and insert inside the bracket the parameters/properties we need. 

```
db.name_collection.find()
```

With Find function can be also requested complex queries.

<br/>

______________________________

#### To Update 

> updateOne()    or   updateMany()


```
db.name_collection.updateOne()

db.name_collection.updateOne({age: 26}, {$set: { age: 27 } })
```

So what we did is to update one data.
We first call the parameter to update (age: 26), then used the     `$set`     to  tell Mongo to change the it to the following parameter (age: 27).

>NOTE: the use of   " $ "  is essential in NoSQL queries.   " $  "  can be followed by different operators:  set   -  inc(increment)  -  rename   -  unset (completely remove a property)    -    push (to add a property)   -    pull  --


______________________________

### To Replace

> replaceOne()  

Almost same as Update function, but insted of replacing/updating one property only, it will change the whole property of the recalled data.

We will want to use Replace function only if we want to wipe the whole property of a data and replace it with something new.


_______________________________________

### To Delete

>    deleteOne()   or deleteMany()


To delete a data in a collection.
