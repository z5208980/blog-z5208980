---
title: "MongoDB Python Developer Path Notes"
date: "2023-05-19"
tags: ["Developer", "Azure"]
image: ""
gradients: ["#70F570", "#49C628"]
---


## Using MongoDB in Python: A Quick Guide
**MongoDB**, a popular **NoSQL database**, offers great flexibility and scalability for storing and managing data. In this blog post, we will explore how to use MongoDB with *Python*, from establishing a connection to performing basic operations.

Connecting with Python
To start working with MongoDB in Python, we first need to establish a connection to the MongoDB server. This can be done using the `pymongo` library, which provides a Python interface for MongoDB. Assuming you have the pymongo library installed, you can connect to MongoDB using the following code:

```py
from pymongo import MongoClient

client = MongoClient(MONGO_URI) # connects to the MongoDB client
```

In the code above, `MONGO_URI` represents the connection string for your MongoDB instance. Once the connection is established, we can proceed to interact with the databases and collections.

### Interacting with Databases and Collections
After connecting to the MongoDB client, we can specify the **database** and **collection** we want to work with. Here's an example of how to connect to a database and collection:
```py
db = client.blog  # connects to the "blog" database
collection = db.post  # connects to the "post" collection in the "blog" database
```

To verify the available **databases**, you can use the `list_database_names()` method:
```py
for db_name in client.list_database_names():
    print(db_name)
```

Similarly, to view the **collections** within a database, you can use the list_collection_names() method:
```py
for col_name in db.list_collection_names():
    print(col_name)
```
These methods allow you to explore the existing **databases and collections**, enabling you to interact with specific datasets.

### Inserting Data
To insert data into a MongoDB database, we can use the insertOne() and insertMany() methods. Let's see how to do this using both the ATLAS CLI and Python.

**CLI**
To insert a single document using the ATLAS CLI, we can use the insertOne() method. Here's an example:

```bash
db.accounts.insertOne({name: "John", age: 25, status: "A"})
```
If we want to insert multiple documents at once, we can use the insertMany() method. Here's an example:

```bash
db.accounts.insertMany([{name: "John", age: 25, status: "A"}, {name: "John", age: 25, status: "A"}])
```

**Python**
In Python, we need to use the PyMongo library to interact with MongoDB. Here's an example of inserting data into MongoDB using PyMongo:

```py
collection.insert_one({"name": "John", "age": 25, "status": "A"})

collection.insert_many([
    {"name": "John", "age": 25, "status": "A"},
    {"name": "John", "age": 25, "status": "A"}
])
```

### Basic Queries
To perform basic queries in MongoDB, we can use the find() method. Here are some examples:

**Find documents by a specific value**
To find documents where the name is "John", we can use the following query:

```bash
db.accounts.find({name: "John"})
```
Find documents with multiple values using `$in`
To find documents where the name is either "John" or "Jane", we can use the $in operator:

```bash
db.accounts.find({name: {$in: ["John", "Jane"]}})
```
Find documents with an exact value using $eq
To find documents where the name is exactly "John", we can use the $eq operator:

```bash
db.accounts.find({name: {$eq: "John"}})
```

**Comparison Operators**
MongoDB provides various comparison operators to query data based on conditions. Here are some examples:

- **Greater than ($gt)**
To find documents where the age is greater than 25, we can use the $gt operator:

```bash
db.accounts.find({age: {$gt: 25}})
```

- **Greater than or equal to ($gte)**
To find documents where the age is greater than or equal to 25, we can use the `$gte` operator:

```bash
db.accounts.find({age: {$gte: 25}})
```

- **Less than ($lt)**
To find documents where the age is less than 25, we can use the `$lt` operator:

```bash
db.accounts.find({age: {$lt: 25}})
```

- **Less than or equal to ($lte)**
To find documents where the age is less than or equal to 25, we can use the `$lte` operator:

```bash
db.accounts.find({age: {$lte: 25}})
```

### Array Queries
If a property is an array, we can use specific operators to query array elements. Here are some examples:

- **Match documents containing the entire array ($all)**
To find documents where the name array contains both "John" and "Jane", we can use the `$all` operator:

bash
Copy code
db.accounts.find({name: {$all: ["John", "Jane"]}})
Match array elements using $elemMatch
To find documents where the name array contains the exact element "John", we can use the $elemMatch operator:

```bash
db.accounts.find({name: {$elemMatch: {$eq: "John"}}})
```

