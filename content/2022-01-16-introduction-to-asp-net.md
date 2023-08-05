---
title: "Introduction to ASP.NET"
date: "2022-01-16"
tags: ["Web", "Developer"]
image: ""
gradients: ["#16d9e3", "#46aef7"]
---

### Motivation
Today I'll be learning about the .NET core ecosystem specifically, the web application because that somthing that might be easier to learn. The purpose for me learning this is to prepare for my intern as a developer for a healthcare company.

### .csproject file
When we create a new project, one important file to notice is the `projectName.csproj` file that contain metadata about the project. I assume for now that it acts like a `package.json` where it store things such as the version type *(in our case .NET 6)* and included packages
```xml
	<ItemGroup>
		<PackageReference Include="Microsoft.AspNetCore.Mvc.Razor.RuntimeCompilation" Version="6.0.0-preview.7.21378.6" />
	</ItemGroup>
```

### Project layout

- Project
	- `Dependencies` folder. This is where all the **packages** are located
	- `Properties` folder. At basic level this contain profile at which your web application are run showing the configuration such as port name.
	- `wwwroot` folder. This is where all the **static** files are located. Files such as `.html`, `.css`, `.js` and `assets` of the web application.
	- `appSetting.json`. This is a json file where all variables are stored so the web application can access. To me this might sound like a `.env` file.
	- `Controllers` folder
	- `Models` folder
	- `Views` folder
	- `Program.cs`. The `app.js` of the web application to start the web applicatoin and running of the application.

### Routing
Just like *React.js* or any web application there will always require **routing**. That is in the `ASP.NET Core MVC`, the routing is implemented in the `Program.cs` mainly this line,
```csharp
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");
```

Here the default routes are `/home/index/id`. These are set incase routes are not fully provided, such as `/home/` where it's missing *index* and an *id* which will be valued `index` and `null`.

The backend of it all comes from the **MVC files** located at the root of the project folder.

#### Controllers
- `Controllers` is the folder where all the routes will occurs. By default there should be a `homeController` where there exist code like,

```csharp
public IActionResult Index() { return View(); }
public IActionResult Privacy() { return View(); }
```
The explanation for above, is that if we do something like `/home/index` then program will know that it wants to execute the `Index()` which returns the `View` for index. In this case it's just a simple `View` in the `Views` folder

#### Views
- `Views` is the folder, where we store all our outputs in html. It like a `component` in React.js where all the **sections of UI** are located. What different is that it allows for templating. There should exist a `Shared` folder which contains files,
	- `_Layout.cshtml`. A file that is the template for a html view
	- `_ValidationScriptPartial.cshtml`. A file where all the script for the `_Layout`.
	- `Error.cshtml`. Simple erro handler view

Let's take a look into a `view.cshtml`

```csharp
@{
    ViewData["Title"] = "Privacy Policy";
}
<h1>@ViewData["Title"]</h1>
<p>Use this page to detail your site's privacy policy.</p>
```

Here we can just add the important **body** for the html. The `_Layout` will be applied taking the above as like a `{{ content }}`. One important note here is that you can now defined variables using **key/pair** values within `@{}`. This allows us to defined variables. *Not sure why as of yet.*  

### Taghelpers
From my initial understanding, it just a way to easier create html from the **server side**. An example is,

```csharp
// Using tagHelper
using (HTML.BeginForm("Index", "Users", FormMethod.POST, new {@class="form-control" } ))

// HTML
<form class="form-control" method="POST" asp-controller="Index" asp-action="Users"/>
```

To help model our data that to be used in view, we can use the `Models` folder to store all the tables of the database.

#### Models
Here in the `models` folder, we can create a **C#** class by,
- Right click
- Click `Add`
- Click `Class`
 
 Like any class creation, you can define the variables that will be defined in a specific database, I'm going to try create a watchlist, where it store all the movies I've watched.
```csharp
using System.ComponentModel.DataAnnotations;

namespace WebDemo.Models
{
    public class Movie
    {
        [Key]
        public int Id { get; set; }
        [Required]
        public string Name { get; set; }
        [Required]
        public DateTime StartDate { get; set; }
        public DateTime FinishDate { get; set; }
    }
}
```

