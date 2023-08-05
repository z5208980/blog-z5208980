---
title: "Learning Angular"
date: "2020-07-29"
tags: ["Developer"]
image: "https://www.dropbox.com/s/5efalso6xtwwu46/angular.png?raw=1"
gradients: ["#DD0031", "#C3002F"]
---

### Installing angular CLI
`npm install -g @angular/cli`

### To create an Angular Project
It will ask you questions, a such using routing and css type `ng new project-name` then you can cd in it, `cd project_name`

To start server
`npm start`

### Creating a component
This is generate files necessary for the component. Important thing is the `app.module.ts`. This file is where all the things are store in-order for the app to run. `ng g component item`

There are lots of ready to use component, that will make life easy, but something, you wanna be more flexible and create component that are unique. To do so we need to know Typescript. As I have knew learnt typescript, all this will be new to me.

In `app.component.ts`

```js
import { Component } from '@angular/core';

/**
	This is used when ever the component is used
	Important keys are :
		- selector: allow this comp be attach to the DOM
		- templateUrl: where the component code will be (html file)
		- styleUrls: [css files] to style the component
  */
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
   // variables that can be accessed in the html
   title = "Hello World"
   constructor() { }
   ngOnInit(): void { }
}
```

### Component Routes
If you have used react routers dom for client side path routing, you can do the same in Angular. So basically, at the start of the project, when we `ng new project_name`, it prompt us to enable routers or not, if so, there will be a file called, `app-routing.module`.ts.

```js
/**
	The main part in the file is this routes var. Which is an array that takes in
	{ path="home", component= HomeComponent },
	Just like in react where we have
	<Router path="home" component={HomeComponent />
	Instead of manually creating them with the Reouter comp, in Angular we use and array.
  */
const routes: Routes = [
	{ path="home", component= HomeComponent },
	{ path="stats", component= StatsComponent },
	{ path="about", component= AboutComponent },
	{ path="**", redirect="/" }
];
```

Note: This is important, as it took me ages to figure out, we need to add `<router-outlet></router-outlet>` in our `app.module.html`, in order for the Routes to work.

### Component Architecture
When we have a component and want to use it in other, we can simply just create a component, and using `selector: 'app-new-component'` in `@Component` when we make that new component.

That why, if we set up the new component, using `ng g component new-component`, we can go to our other component and simply add it like html.

```js
<app-new-component></app-new-component>
```

```js
export class DashboardComponent implements OnInit {
    // variables that can be accessed in the html
    title = "Hello World"
    constructor() { }

    ngOnInit(): void { }
}
```

Passing in parameters to components (sharing components), Using @Input and @Output
So, if we wanna past in a variable from parent component into our children component that we called, we can so by declaring, `[childVarible]="parentVariable"`.

So in the child ts file

```js
import { Component, OnInit, Input, Output } from '@angular/core';
```

### Ng
```js
<div>{{jsonVariable | json}}</div>
<div *NgFor="for item of items">
{{item}}
</div>
<div *NgIf="if cond then a else b">
</div>
<input ([NgModel])="userInput" type="text"></input>
```
The above are all very basic ng syntax that can be used for looping, if statements and getting the user input live onchange.

During, this time, I wanna point out that I’ve also been playing around material design for awhile. It is a very learning curve, especially angular material. I will be learning material when I do another project on React.

### Services
The way we get data to fill in our webpage is through services that we create, via `ng g s service_name`. It basically a class that returns `observerables` that the components `subscribe` to get the json data. (This is like the observer pattern in OOP)

To import the service that has been create, you do it in `app.module.ts`

```js
import { ApiService } from './service/api.service';

@NgModule({
...
providers: [
    ApiService
  ],
...
});
```

To use this service in a component,

```js
import { ApiService } from '../service/api.service';

class {
	constructor(private apiService: ApiService) { }
	/* then u can use the methods in the service and subscribe to get data */
}
```

### Deploy to gh-pages
```bash
// Deploying to gh-pages
npm i g install angular-cli-ghpages

// Deploying to gh-pages
ng add angular-cli-ghpages
ng deploy --base-href=/<repositoryname>/
// Then git add and commit
```

### First Impression, Angular vs React?
So, Angular to me seems to be a very steep learning curve. It’s much different and complex compared to React or vanilla JS. I know that I won’t be using Angular again for a very long time. To me it just seem too much, when other frameworks have features and are lightweight. Throughout creating an Angular webapp, I struggled to used libraries such as Leaflet and even material UI, whereas using them in JS was easy af. That said, it very well designed, and it very structured, making the code organised and scalable. I noticed it uses OOP design patterns which I very like, such as observables and singleton. But yea, it just seem like too much for me, using `ng serve` to build and compile my app took while too.

That said, This was all done in three days. Here’s my webapp. It’s on Covid-19 information about Australia, containing simple data visualisation and nice openstreetmap detailing the cases for each local area. [The project I’ve made whilst learning Angular](https://z5208980.github.io/covid19-au/).