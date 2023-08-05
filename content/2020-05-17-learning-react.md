---
title: "Learning React"
date: "2020-05-17"
tags: ["Developer"]
image: "https://www.dropbox.com/s/5jzc1ruq2xlivkf/react.png?raw=1"
gradients: ["#4e54c8", "#8f94fb"]
---

## Installation

```jsx
import React from "react"
import ReactDOM from "react-dom"

// JSX
ReactDOM.render(,document.getElementbyId(‘root’))
// the html content, where in the html
// So I have a div root where all the html code in args one.
```

### Using function
```jsx
function NavBar () {
	// js code
	return (
		// html
	)
{
```
To call it,

```jsx
<NavBar />
```
hence rendering navbar in html is,

```jsx
ReactDOM.render(<NavBar />,document.getElementbyId(‘root’))
```

## Moving components in to components folder
It goods practice to store all React components in a components folder. NavBar.js should be in folder components

```jsx
import React from "react"

function NavBar() {
	return (
	    // Navbar HTML
		// This usually is consist of other React ‘components’ and ‘elements’
		<NavBar />
		// …
		</Footer />
	)
}

export default Content  // So we can import in other files
```

Then to use component, import it in the desire file.

```jsx
import NavBar from "./components/NavBar."

<NavBar />
```

## Styling
Styling inline is more dynamic since we can change it in React.

```jsx
// inline

container = {
	color: "#000000",
	fontSize: 40,
	padding: "50px",
	// Note: you can use ternary
	display: true ?  "block"  :  "none"
}
<h1 style={ container }></h1>

// className rather than class
<div className="container"></div>
```

## Using JS in React
You can use JS normally in React, however if you want to display it to the DOM, such that

```jsx
let user = "Max";

<h1>Welcome { user }</h1>
```

Here we use `{ }` just like in other languages such as HUGO `{{ }}` or Jinja `{{ }}`. We use `{ }` to display that we are using JS.

## Arguments in React components
Passing the arguments with a key and value in the tag.

```jsx
// Note is { {...} }. The outer {} is to tell React its going into JS, and {...} is the json in JS.
<Content
    json = { {...} }
    other = "there can be more arguments"
/>
```

In the function Content there exist one argument props. props is also a json that hold all the arguments parsed.

```jsx
function Content(props) {
	console.log(props)
	/*
		props = {
			json = {...},
			other= "there can ..."
		}
	*/

	return (
		// ...
	)
}
```

## Class

```jsx
function Component(props) {
	return (
		<div>{ props }</div>
	)
}
```

Class are more useful and a neater way than functions. I will compare the JS Classes to Java Class

- Like Java `extends` allows you to make the components have useful methods that React.Component class has.
- `render()` is the default methods that returns the html code, likes Java `main()` method

```jsx
import React, {Component} from  "react"

class Component extends Component {
	constructor() {
		// This is required as our parent Component constrcutors also need to be init, when we init the component.
		super();

		// State is also required to store values that are for the class. This is useful for when we can change it by using this.setState
		this.state = { key: "value" };
	}

	methods() { // ... }

	render() {
		let var = methods();
		return (
			<div>{ this.props }</div>
			<div>{ this.json.value }</div>
		)
	}
}
```

This is equivalent to `function Component(props)`. Except now, we have a better version, as it has a constructors for initialisation and storing attributes and methods that can be used only by the components and is nicely scoped there.

## Event Handlers and this.setState
We can add EventHandlers just like inline html but in camelCases like so

```jsx
<div onClick={ clickMethod() }>{ this.props }</div>
<div>{ this.json.value }</div>
```

You then need to bind it the event in the constructor of the class. To me its like `element.addEventListener()`

```jsx
constructor() {
	this.state = { counter: 0 };

	// This is like Component.addEventListenter(_,clickMethod())
	this.clickMethod = this.clickMethod.bind(this);
}

clickMethod() {
	// The passes arg is is current state and this.setState allows us to change the attributes in the class
	this.setState(prevState => {
		count = prevState.count + 1;
	});
}
```

Note: Every time `setState` is used the `render()` is called after.

## Lifecycle
Event compare has a lifecycles. The lifecycle has three phrase

The main one is `componentDidMount()`. This phrase is runs **after** `render()`.

```jsx
componentDidMount() {
	// Make sure here after component is on DOM.
}
```

### Creating A Portfolio
Since I need to create a portfolio, I might as well create a web one using react. Just to give me a fell of what it takes.

So installing and running React locally was not so hard. Its just in a terminal change `app-name` to be your project folder. Keep in mind you’ll need `npm` and `node.js`

```bash
npx create-react-app app-name
```

For me this took awhile, apparently it downloaded 200+ MB worth of React modules … Once done,

```bash
cd app-name
npm start
```

This is run and open localhost and you can start editing. For my portfolio I needed only bootstrap css and that was easy enough, by adding it Bootstrap CDN for CSS. For the full Bootstrap, you’ll have to search it up. Sorry.

## Thoughts after making Portfolio
So I’ve made a nice small portfolio page in around 2 days. My feelings on react is that it is amazing compare to how I use to make webpages. The reusable is probably the best feature for me, cause I usually use the same navbar, and card template and change it up with more css. All I need to do now is to bring the files of the divs instead of copy paste the code from previous projects.

Through I think React is a not much of a learning curve, I still have a lot to learn such as the more about the Lifecycle of a Class and using React Hooks. I’ll be sure to write on them when I bothered to invest my time into learning them. As for now I think got a good feel of what React is compatible.

Finally, For y’all who want to know the [result](https://z5208980.github.io/me/) of a few hours of learning React