A useful library is `System.ComponentModel.DataAnnotations` where it will provide parameters such as `Key` and `Require` to denote the attributes in the model, that they are a **primary key** and a **required non null** value respectively.

The database to use would be the using **MySQL** and to connect it to the ASP.NET web application we will config in the `appSetting.json`. That is adding,
```js
"ConnectionStrings": {
	"DefaultConnection": "SQLServer"
}
``` 

#### NuGet 
This is the `npm i` or the `pip install` of the `C#` environment. We can search the marketplace to download packages form visual studio.

In case you don't have nuget packages, you can change the package source, by adding 
```csharp
nuget.org as package name
https://api.nuget.org/v3/index.json as package source
```

Coming back to the database we need to install `EntityFrameworkCore` in the nuget package manager and adding it in the `Program.cs`
```csharp
using Microsoft.EntityFrameworkCore;

builder.Services.AddDbContext<ApplicationDbContext>(options => options.UseSqlServer(
	builder.Configuration.GetConnectionString("DefaultConnection")
));
```

Another important step is to migrate the class in `Models` to the database as it know how to use and interact with the class and tables. Todo so, the best way is too

Coming back to the database, we will need to install `EntityFrameworkCore.Migrations` which allows for interaction. Then in nuget commnadline, we can use the command,
`add-migrationname` to add the migrations in a newly created file `Migrations`

Once we have the files that contain `Up` and `Down` function we can use the,
`update-database` to push the implementation to the database.

#### Creating a form
So now we have the model and connection to the database, we have to allow users from the web to add and edit, basically CRUD the data. Todo so, we can create a **view** in `Views` and create a **Form** that takes in the attributes of the *Movie model* as **html input**.
```html
@model Movie 	<!-- like importing the class Movie from models-->

<form method="POST">
	<input asp-for="Name" type="text"/>
	<input type="submit" class="btn btn-primary"/>
</form>
```
Here is a simple example for the **tag-helper**, `asp-for` binds with the attribute *Name* in the Movie model. That way when the form is request, then that input will be the value for the `Name` attribute in Movie.

Also, when we send a request (in this case a *POST* request) to the web application, we need to be able to handle it in the `controller` via an `IActionResult`.

```csharp
// _db = db // database loaded
[HttpPost]
[ValidateAntiForgeryToken]
public IActionResult Create(Movie obj) {
	if (obj.Name == obj.DisplayOrder.ToString()) {
		ModelState.AddModelError("name", "The DisplayOrder cannot exactly match the Name.");
	}
	
	if (ModelState.IsValid) {
		_db.Categories.Add(obj);
		_db.SaveChanges();
		TempData["success"] = "Category created successfully";
		return RedirectToAction("Index");
	}
	return View(obj);
}
```

Important note in the code above, is `[HttpPost]` and `[ValidateAntiForgeryToken]`. `[HttpPost]` tells the view that if there is a **POST request** then this `create()` method will be invoked and for **security purpose** the `ValidateAntiForgeryToken` is added.

Another thing to note, is the server side rendering. through my experience (PHP), I validated server side if manually checking all POST arguments are valid by using regex and validation checking on the SQL side. Here, what I see is that ASP.NET we can use `ModelState` todo various side server input validations to see if the inputs are check.

For more client approach, the result is the same. Using javascript to perform checks on the inputs. Todo that in ASP.NET, we'll need to use the `<partial>` tag in the view html to load in the scripts we mentioned early in `Shared/_ValidationScriptPartial.html`. Like so,
```html
@section Scripts{
	@{
		<partial name="_ValidationScriptsPartial" />
	}
}
```
 The remaining, *edit, delete* will use similar methods as the create information about. I won't go into much details.
 
### Conclusion
This is a very brief and rush first take using ASP.NET and C#. It took around 2 hours to learn this much. In my opinion through, it is great, using Node.js or python is so much easier and simplier. It's like the *Angular* for server side and web application. Very heavy loaded for something that can be deal with using lightweight methods like Vue or React. Again I believe it is suitable for enterprises and full on scale projects so it wouldn't be bad to use these stronger and much supportive frameworks. 