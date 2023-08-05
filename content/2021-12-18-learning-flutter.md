---
title: "Learning Flutter"
date: "2021-12-18"
tags: ["Developer", "Mobile"]
image: ""
gradients: ["#84fab0", "#8fd3f4"]
---

## Abstraction
The reason why I learning Mobile development is the shear amount of skill and experience required in job interview. I decided Flutter over
React Native and even native Andriod or Swift is because I am too ceebs to learn a new environment and framework. Flutter allowed me to
create a mobile app using my extensive knowledge of JS and C.

# Flutter
## Setup

This is a easier way to setup the flutter environment

- Download Andriod Studio
	- In Andriod Studio, you need to navigate to the **SDK manager** and from there you have to choose the packages such as,
		- Android OS system (Will need for creating an Andriod Emulator)
		- Andriod SDK CommandLine

- Download **Flutter** (either from web or git clone)
	- Then add the file to the PATH. In Windows, you need to window search env and append the the flutter's bin folder, such that `directory_to\flutter\bin`.
	- Then on the terminal, `flutter doctor`
	- (Most liekly) need to run the cmd, `flutter doctor --android-licenses` to agree to the licensing

## To create Flutter app
```
flutter create project_name
```

This will download a boilerplate for the flutter app. Then to run the app we will need to `cd` in the folder and run the command `flutter run`. This will connect to the web, however for andriod development we will try connect to the **Andriod Emulator**. Andriod emulator can be made via the **AVD manager** in Andriod Studio.

`Creating Andriodn Emulator ...`

### Connect Flutter application to Andriod Emulator
Now, that we have the two main component complete **(Flutter App, Andriod Emulator)**, we will be connect them. To do so, we can open the flutter folder from `flutter create` in **VS Code**. Here we can select the Device and choose the Andriod Emulator. Then all we need to is click the play button to run the app!

# Basics
Referring the anatomy of Flutter to React.js. Flutter has **Widget** compared to *Components*. Example of Widget include, `MaterialApp`, `Center` and `Text`
Also note that flutter is the language `Dart`.

A very basic *hello world* can be displayed as,
```dart
import  'package:flutter/material.dart';
void main() => runApp(HelloFlutterApp());

class  HelloFlutterApp  extends  StatelessWidget  {
	@override
	Widget build(BuildContext context)  {
	return  MaterialApp(
		home:  Center(
			child:  Text("Hello Flutter !"),
			),
		);
	}
}
``` 

Here we see that the widget is done via depth. This can is just like html where it is get deeper.

`SafeArea`
Another type of wrapper used that will be useful is the `SafeArea`, where it will display the app within the display and not overlapping with the operating system status bar

