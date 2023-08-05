---
title: "Azure Blob Storage Dotnet"
date: "2022-08-30"
tags: ["C#", "Developer", "Azure"]
image: ""
gradients: ["#8EC5FC", "#E0C3FC"]
---

## Azure Blob Storage
Azure Blob Storage (By Microsoft) is mainly used to store *"blob"s* of information, which typically consists of unstructured or binary data. The data will be stored in the cloud. These blob data can then be accessed via the Azure Storage API, or via CLI. For use in projects, this will be mainly using the REST API. In this writeup, it'll mainly be C# which has a Client Library available in .NET. Of course, what comes to mind is that it can be used for distributed access or simply backup.

Documentation for .NET Libraray (NuGet): https://docs.microsoft.com/en-us/dotnet/api/overview/azure/storage

## Requirements
We will need Azure Blob Storage Library. To do so, go to the project's `Dependancy > Packages` and type `Azure.Storage.Blobs` and *Add* the NuGet package. Now we can use this to connect to Azure Storage, which brings us to the Azure service. 

Note: *Alternatively* this can be done via the cmd line, 
```bash
dotnet add package Azure.Storage.Blobs
```

You can create a Blob Storage service by adding a *Resource Group* and adding `Storage > Storage account - blob, file, table, queue` to create a **Storage Account**

Once a Storage Account is used, we can add data in **Containers**. Essentially, containers are *Folders* where you can separate the type of data that is uploaded.  Once a container has been created, to gain access to the `ConnectionString` (which will be used in code), go to (in the Storage Account level) `Settings > Access keys`. There will be a field with **Connection string**.

For best practice like most ConnectionString in traditional DB access, we can set this value in `appsettings.cs`, but for simplicity, this will be a 

```csharp
using Azure.Storage.Blobs;
using Azure.Storage.Blobs.Models;
using System;
using System.IO;
using System.Threading.Tasks;

namespace BlobExample1
{
    class Program
    {
        // Maybe move to these variables somewhere
        const string ConnectionString = "DefaultEndpointsProtocol=https;...";
        const string ContainerName = "container";

        // Connect to container
        static BlobContainerClient _containerClient;

        static async Task Main()
        {
            // Create container
            //BlobServiceClient blobServiceClient = new BlobServiceClient(ConnectionString);
            //BlobContainerClient _containerClient = await blobServiceClient.CreateBlobContainerAsync(containerName);

            string filename = "filename.txt";
            bool success = await Upload(filename);
            Console.WriteLine($"Upload: {success}");

            Console.WriteLine("Getting filename of container:");
            await foreach (BlobItem blobItem in _containerClient.GetBlobsAsync())
            {
                Console.WriteLine($"- {blobItem.Name}");
            }
        }

        private static async Task<bool> Upload(string filename)
        { 
            // Create a file for uploading or downloading
            const string localPath = "path/to/file/";
            string localFilePath = Path.Combine(localPath, filename);
            try
            {
                // Get a reference to a blob
                _containerClient = new BlobContainerClient(ConnectionString, ContainerName);
                BlobClient blobClient = _containerClient.GetBlobClient(filename);

                Console.WriteLine("Uploading to Blob storage as blob:", blobClient.Uri);
                // Upload data from the local file
                await blobClient.UploadAsync(localFilePath, true);
            }
            catch
            {
                return false;
            }

            return true;
        }
    }
}
```

The above is a simple program that will be used to upload a file to the container, where the `Upload()` creates a client and finally prints a list of files in the container. A `ls` for the container.

Running this code will upload the file in `localPath\filename` to the container of the `ConnectionString`. Then in Azure, the file can be accessed. If the resource is inaccessible due to permission, an alternative is using the app called **Storage Explorer**. This can be downloaded here: https://azure.microsoft.com/en-us/products/storage/storage-explorer/.

Effectively this application allows for the attachment of a resource which in this case, is the Storage resource. In the application, go to `Select Resource\Storage account of service\Connection (Key or SAS)`. Here there will be a connection string field in which the connection string will be entered and connected next until the end. Then the directory and container can be accessed via the GUI.

### Microsoft Azure Storage Blob
Instead a project is using an older .NET framework, then the `Azure.Storage.Blobs` won't work as it requires **.NETStandard v2**. Hence we can download the deprecated version known as `Microsoft.Azure.Storage.Blob`. Connecting to a container is a bit more and will use different Classes.

```csharp
using Microsoft.Azure.Storage;
using Microsoft.Azure.Storage.Blob;
using System;
using System.IO;
using System.Threading.Tasks;

namespace BlobExample2
{
    class Program
    {
        // Maybe move to these variables somewhere
        const string ConnectionString = "DefaultEndpointsProtocol=https;...";
        const string ContainerName = "container";

        // Connect to container
        static CloudBlobContainer _containerClient;

        static async Task Main()
        {
            // Create container
            if (!CloudStorageAccount.TryParse(connectionString, out CloudStorageAccount storageAccount))
            {
                throw new Exception("Could not create storage account with connectionString");
            }
            var blobClient = storageAccount.CreateCloudBlobClient();
            _containerClient = blobClient.GetContainerReference(containerName);

            string filename = "filename.txt";
            bool success = await Upload(filename);
            Console.WriteLine($"Upload: {success}");
        }

        private static async Task<bool> Upload(string filename)
        { 
            // Create a file for uploading or downloading
            const string localPath = "path/to/file/";
            string localFilePath = Path.Combine(localPath, filename);
            try
            {
                string filename = Path.GetFileName(localFilePath);
                // Upload data from the local path
                var blob = _containerClient.GetBlockBlobReference(filename);
                using (FileStream fs = File.Open(localFilePath, FileMode.Open))
                {
                    await blob.UploadFromStreamAsync(fs);
                }
            }
            catch
            {
                return false;
            }

            return true;
        }
    }
}
```