---
title: "SQL + .NET Core + Angular"
date: "2022-01-23"
tags: ["Web", "Developer"]
image: ""
gradients:  ["#76b852", "#8DC26F"]
---

### SQL + .NET Core + Angular
This is another work session that I needed to learn in terms of .NET application. This time it's more of a full stack web implementation with both frontend and backend components.

#### Setting up SQL Server

**Requirements**
- SQL server (https://www.microsoft.com/en-au/sql-server/sql-server-downloads)
- SQL SMSS (Interface for server) (https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15)

To create a *server instance*, goto
- Install -> **SQL stand-alone installation**

The install should be choicen as default except on these selections,
In **Feature selection**
-	select **Database Engine Services**

In **Database Engine Configuration**
- select **Mixed mode**, and optionally set a **password**
- **Add current user**

Then coming on default installation, everything should be setup

To use the server, we need to use the **SSMS software** and enter **.** as SQL name, then the first SQL server should be the created server.

#### Installing .NET core

Simply just download *Visual Studio* from Microsoft

#### Installing Angular

Follow the instructions here, https://angular.io/cli. or simply just open a terminal and npm install angular
```bash
npm install -g @angular/cli
```

### Database SQL

This is more a revision of my DB skills, but to create and use a database in SMSS, first we need to look at the **Database** folder. To basically do anything on the database, we'll need to **new query**.

**Note:** When using queries, MAKE SURE that you *new query* on the desired location. Eg, if you want to create table in db, goto the the db and to the tables and then new query.

#### Create Database
Since our db is empty, the `CREATE` will our use to create a **Database** and **Execute**.
```sql
CREATE Database WatchDB
```
This command will create a db named *WatchDB* that stores all the titles of movies, or tv series that I've watched.

#### Create Table
To popular our database, we'll need to create **Tables** in our db. To do so, just use
```sql
CREATE Table Title (
	TitleId int identity(1,1), /* starts a 1 and increments 1 for new entry*/
	Title varchar(100),
	StartDate int,
	EndDate int
)
```
This command will create a table *Title* in WatchDB.

**Note** we can use the `.sql` from our new query as a playground file. To *execute* a specific sql, we'll need to **highlight** the code, and run execute.

To **insert** a instance or a tuple into a table,
```sql
INSERT into Title values ('Eternals', '2022-01-21', null);
```

To **Query**,
```sql
SELECT * FROM Title;
```
### REST API
To create a .NET core Web API, we'll need to user their template. This will give us a sample web API of *whetherforcast*, which if we run (it'll be on localhost) it'll prompt us to the swagger documentation. With one *Getter method*.

Now the template works, typically in .NET core application, the MVC is the approach in designing application, hence a **Models** folder with all the *Tables* of the database in form of **Class** is needed.

Recall in our Title Table,
```sql
TitleId int identity(1,1),
Title varchar(100),
StartDate date,
EndDate date
```

It'll be best to include all the attributes from the sql table into the class model.

#### Connecting API to Connect
```sql
"ConnectionStrings": {
	"DefaultConnection": "Data Source=.; Initial Catalog=WatchDB; Integrated Security=true"
},
```

This goes in **appsettings.json**. Like I said in the .NET core web application, **appsettings.json** is like a .env file that storage variable for the project.

To use **sql** in our web API, we'll most likely need a nuget library called *SqlClient*.

Once we setup a variable to the db, we need to create a controller, that stores the implementation of the **endpoints** for the web api.

```csharp
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

using Microsoft.Extensions.Configuration;   // Used to config our db
using System.Data.SqlClient;    // library to help process SQL
using System.Data;
using WatchList_API.Models;    // To load in the Models that conform with the db

namespace WatchList_API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class TitleController : ControllerBase
    {
        private readonly IConfiguration _configuration;

        public TitleController(IConfiguration configuration)
        {
            _configuration = configuration;
        }


        [HttpGet]
        public JsonResult Get()
        {
            string query = @"SELECT TitleId, TitleName, StartDate, EndDate FROM dbo.Title";
            DataTable table = new DataTable();  // From sqlClient library
            string sqlDataSource = _configuration.GetConnectionString("DefaultConnection"); // Makes a connection

            SqlDataReader myReader;
            // Open connection to db and run query, and load reult in a table with help from the sqlClient library
            using (SqlConnection myCon = new SqlConnection(sqlDataSource))
            {
                myCon.Open();

				// Is use to query the connectted db
                using (SqlCommand myCommand = new SqlCommand(query, myCon))
                {
	                // Load to a tableformat that will be easy to turn to JSON
                    myReader = myCommand.ExecuteReader();
                    table.Load(myReader); ;

                    myReader.Close();
                    myCon.Close();
                }
            }

            // Result the table as JSON format
            return new JsonResult(table);
        }
    }
}
 ```

The code has been commented to help get an understanding of an endpoint of our web api. This the snippet, it is a `GET` request, that does a simply connection to the db, using the *sqlClient* library and executes the SQL. the result is store in a table and returned in JSON object. The rest would be the same for other http methods such as `POST`, but instead you'll need to change the query to `INSERT into table VALUES (...)` or `PUT` (`UPDATE`) and `DELETE` (`DROP`).

That's the backend complete. Time for the frontend using *Angular*.

### Frontend
For the frontend, the company I'm interning for uses Angular, so I guess Angular will be the tech added to this stack. Note however, I did learn Angular before so this section may be brief.

```bash
ng new	# Start new Angular project
ng start --open	# Run server

ng generate component componentName # Creates component
ng generate service ServiceName # Generate Service (used for API)
```

In my case, the watchlist will only need a Title component that has functionality such as *add* or *edit*. Hence,
```bash
ng generate component title
ng generate component title/add-title

ng generate service service-api
```

Once all the necessary components are generate, you'll need to config the `app,module`, adding the service and other libraries.
```ts
import { ServiceApiService } from  './service-api.service';

import { HttpClientModule } from  '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from  '@angular/forms';
```

In the service api, you'll need to add these library to help with making API called to the API and allowing the component with the updated information
```ts
import { HttpClient } from  '@angular/common/http'; // ajax request
import { Observable } from  'rxjs'; // used to help entire webpage know about the ajax information via subscribe pattern
```

then in the class is where all the api call with exist an example of the endpoint `/api/title` for `GET` that was written in our web api will be, 
```ts
getWatchlist(): Observable<any[]>{
	return  this.http.get<any>('https://localhost:7145/api'+'/title');
}
```

Then whenever you want to call the service in your component, simply load the service in the component and subscribe to it. That's all.


