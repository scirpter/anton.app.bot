# anton.app.bot
An "exploit" that will solve your exercises on https://anton.app.

This bot is NOT done and might not solve every exercise type.

# How to find Lesson Url

**Disclaimer:** While this guide specifically refers to Chromium Edge, the general steps outlined may also be applicable to other web browsers with developer tools for network analysis. 

### Step 1: Open Chromium Edge
Launch your Chromium Edge web browser on your computer.

### Step 2: Navigate to Anton.app
Enter the URL "Anton.app" in the address bar of Chromium Edge and press Enter to navigate to the website.

### Step 3: Open DevTools
Right-click on any space on the webpage and select "Inspect" from the context menu. This will open the DevTools panel in Chromium Edge.

### Step 4: Access the Network Tab
In the DevTools panel, you will see several tabs such as "Elements", "Console", "Sources", etc. Look for a ">>" (more)![grafik](https://user-images.githubusercontent.com/92308299/231522043-9f811e31-ad12-494f-b2e0-42aa987a55b2.png) button or a similar icon, usually located in the top-right corner of the DevTools panel, and click on it to reveal additional tabs. Then, switch to the network analysis panel on the "Network" tab.

### Step 5:  Trigger the Network Request
Perform the action on anton.app that will load the correct exercise block. This may involve reloading the current webpage or navigating to a different webpage on anton.app. If you navigate to a different webpage, clear the network log by clicking on the "Clear" button![Screenshot 2023-04-12 174527](https://user-images.githubusercontent.com/92308299/231511972-5a29a162-9e62-4958-86ed-56145b823e07.png) in the top left corner of the network panel, to ensure that only the relevant network request is captured. 

### Step 6: Filter and Find the Lesson Url
At the top left corner of the developer tools, you should see a search bar. Below it, you will find captured traffic data, which may look something like this: 
![grafik](https://user-images.githubusercontent.com/92308299/231515495-c84ef1e2-d803-46c1-a2bd-c877b318f8f1.png)
To find your lesson URL, type `?fileId=level` into the search bar. After that, you should see only one URL remaining, which is your lesson URL.
If you open the link you received, it should start like  `{"title":`

If you still need help, please feel free to create an issue, and I will do my best to assist you as soon as possible.

