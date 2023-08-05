---
title: "Creating First Chrome Extension"
date: "2020-07-05"
tags: ["Developer"]
image: ""
gradients: ["#130CB7", "#52E5E7"]
---

## Abstraction
This was my experience when creating a chrome extension for the first time. Honestly, I didn’t think it was hard. This was only because I’ve coded in Javascript before. It’s really not much of a learning curve. The only thing new was understanding the Chrome Extension APIs that allows us to manage tabs, run scripts and store data.

### Requirements Files
- manifest.json
- icons
- popup.html
- popup.js
- background.js

## manifest.json
the `manifest.json` is a json file that is used to store information about how the extension will work.

*This was the manifest.json to run my tally click extension.*

```json
{
    "name": "Click",	// Required
    "version": "1.0",	// Required
    "manifest_version": 2 	// Required
    "description": "Tally your clicks, and touch on all devices",
    "permissions": [ // chrome extension addons
	    "storage",
	    "declarativeContent",
	    "activeTab",
	    "*://*/*"
    ],		
    "background": {	// script that will run the background
        "scripts": ["background.js"],
        "persistent": true
    },
    "icons": {	// icons display
        "16": "icon16.png",
        "48": "icon48.png",
        "128": "icon128.png"
    },
    "browser_action": {	// the frontend for extension
        "default_popup": "popup.html"
    },
}
```

## popup.html
The `browser_action` is used when the user clicks on the icon in the extension tab on a chrome browser. A popup will appear and this is where you can display more information and UI for your extension. It will be in html and hence, most of the time it named `popup.html`.

*My simple `popup.html` file where the `popup.js` is initialised to run the logic for the popup.*

```html
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="style.css">

        <script src="popup.js"></script>
    </head>
    <body>
        <div class="content text-center">
            <div class="header text-bold text-center">Total Clicks so far!</div>
            <div id="result" class="text-bold">0</div>
        <div>
    </body>
</html>
```

## popup.js
The `popup.js` used in the `popup.html`. This is where the logic for the popup.html will be.

*Here I took the result div in popup.html and got the clicks values store in a chrome extension API **storage** using `chrome.storage.sync`. After obtain that value it was only using JS to render to the DOM.*

```js
document.addEventListener('DOMContentLoaded', function() {
    let r = document.getElementById('result');
    const key = 'clicks'
    chrome.storage.sync.get(['clicks'], function(result) {
        console.log(`Total clicks: ${result.clicks}`);
        r.innerText = result.clicks;
    });
});
```

## background.js
The `background.js` is a script that is used as a listener. What it does is it allows the management of events in the browser. For my purpose its was listening for a click in each tabs and send a message to it so it can increment the click count.

*Its commented out, but there is code that basically is like a `eventListener` for tabs. You can get the browser’s tab using `chrome.tabs.query`. To run JS in the tabs, use `chrome.tabs.executeScript(tabId, { code: script }, () => {});`.

The code below shows how the each click was detected on stored using `chrome.storage.sync`*

```js
// adding script in each tabs for detection of clicks
// ...

chrome.runtime.onMessage.addListener(function(req, sender, resp){
    // const key = 'clicks'
    chrome.storage.sync.get(['clicks'], function(result) {
        let total = result.clicks;
        if(isNaN(total)) {
            total = 0;
        }
        console.log(result.clicks);
        total = Number(total) + 1;

        chrome.storage.sync.set({'clicks': total}, function() {
            console.log('Incremented');
        });
        console.log(`Total clicks: ${total}`);
    });
});
```