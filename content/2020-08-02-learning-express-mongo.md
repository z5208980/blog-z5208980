---
title: "Learning ExpressJS And MongoDB"
date: "2020-08-02"
tags: ["Developer"]
image: "https://www.dropbox.com/s/saj3h5utevzp18v/mongodb.png?raw=1"
gradients: ["#76b852", "#8DC26F"]
---

## Abstraction
This is my learning notes on learning for the first time ExpressJS, a JS library useful for creating an API. Also, I’ll be trying to learn MongoDB. (Note MongoDB was harder to install, so instead I resorted to using MongoDB Altas [Cloud Version]).

## ExpressJS
```bash
npm i --save express
```

### Other useful libraries to consider
```bash
npm i --save morgan	# Debugger for HTTP: GET /endpoint 400 2ms
npm i --save lodash	# Useful for _
# Refresh apps upon saving, remoes the need to restart app everytime
npm i -g nodemon	# Usage: nodemon <server.js>
nodemon server.js
```

### Init Express app
```js
var express = require('express');
var app = express();

// API Routes
...

const port = 3000
app.listen(port, () => {
  console.log(`Server running on localhost:${port}`);
});

// HTTP Methods
app.get('/lions/:id', function(req, res) {
	var lion = _.find(lions, {id: req.params.id});
	...
});

app.post('/lions', function(req, res) {
	...
});
```

### Middleware
Utility classes to help Express. The backbone of Express. Just a function.

In Express, Middleware requires `next()` so it know to continue in the server. The middle in the example below, is the `function(**kwargs)`.

```js
// This run first when endpoint has path /
app.all('/', function(req, res, next) {
	// ...
	next();
});

// This is good for querying the db before going to the API endpoint.
// The function runs first, when ever there is a param, intent.
// i.e /brain/:intent
app.param('intent', function(req, res, next, intent) {
	// ...
	next();
});
```

### Routers
Routers allows you to determine how an application responds to a client request to a particular endpoint.

```js
// In seperate folders, we can have,
/* foo.js */
var fooRouter = require('express').Router();
// endpoints ...
fooRouter.get(/* ... */);

module.exports = fooRouter;

/* bar.js */
var barRouter = require('express').Router();
// endpoints ... (can have same ends as bar.js)
module.exports = barRouter;

// These are Routers are basicall the 'app' for that server.
// Then in the server JS file, we load them in and mount them
var fooRouter = require('./foo');
var barRouter = require('./bar');

app.use('/foo', fooRouter);
app.use('/bar', barRouter);
/*
	.../foo/... we use fooRouter's endpoints
	.../bar/... we use barRouter's endpoints
 */
```
For my learning project, I won’t be needing this, but I will just be adding Routers as it may be very VERY useful the *versioning* an API.

## Mongo
**NoSQL Db** meaning it is not a relational database. It is known as a “*document store*”.

These are useful libraries for MongoDB
```bash
npm i --save mongodb
npm i --save mongoose
```

### Mongoose
Allows us to create Schemas for our non schematic Mongo DB. Since I had trouble with Mongo, I’ve decided to use MongoDB Atlas and have my db in the cloud

```js
var mongoose = require('mongoose');

mongoose.connect('mongoDB_URL', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});
```

### Modeling
```js
// In fooModel.js
var mongoose = require('mongoose');

// We need a model so we can query, our MongoDB
var Schema = mongoose.Schema;

// This schema is my layout. I'll have
var FooSchema = new Schema({
    key: {
      type: String,
      required: True,
      unique: True
    },
    key2: [{type: String}],
    key3: { type: Int },
    key4: [{type: Boolean}]
});

let fooModel = mongoose.model('foo', FooSchema);
export.module = fooModel;
```

### Typical GET action
This is to query or filter data from an MongoDB. I also want to point out that I’ve been using MongoDB Atlas which is the cloud version of Mongo. It literally the same thing, except the db is not on my local machine.

```js
const fooModel = require('./fooModel');

const result = await fooModel.find({key: inputted_key }); // Mongoose Syntax
// also findById('id', ...)

try {
  res.send(result);	// Send queried from find()
} catch (err) {
  res.status(500).send(err);
}
```

### Typical POST action
To create instance of a model, we user the `model` we exported. To save the model, we you the `save()` method on the new instance. Note that this `save()` comes from Mongoose.

```js
// Create a model instance
const newFoo = new fooModel({
	...
});

// This is to save the model
try {
    await newFoo.save();		// Mongoose Syntax
    res.send(newFoo);
} catch (err) {
    res.status(500).send(err);
}
```
Usually the data from model, will come in from `req.body`, if the frontend has set the `data: {tag: '', pattern: [''], response: [''], context: [''],}` when using `fetch` or `axios`.

### Other useful things to add
**CORS** is important to allow which url cans access your endpoint API. To enable CORS, then

```bash
npm i --save cors
```

```js
// server.js
const cors = require('./cors');

// MiddleWare
app.use(cors({
  origin: '*' 	// Allow anyone to access or add the url that u allow.
}));
```