## Using Material Icon
Since Flutter is made by Google, the style will be usingis Material Design (also Google's).
To user material design.

`MaterialApp` is hte widget we wrap on top of widget to change the design to a material UI.

It usually consist of a `home` property
```
MaterialApp (
	home: <Widget>
);
```
#### Statelesswidget / Statefulwidget
Widget can either be
- Statelesswidget - Immutable widgets. They can't change when a user interact with it, but will change entirely everytime hte app is loaded or saved cause it has no memory
- StatefulWidget - They have a state and will change depending on the actions taken. Like toggle, or radio buttons in inputs

An example of StatefulWidget

```dart
class HelloFlutterApp extends StatefulWidget {  
	@override  _HelloFlutterAppState createState() => _HelloFlutterAppState();
}

class _HelloFlutterAppState extends State<HelloFlutterApp> {  
	@override Widget build(BuildContext context) {    
		return Container();  
	}
}
```

When you want to update / change a *state*, then you can use `setState()` like so,
```dart
setState(() { 
	variable = newVariable; 
})
```

## Common Widgets

```dart
Scaffold (		// body tag
	appbar: Appbar(...);
	body: Container();
),

Appbar (	// this is like the navbar
	title: const Text('...'),
	backgroundColor: Colors.white,
	actions: <Widget>[...],
);

IconButton (		// button with onPress
	icon: const Icon(Icons.arrow_back),
	tooltip: '...',
	onPress: () {
		// ...
	},
),

Container (		// like div
	color: Colors.blue,
	width: double.infinity, 	// As large as it parent's width
	height: 250,
	child: Image.network(...)  	// Or something or that sort
),

ListView (		// like ul
	children: <Widget>[...],
),

ListView.builder(      	// For more dynamic rendering 
	itemCount: something == null ? 0 : something.length,            			
	itemBuilder: (context, index) {                    
		return Padding(          
	          padding: const EdgeInsets.all(8.0),            
              child: Text(movies[index]["title"]),         
		);        
	},      
),


// Image.asset( 	// Using local imgs
Image.network(		// Using the internet
"https://github.com/ptyagicodecamp/educative_flutter/raw/profile_1/assets/profile.jpg?raw=true",  
	height: 250,  
	fit: BoxFit.cover, 
),


Divider(	// hr
   thickness: 5, // thickness of the line
   indent: 20, // empty space to the leading edge of divider.
   endIndent: 20, // empty space to the trailing edge of the divider.
   color: Colors.black, // The color to use when painting the line.
   height: 20, // The divider's height extent.
 ),

ListTile (		// Leading Icon | Text | Trailing Icon
	leading: Icon(Icons.arrow_back),   
	title: Text("Hello World"),   
	subtitle: Text("small text"),   
	trailing: IconButton(     
		icon: Icon(Icons.message),     
		color: Colors.indigo.shade500,     
		onPressed: () {},   
	),
),

// mainly used in `Scaffold.floatingActionButton`
FloatingActionButton(
	onPressed: () { ... },
	backgroundColor: Colors.green,
	child: const Icon(Icons.navigation),
),
```

#### Row and Column
`Row()` and `Column()` are grid layout that is usually for the layout of vertical and horizontal items. They contain a `child` attribute like so,
```dart
Row( 
	mainAxisAlignment: MainAxisAlignment.spaceEvenly,
	child: [...] // or <Widget>[]
),
```

```dart
An example is of using a row in cleaner Flutter is,

Widget buildTextBtn() { 
	return Column(   
		children: <Widget>[     
			IconButton(       
				icon: Icon(
					Icons.message,         
					color: Colors.indigo.shade800,
					),       
				onPressed: () {},     
				),     
			Text("Text"),   
		], 
	);
}

Widget buildCallBtn() { ... }
Widget buildVideoBtn() { ... }
Widget buildEmailBtn() { ... }

// Then call the components in a row,
Row( 
	mainAxisAlignment: MainAxisAlignment.spaceEvenly,
	child: <Widget>[
		buildTextBtn(),
		buildCallBtn(),
		buildVideoBtn(),
		buildEmailBtn(),
	]
),
```

## Styling

#### Global
This is used on `Widgets` that have `theme` as it attribute that takes `ThemeData` and when using `theme`. Ane example and a good practise for creating a styling software pattern is using a class such as,

```dart
// An example of dark theme styling
class MyAppThemes { 
	static ThemeData appThemeDark() { 		
		brightness: Brightness.dark,  // dark mode
		appBarTheme: AppBarTheme(   			
			color: Colors.black,	// change appbar to dark
			iconTheme: IconThemeData(     
				color: Colors.white,  // need to change icons to white   
				), 
			),
			iconTheme: IconThemeData(   
				color: Colors.blue, 
			),
		),
	}
	
	// More stlying like appThemeDark()
	static ThemeData appThemeDark() { ... }
}
```

Then to use the style in `theme` attribute,

``` dart
ENUM THEME { DARK, LIGHT }

const appTheme = THEME.LIGHT

MaterialApp(
	theme: appTheme == THEME.DARK                    
		? MyAppThemes.appThemeDark()         
		: MyAppThemes.appThemeLight()
	home: Scaffold(        
		appBar: buildAppBarWidget(),        
		body: buildBodyWidget(),        
		floatingActionButton: FloatingActionButton(          
			child: IconButton(            
				icon: Icon(Icons.threesixty),            
				onPressed: () {              
					setState(() {                
					appTheme == THEME.DARK                    
						? appTheme = THEME.LIGHT          
						: appTheme = THEME.DARK;              
					});            
				},          
			),
),
```

## API in Flutter

#### Setup

You will need to add the `http` package to `pubspec.yaml`
```dart
dependencies:  
	flutter:    
		sdk: flutter  
	http: ^0.12.0+1			// This is the main one!
```

and call it in the `main.dart`. To use `http` request, get call it like so,

```dart
import 'dart:convert';		// JSON parser
import 'package:http/http.dart' as http;	// like axios

// htto get request
final response = await http.get(apiEndPoint);
var data = json.decode(response.body); 	// from dart:convert
```

Note this is an await function so top level functions call will need `async`

When we want to load something at the every beginning like the data from APIs, we can use the `initState`
```dart
class _MoviesListingState extends  State<MoviesListing>  {

	@overridevoid 
	initState() { 
		super.initState(); 
		apiCall();
	}
	
	@override
	Widget build(BuildContext context)  { ... }
}
```