### Logical Operators
MongoDB supports logical operators to combine multiple conditions. Here are some examples:

- **Logical OR ($or)**
To find documents where either the name is "John" or the age is 25, we can use the `$or` operator:

```bash
db.accounts.find({$or: [{name: "John"}, {age: 25}]})
```

- ** Logical AND ($and)**
To find documents where both the name is "John" and the age is 25, we can use the `$and` operator:

```bash
db.accounts.find({$and: [{name: "John"}, {age: 25}]})
```

These query operations provide powerful capabilities to retrieve specific data from MongoDB *based on various conditions.* Experiment with these queries to efficiently **retrieve the data** you need from your MongoDB collections.

### Replace Operations
To replace a document in MongoDB, we can use the replaceOne() method. This operation replaces the entire document with the specified replacement document. Here's an example:

```bash
db.accounts.replaceOne({_id: ObjectId("...")}, {name: "John", age: 25, status: "A"})
```
In this example, we replace the document with the specified `_id` with a new document containing the updated values for the name, age, and status fields.

Alternatively, we can use the `updateOne()` method to achieve the same result:

```bash
db.accounts.updateOne({_id: ObjectId("...")}, {$set: {name: "John", age: 25, status: "A"}})
```
The `$set` operator allows us to update specific fields within the document while leaving other fields unchanged.

If you want to perform an upsert operation, which updates the document if it exists or inserts it if it doesn't, you can use the `updateOne()` method with the upsert: true option:

```bash
db.accounts.updateOne({_id: ObjectId("...")}, {$set: {name: "John", age: 25, status: "A"}}, {upsert: true})
```

- **Find and Modify**
The `findAndModify()` method is another option for updating documents. It updates the document and returns the old version of the document as the result. Here's an example:

```bash
db.accounts.findAndModify({query: {_id: ObjectId("...")}, update: {$set: {name: "John", age: 25, status: "A"}}})
```
- **Update Many**
To update multiple documents that match a query, we can use the `updateMany()` method. This operation allows us to update multiple documents with the same set of changes. Here's an example:

```bash
db.accounts.updateMany({name: "John"}, {$set: {name: "John", age: 25, status: "A"}})
In this example, we update all documents where the name field is "John" with the new values for the name, age, and status fields.

### Delete Operations
To delete documents in MongoDB, we can use the `deleteOne()` and `deleteMany()` methods. Here are some examples:

- **Delete One**
To delete the first document that matches a query, we can use the deleteOne() method:

```bash
db.accounts.deleteOne({_id: ObjectId("...")})
```

In this example, we delete the document with the specified `_id`.

- **Delete Many**
To delete multiple documents that match a query, we can use the deleteMany() method:

```bash
db.accounts.deleteMany({name: "John"})
```

In this example, we delete all documents where the name field is "John".

These replace and delete operations provide powerful capabilities for modifying and removing data in MongoDB collections. Use them carefully to ensure data integrity and consistency in your database.

### Sorting Data
To sort documents in MongoDB, we can use the sort() method. This method allows us to specify the field to sort by and the sort order. Here are some examples:

- **Sort in ascending order**
To sort documents in ascending order by the name field, we can use the following query:

```bash
db.accounts.find().sort({name: 1})
```
The value **1 represents ascendin**g order.

- **Sort in descending order**
To sort documents in descending order by the name field, we can use the following query:

```bash
db.accounts.find().sort({name: -1})
```
The value **-1 represents descending** order.

- **Sort with additional filters**
We can also combine sorting with additional filters to further refine our query. Here's an example of sorting documents by the name field and filtering for documents where the name is "John":

```bash
db.accounts.find({name: "John"}).sort({name: 1})
```

- **Limiting Results**
To limit the number of documents returned in a query, we can use the `limit()` method. This method restricts the result set to a specified number of documents. Here's an example:

```bash
db.accounts.find().sort({name: -1}).limit(10)
```
This query will sort the documents in descending order by the name field and limit the result set to only the top 10 documents.

### Projection - Returning Specific Fields
Projection allows us to specify which fields to include or exclude in the returned documents. We can use the **second argument **of the `find()` method to define the projection. Here's an example:

```bash
db.accounts.find({age: {$lt: 18}}, {name: 1, age: 1, status: 1})
```

In this example, we only include the name, age, and status fields in the returned documents. The value **1 indicates the field is included**.

- **Counting Documents**
To count the number of documents that match a query, we can use the `count()` or `countDocuments()` method. Here are the examples:

```bash
db.accounts.find({age: {$lt: 18}}).count()
```
This query will return the count of documents where the age is less than 18.

```bash
db.accounts.find({age: {$lt: 18}}).countDocuments()
```
The `countDocuments()` method is recommended over `count()` as it provides more accurate results and better performance.

These sorting and filtering operations allow us to retrieve and manipulate data in MongoDB based on specific criteria. Experiment with these operations to efficiently retrieve and organize your data as per your requirements.
## CRUD Operations in Python with MongoDB
To perform CRUD (Create, Read, Update, Delete) operations in Python with MongoDB, we can use the **PyMongo** library. Here's how you can perform each operation:

### Create (Insert) Documents
To insert a single document into a MongoDB collection, we can use the insert_one() method. It returns an InsertOneResult object containing information about the insertion. Here's an example:

```py
result = collection.insert_one({"name": "John", "age": 25, "status": "A"})
document_id = result.inserted_id
```
To insert multiple documents into a collection, we can use the `insert_many()` method. It accepts a list of documents to insert. Here's an example:

```py
collection.insert_many([
    {"name": "John", "age": 25, "status": "A"},
    {"name": "John", "age": 25, "status": "A"}
])
```

### Read (Query) Documents
To retrieve a single document that matches a query, we can use the find_one() method. It returns the first document that matches the query criteria. Here's an example:

```py
document = collection.find_one({"author": "author"})
```

To retrieve multiple documents that match a query, we can use the `find()` method. It returns a cursor object that we can iterate over to access the matched documents. Here's an example:

```py
cursor = collection.find({"author": "author"})

