## Mtaa
## It's a web application that allows members of the neighbourhood to view and post events , alert , parties etc that are happening or going on.
### 24 March 2019
#### By **[Francis T Karagu]**

## Description
It's a web application that allows members of the neighbourhood to view and post events , alert , parties etc that are happening or going on.

## Specifications
### Who is the target User?
* Neighbourhood members who wants to be kept updated on the current events.

### Front-end/User Interface Logic Objectives
* By default the page will load and provide two options.
* Sign in: This section will be used to authenticate users on the application.
* Mtaa (Home): This is the landing page of the application.

### Back-end/Business logic Objectives
* The application is using a POSTGRES database to store data.
* Once a user has accessed the page she/he can post or review what has been posted.

### Behaviour-Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Create User | Enter username, Email and password | Redirected to sign in. |
| Sign In | Click on the Sign In and enter username and password | Loads the home page. |
| Post | Click on the Post to view posted info | Loads all posted Info. |
| Option | Click on the Option to create Business or Neighbourhood name | Loads all required detail for creating Business or Neighbourhood. |
| Dashboard | Click on the Dashboard to access Admin Interface | Loads the admin page. |
| Contacts | Click on the Contacts to access page | Loads all the contacts. |

## Prerequiites
    - Python 3.6 required
    - Django
    - POSTGRES

## Application link
Here is a live working link https://thashmtaa.herokuapp.com/

## Set-up and Installation
    - Install python 3.6
    - Install Django

    Incase you need to access / improve the application please follow the below steps
    1.  Use this command $ git clone <https://github.com/Fkaragu/Mtaa.git>
        This will clone the projects repository into a local folder on your device.
    2.  Open the files with an editor( preferably Atom. )
    3.  Study the code. learn from it. Improve on it.

## Known bugs
No known errors.

## Technologies used
    - Python 3.6
    - Django
    - HTML
    - Bootstrap

## Support and contact details
In case of any problems reach me through my email:fkaragu@gmail.com

### License
Copyright (c) {2019} **{Francis Thande Karagu}**
Permission is hereby granted, free of charge, to any person willing to obtain a copy of this program for personal use. However if the program will be used for commercial gain then a royalty fee will have to be paid to the author of the program.
