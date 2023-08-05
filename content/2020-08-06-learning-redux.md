---
title: "Learning Redux (Dropped)"
date: "2020-08-06"
tags: ["Developer"]
image: ""
gradients: ["#7F00FF", "#E100FF"]
---

## Redux
Bring all states into one giant JS object (called a state tree). Contains a reducer function (2 arguments)
- current state of UI
- an action
returns a new state of the UI

### Installation

```bash
npm  i redux

# Create react app with redux
npx create-react-app my-app --template redux
```

```js
// Creating a reducer
const subReducer = (state = {total: 10}, action) => {
	if(action.type === 'ADD') {
		const total = state.total;
		const amount = action.payload.amount;
		// state.total = total + amount // This will mutable and hence react won't see rerender.
		// Hence, we can return new instance of state
		return {
			total: total + amount
		}
	}
	return state;
};

applyMiddleware: function()
	// Simple allow us to run to our reducers when creatingStore, creating a state.
	const middlewareFunction = ({ /* ... */}) => {
		console.log('Middleware Function');
	}

	// This will allow us to run our middleware function first to 'API' call and mutate our objects before creating a store.
	const storeMiddleWare = createStore(reducer, applyMiddleware(middlewareFunction));

bindActionCreator: function()
	// Binds an action with a dispatch.
	const createAddAction = (amount) => {
		return {
			type: 'ADD',
			payload: {
				amount: amount
			}
		}
	};
	// the use of bindActionCreator will allow us to, dispatch and add.
	const dispatch = bindActionCreator(createAddAction, store.dispatch);
combineReducers: function()
	// Combining reducers
	const reducer = combineReducers({
		childOne: subReducer
		// ... Other reducers

	})
compose: function()
	// combines functions with same arguments
	const boldStr = (string) => string.bold();
	const upperStr = (string) => string.toUpperCase();

	const boldAndUpperStr = compose (boldStr upperStr);
	boldAndUpperStr('hello world'); 	// <b>HELLO WORLD</b>
createStore: function()
	// Can be used to store a reducer.
	const store = createStore(subReducer);
	// you can get the state of reducer.
	store.getState();
	// Allows you to change the state via an action.
	// In this case, it is a of action.type ADD and has a payload
	store.dispatch({ type: 'ADD', payload = {amount: 23} });
```

### Mapping our reducer to React
```js
// Take reducx (state) and take a smaller subtree of that redux. MEaning that if a , not all the component will take a rerender().
const mapStateToProps = state => {
	return state;	// returns entire state.
	// return state.something // Return the subtree of a state.
};

const mapDispathToProp = dispatch => {
	// returns a state
	return {
		dispatch(dispatchFunction());
	}
};

// Return new
const NewHigherComponent = connect(mapStateToProps, mapDispathToProp)(classComponent);

// can use as <NewHigherComponent />
const store = createStore(
	reducer,
	applyMiddleWare(/* middleWareFunctions */)
	window.__REDUX_DEVTOOLS_EXTENSION__	// Should have Redux Tab in DevTool. Really Helpful
);

<Provider store={store}>
	<Application />
</Provider>
```
