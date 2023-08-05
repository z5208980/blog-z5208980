---
title: "First Time with Azure DevOps"
date: "2023-01-13"
tags: ["Developer", "Azure"]
image: ""
gradients: ["#ed4264", "#ffedbc"]
---

## Azure DevOps: Creating and Building a Release Pipeline
*As part of my first time using Azure DevOps and beginning introducted to CI/CD. This is a short guide or notes on my experience.*

**Azure DevOps **provides a powerful platform for managing the entire software development lifecycle, from version control to **build and release automation**. In this blog post, we will focus on the process of creating and configuring a build and release pipeline in Azure DevOps.

### DevOps Repos: Managing Codebase
To start with Azure DevOps, you can easily import an existing codebase into a repository. By navigating to the `Repos` section and selecting Files, you can push your codebase using **Git**. If you need to clone a repository locally for development, you can use the git clone command, typically in the format `https://dev.azure.com/{projOwner}/{projName}/_git/{repoName}`.

Please note that *stakeholders* with **limited access **might not be able to view the Repo tab or clone repositories. In such cases, you need to **change the access level in Azure**.

When multiple individuals are working on different features or implementations within a project, branching becomes essential. You can create a branch locally using `git branch {branchName}.` To access the branch, use `checkout {branchName}`. After making changes, you can add and commit them. Since the branch was created locally, it doesn't exist in the remote DevOps repository. Therefore, you need to push it to the origin using `push origin {branchName}`. To incorporate updates from the branch, you can use `pull origin {branchName}`.

When new code is pushed to the DevOps repository, it appears in the `Files` section of `Repos`. To merge these changes with the *main master* branch, you need to create a *Pull Request*. In DevOps, there are multiple ways to create a Pull Request, such as through the *three-dot icon* on the `Branches` section or directly in the Pull Request section of Repos.

### Build Pipeline: Ensuring Code Quality
A **build pipeline is a script or series of tasks** that build and validate the project. To create a build pipeline, navigate to `Pipelines` and select Pipelines. Here, you can define the steps and tasks necessary to build and test your code.

A build pipeline typically includes steps such as **restoring dependencies, compiling the code, running unit tests, and generating artifacts**. Azure DevOps provides a variety of built-in tasks and extensions to help you customize your build pipeline according to your project's requirements. By configuring triggers, you can automate the build process based on code changes or a predefined schedule.

### Release Pipeline: Automating Deployment
**Release pipelines are responsible for deploying the codebase to various environments or services**. In most cases, this involves deploying to Azure services, such as *Azure Web App.* To create a release pipeline, navigate to `Pipelines` and select `Releases`.

To ensure flexibility and remove coupling, it's a best practice to use variables in your release pipeline. These variables can replace **environment-specific** settings in configuration files like `app.settings` or `.env`. By utilizing the `Variables` tab and creating **Variable Groups**, you can define *key-value* pairs for each stage in your release pipeline. These variables can be accessed throughout the pipeline, allowing you to easily manage environment-specific configurations.

Once your release pipeline is configured, you can define the deployment stages, including any necessary** approval processes**. Azure DevOps provides features for manual or automated approvals, allowing you to control when and where your code is deployed. By defining artifacts and linking them to your build pipeline, you can ensure a seamless flow from code changes to deployment.

## Conclusion
Azure DevOps offers a comprehensive set of tools for managing code, building, and releasing applications. By utilizing the features provided by Azure DevOps Repos, Build Pipelines, and Release Pipelines, you can streamline your development process and automate the deployment of your