for document in cursor:
    print(document)
```

### Update Documents
To update a single document, we can use the `update_one()` method. It updates the first document that matches the query with the specified update operation. Here's an example:

```py
from bson.objectid import ObjectId

result = collection.update_one(
    {"_id": ObjectId("646741e888610f136ee64ced")},
    {"$inc": {"likes": 1}}
)
```

**Note**: We need to import bson packages to use `ObjectId`
``` 
from bson.objectid import ObjectId
```

To update multiple documents, we can use the `update_many()` method. It updates all documents that match the query with the specified update operation. Here's an example:

```py
result = collection.update_many(
    {"author": "Ricardo"},
    {"$inc": {"likes": 1}}
)
```

### Delete Documents
To delete a single document, we can use the `delete_one()` method. It removes the first document that matches the query criteria. Here's an example:

```py
result = collection.delete_one({"_id": ObjectId("646741e888610f136ee64ced")})
```
To delete multiple documents, we can use the `delete_many()` method. It removes all documents that match the query criteria. Here's an example:

```py
result = collection.delete_many({"author": "Ricardo"})
```

These examples demonstrate how to perform CRUD operations using PyMongo in Python. Modify the queries and documents based on your specific use case and requirements.

## Transaction Handling in MongoDB
In MongoDB, transactions provide a way to perform multiple operations as a single atomic unit of work. This ensures data **integrity and consistency**, allowing you to maintain the correctness of your data even in the presence of **concurrent operations**. Let's explore how transactions work in MongoDB using an example.

### What is a Transaction?
A transaction is a sequence of operations that are executed as a **single unit**. In MongoDB, transactions are performed on a session, and they guarantee that either all the operations within the transaction are applied or none of them are.

### Starting a Transaction
To start a transaction in MongoDB, we can use the `with_transaction` method within a client session. Here's an example:

```py
from pymongo import MongoClient

# Connect to the MongoDB cluster
client = MongoClient(MONGODB_URI)

# Define the callback that specifies the sequence of operations to perform inside the transaction
def callback(session, transfer_id=None, account_id_receiver=None, account_id_sender=None, transfer_amount=None):
    # Get references to collections
    accounts_collection = session.client.bank.accounts
    transfers_collection = session.client.bank.transfers

    # Create a transfer document
    transfer = {
        "transfer_id": transfer_id,
        "to_account": account_id_receiver,
        "from_account": account_id_sender,
        "amount": {"$numberDecimal": transfer_amount},
    }

    # Transaction operations
    # Update sender account: subtract transfer amount from balance and add transfer ID
    accounts_collection.update_one(
        {"account_id": account_id_sender},
        {
            "$inc": {"balance": -transfer_amount},
            "$push": {"transfers_complete": transfer_id},
        },
        session=session,
    )

    # Update receiver account: add transfer amount to balance and add transfer ID
    accounts_collection.update_one(
        {"account_id": account_id_receiver},
        {
            "$inc": {"balance": transfer_amount},
            "$push": {"transfers_complete": transfer_id},
        },
        session=session,
    )

    # Add new transfer to 'transfers' collection
    transfers_collection.insert_one(transfer, session=session)

    print("Transaction successful")

