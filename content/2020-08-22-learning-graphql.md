---
title: "Learning GrapgQL"
date: "2020-08-22"
tags: ["Developer"]
image: ""
gradients: ["#f7797d", "#FBD786"]
---

## GraphQL
**GraphQL** is a query language and is strongly typed. This is usually for building a stack for an API. It’s implementation was created by Facebook. However unlike REST APIs, GraphQL uses only one **url** and can resolve all the queries. By this i mean we can get all the blogs for a user. REST would require us to get the user and their blog’s ids. Then query on all blog via its id.

### Schema in GraphQL (SDL)
Usually for components such as users, we an create a `gql` extension file, `user.gql`

``` js
extend type User {
	id: ID			// Scalar type from GraphQL
	name: String!	// Scalar type with ! (means required)
	friends: [User!]!  // Built in type [] (must to array of type User)
}

extend input newUserInput {
	id: ID
	name: String!
	friends: [User!]!
}

// This is used for thigns like CRUD. See CRUD for more information
extend input updateUserInput {
	id: ID
	name: String
	friends: [User]
}

extend type Query {
	/* All the query goes here
	 * QueryAction: Type
	 * QueryActions are functions to retrieve data
	 * (must return the valid type)
	 */
	user(id: ID!): User!
	users: [User]!
	getData: User! // Example query used for resolver.
}

user(id = `1`) {
	// Since in Query this function must returns type User.
	User {
		id
		name
		friends
	}
}

users() {
	User {
		id
		name
		friends
	}
}
```

### CRUD
```js
extend type Mutations {
	/*
	 * Note that for the inputs they must be of type input
	 */
	newUser(input: newUserInput!): User!
	updateUser(id: ID!, input: updateUserInput): User!
	removeUser(id: ID!): User!
}

mutation newUser() {
}

mutation updateUser() {
}

mutation removeUser() {
}
```

### Resolvers
```js
Used for retrieving data.

// The keys should match the ones above.
export default {
	Query: {
		/* From the above Query Object. This means the resolver is created.
		 _: root args
		 * args: resolver's args
		 * ctx: context, global state information. i.e user, cache
		 * info: ADVANCE STUFF. NOT NEED TO LEARN JUST YET
		*/
		getData(_, args, ctx, info) {
			// throw Error()	// Handling throwing error
		}
	}
	Mutation: {}
	User: {
	}
}
```
See more about resolvers in the resolver in Server

### Init a server (using Apollo)
**ApolloServer** is basic *Express* that utilizes GraphQL. To install ApolloServer,

```bash
npm i apollo-server graphql
```

```js
import { ApolloServer } from 'apollo-server'
import {  loadTypeSchema  } from './utils/schema'

import user from './types/user/user.resolvers'

const types = ['user', /* Other objects for project */]
export const start = async () => {

const rootSchema = `
	type User {
		name: String!
		age: Int
		friends: [User!]!
	}
	extend type Query {
	user(name: String!): User!
	friends(name: String!): [User!]!
}
	schema {
		query: Query
		mutation: Mutation
	}
	`

// Here we load the tpyes into a schema
const schemaTypes = await Promise.all(types.map(loadTypeSchema))
const server = new ApolloServer({
	typeDefs: [rootSchema, ...schemaTypes],
	resolvers: { // Usually resolvers init here
		user(_, args) {
			return { name: args.name, friends: [] }
		},
		friends(_, args) {
			return { name: args.name, friends: [] }
		},
		User: {
			// Resolvers for type User
			name(_, args) {
				return 'John'
			},
			age(_, args) {
				return 15
			},
			friends(_, args) {
				return []
			},
		}
	},
	context({ req }) {
		// use the authenticate function from utils to auth req, its Async!
		return { user: null }
	}
})

await connect(config.dbUrl)

// Starting server
const { url } = await server.listen({ port: config.port })
	console.log(`GQL server ready at ${url}`)
}
```

### Interface
Interface creates an abstract type for objects. Rather than `type`, use `interface` like in OOP.

```js
interface Phone {
	brand: String!
	os: String!
}

type IPhone6 implements Phone {
	brand: String!
	os: String!
	iosVersion: Float!
}

type IPhone5 implements Phone {
	brand: String!
	os: String!
	iosVersion: Float!
}

type SamsungGalaxy6S implements Phone {
	brand: String!
	os: String!
	andriodVersion: Float!
}
```
This is useful if you want to query the entire phone. Rather then querying individuals, ie IPhone6, IPhone5, SamsungGalaxy6S, …, we can query the interface Phone to get all the `phones`. Like so

```js
type Query {
	phones: [Phone]!
}

schema {
	query: Query
}
// In the resolver to resolver such query.
resolver: {
	Query: {
		phones(_, args) {
			return [
				{ brand: 'Apple'},
				{ brand: 'Samsung'},
			]
		}
	},
	Phone: {
		// This is important when returning an interface since, it is an abstract type we need to more specification.
		__resolveType(phone) {
			return phone.brand
		}
	}
}
```
To query in localhost: Note that `...` on `type` allows us to get its keys only to that of the given type. The example given allows to query the `iosVersion` on the `iphone6` since other types like `SamsungGalaxy6S` won’t have that key.

```js
{
	phone {
		brand {
		}
		... on Iphone6 {
			iosVersion	// This will allow us to return the iosVersion on the Iphone6
		}
		... on SamsungGalaxy6S {
			andriodVersion
		}
	}
}
```
Unions This is used the same way as interfaces, instead it’s implements like the or.

```js
Union SeachItem = People | Place | Review // | ...
```