---
title: "Learning Hugo"
date: "2020-06-15"
tags: ["Developer"]
image: "https://www.dropbox.com/s/i1ezbamlwsynljq/hugo.png?raw=1"
gradients: ["#ff9966", "#ff5e62"]
---

## Abstraction
This is my first blog, so you’ll need to excuse my noobness in creating posts for a while. As my first blog, I think it was only write to introduce myself, but I had something in mind. Instead, over these past few hours, I’ve been learning HUGO, a static site generator that allow users to create dynamics sites! Since I had a hard time learning and wanted to create my own theme. This post will hopefully give your a lot of insight to customising different features of the website without the need of a theme! I’ll skip the basic and only focus giving information on the design of HUGO.

## list.html
The `layouts/_default/list.html` is a html file used to display your posts (blogs). Stuff like

`{{ .Title }} {{ .Description }} {{ .Content }} {{ .TableOfContents }}`

### Looping Through post
In `list.html` to loop through and display all **posts**

```html
{{ range .Pages }}
    <div class="">
        <a href="{{ .URL }}">{{ .Title }}</a>
        {{ if .Summary }}
            <div class="">
                {{ .Summary }}
            </div>
        {{ end }}
    </div>
{{ end }}
```

Here we are looping through `.Pages` which is the `content` folder Each “Page” has a `{{ .URL }}`, `{{ .Title }}`. If the Page is a post then it will contain a `{{ .Summary }}` else its a folder, meaning the url will href you to the page will all the posts or folder in it.

## Single.html
The `layouts/_default/single.html` is a html file used to display your posts (blogs). Stuff like

`{{ .Title }} {{ .Description }} {{ .Content }} {{ .TableOfContents }}`

### Table of Content
Adding this HUGO tag

```html
<div>
    {{ .TableOfContents }}
</div>
```

will produce this in html

```html
<nav id="TableOfContents">
  <ul>
    <li><a href="#header-2">Header 2</a></li>
    <li><a href="#table-of-content">Table of Content</a></li>
  </ul>
</nav>
```

Hence to edit TableOfContents just take the id and style it will css!

```css
#TableOfContents { }

/* List */
#TableOfContents ul { }
```

### Pagination
To Paginate your posts, first goto your `config.toml` add the key `paginate: n` where n is the number of post u want to display each pagination.

then goto `list.html` where your posts are displayed. set a paingation varialbe

```go
{{ $paginator := .Paginator }}
```
In your loop, your `.Pages` become `.$paginator.Pages.` So your entire code is

```html
{{ range $paginator.Pages }}
    <div class="">
        ...
    </div>
{{ end }}
```

in your `partial` folder, add this a `pagination.html` and add it to list.html

```go
{{ partial "pagination.html" $paginator }}
```

Making sure that pass in the `$paginator` var.

your `pagination.html` goes something like this.

```go
{{if .HasPrev}}
    <a href="{{ .Prev.URL }}">Newer Posts</a>
{{end}}
    <span class="page-number">Page {{ .PageNumber }} of {{ .TotalPages }}</span>
{{if .HasNext}}
    <a href="{{ .Next.URL }}">Older Posts</a>
{{end}}
```