# Start a client session
with client.start_session() as session:
    # Use with_transaction to start a transaction, execute the callback, and commit (or cancel on error)
    session.with_transaction(
        callback,
        transfer_id="TR218721873",
        account_id_receiver="MDB343652528",
        account_id_sender="MDB574189300",
        transfer_amount=100,
    )

# Close the client connection
client.close()
```

In the example above, we define a **callback function** that specifies the sequence of operations to be executed within the transaction. The operations involve updating the sender and receiver accounts, as well as inserting a new transfer document into the transfers collection. The transaction is started using `session.with_transaction()`, passing the callback function and the **required parameters**.

If all operations within the transaction are successfully executed, the changes will be committed. Otherwise, if an error occurs, the transaction will be canceled, and all changes will be rolled back.

### Transaction Time Limit
It's important to note that a transaction should complete within a certain time limit. In MongoDB, the default time limit for a **transaction is 60 seconds**. If the transaction takes longer than this limit, it will *fail and be aborted*.

## Simplifying MongoDB Data with PyMongoArrow
Managing and manipulating data efficiently is a crucial aspect of working with MongoDB. PyMongoArrow is a valuable library that simplifies data conversion between MongoDB documents and Apache Arrow RecordBatches. Let's take a closer look at what PyMongoArrow offers and how it can enhance your MongoDB workflow.

### Installation and Setup
Getting started with *PyMongoArrow* is straightforward. You can install the library using pip:

```py
pip install pymongoarrow
```
To begin using PyMongoArrow, it's necessary to enable the integration with PyMongo by invoking the `install_pymongo()` method:

```py
import pymongoarrow
pymongoarrow.install_pymongo()
```

###What Does PyMongoArrow Do?
PyMongoArrow provides several key functionalities that can greatly improve your data handling capabilities:

1. Conversion to Apache Arrow RecordBatches: PyMongoArrow allows you to convert MongoDB documents into Apache Arrow RecordBatches. This conversion provides a structured and efficient representation of your data, enabling advanced analytics and processing.
2. Conversion from Apache Arrow RecordBatches: Conversely, PyMongoArrow allows you to convert Apache Arrow RecordBatches into MongoDB documents. This functionality facilitates seamless integration with other MongoDB operations and simplifies data migration or synchronization tasks.
3. Enhanced Data Manipulation: By utilizing Apache Arrow RecordBatches, PyMongoArrow enables efficient data manipulation and analysis. You can leverage the powerful features of Apache Arrow, such as vectorized operations, to perform complex computations and transformations on your MongoDB data.
4. Cross-Language Compatibility: PyMongoArrow supports using Apache Arrow RecordBatches in Python as well as other programming languages. This compatibility allows you to leverage the benefits of Apache Arrow in a language-agnostic manner, making it easier to collaborate and integrate with different tools and systems.

With PyMongoArrow, you can streamline your MongoDB data workflows by leveraging the capabilities of Apache Arrow. This powerful combination simplifies data conversion, enhances data manipulation, and promotes interoperability across different programming languages.

## MongoDB Aggregation: Transforming Data with Power and Flexibility
MongoDB Aggregation provides a powerful framework for **transforming and processing data** within a MongoDB collection. It enables you to perform complex data manipulations, calculations, and aggregations using a pipeline of stages. Here are some key concepts and examples to help you harness the full potential of MongoDB Aggregation.

### Understanding the Pipeline Stages
The aggregation pipeline consists of **multiple stages,** with each stage transforming the documents as they pass through the pipeline. Here's an overview of the pipeline stages:

- Each stage takes a document as input and produces a document as output.
- Each stage can have zero or more documents as output, allowing you to shape and refine your data at each step.
- Stages can include operations like filtering, grouping, sorting, limiting, projecting, and more.

### Executing Aggregation Queries
To perform an aggregation, you can use the aggregate() method on a MongoDB collection. The method takes two parameters: the pipeline array and an optional options document. Here's an example of using aggregation:

```py
db.collection.aggregate(pipeline, options)
```
In the above code snippet, **pipeline is an array of stages**, and options is an optional document that can specify additional parameters for the aggregation.

### Aggregation Examples
Let's explore a few common aggregation scenarios to demonstrate the power and flexibility of MongoDB Aggregation.

- **Grouping and Averaging**
```py
db.collection.aggregate([
    {"$match": {"author": "Ricardo"}},
    {"$group": {"_id": "$author", "avg_likes": {"$avg": "$likes"}}}
])
```
This example matches all documents with the author name "Ricardo" and groups them by author, calculating the average likes per video.

- **Sorting, Limiting, and Projecting**
```py
db.collection.aggregate([
    {"$match": {"author": "Ricardo"}},
    {"$group": {"_id": "$author", "likes": {"$sum": 1}}},
    {"$sort": {"likes": -1}},
    {"$limit": 5},
    {"$project": {"_id": 0, "title": 1, "likes": 1}}
])
```
Here, we match documents with the author name "Ricardo," group them by author, count the number of videos, sort in descending order of likes, limit the result to 5, and project only the title and likes fields while excluding the `_id` field.

- **Setting a New Title**
```py
db.collection.aggregate([
    {"$match": {"likes": {"$gt": 100}}},
    {"$sort": {"likes": -1}},
    {"$limit": 5},
    {"$project": {"_id": 0, "title": 1, "likes": 1}},
    {"$set": {"title": "New Title"}}
])
```
In this example, we match documents with likes greater than 100, sort and limit the result, project only the title and likes fields, and then set a new value for the "title" field.

- **Counting**
```py
db.collection.aggregate([
    {"$count": "likes"}
])
```
This aggregation counts the total number of likes across the entire collection, providing a single result document with the count.

- **Outputting Aggregation Results to a New Collection**
```py
db.collection.aggregate([
    {"$group": {
        "_id": "$author",
        "max_likes": {"$max": "$likes"}}
    },
    {"$limit": 5},
    {"$out": "likes"}
])
```
Here, we group documents by author and calculate the maximum number of likes. We then limit the result to 5 and output the aggregaated data to a new collection named "likes."

By leveraging the powerful capabilities of MongoDB Aggregation, you can perform sophisticated data transformations, generate meaningful insights, and optimize query performance for complex data processing scenarios. The aggregation pipeline offers a versatile and efficient way to manipulate and analyze your MongoDB data.

## Indexing
To optimize query performance in MongoDB, indexing plays a crucial role. By creating appropriate indexes on specific fields, you can significantly enhance the speed of data retrieval and improve overall database performance. Here are some examples of how to create indexes using the MongoDB CLI:

Creating a unique index on the "email" field:

```py
db.collection.createIndex({ "email": 1 }, { "unique": true })
```
Setting the "unique" option to true ensures that the "email" values are unique in the collection.

Let's consider a "users" collection that stores user information with fields like "name," "email," and "age." We can create multiple indexes to optimize various types of queries.

Index on the "name" field:

```py
db.users.createIndex({ "name": 1 })
```
This creates a single-field index on the "name" field with an ascending sort order (1).

Compound index on the "email" and "age" fields:

```py
db.users.createIndex({ "email": 1, "age": -1 })
```
This creates a compound index on both the "email" and "age" fields. The** ascending sort order (1) **is used for the "email" field, while the **descending sort order (-1)** is used for the "age" field.

By creating these multiple indexes, you can optimize different types of queries. The index on the "name" field improves queries searching for users by their name. The compound index on "email" and "age" fields is beneficial for queries involving filtering by email and sorting by age in descending order.

To view the indexes in a collection, you can use the following command:

```py
db.collection.getIndexes()
```
This will provide a list of all indexes defined on the collection, including their names, key fields, and any additional options.

By leveraging appropriate indexing strategies, you can maximize the performance of your MongoDB queries and efficiently retrieve data from your collections.

## MongoDB Compass
MongoDB Compass is a versatile **GUI tool** designed to streamline your MongoDB data management tasks. With its user-friendly interface, you can effortlessly explore, manipulate, and optimize your MongoDB data. From creating queries and aggregations to managing indexes and views, MongoDB Compass provides a seamless experience. Additionally, it simplifies data import/export, making it easy to import data from various formats and export data for analysis or sharing. Embrace MongoDB Compass to enhance your productivity and unlock the full potential of MongoDB.