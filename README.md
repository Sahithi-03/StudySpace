### About the project
The StudySpace is a mini utility space for students which consists Information storage, simple Kanban style task tracker, Stopwatch, and Quotes.

**InfoStore** - for storing revision notes, important links in cards style. Users can view the information cards in the most recently created format, edit the already saved notes, and delete the existing notes.

**Task Tracker** - mini kanban style format with 2 tracks to store the tasks in yet to complete and already completed format. Users can view the tasks with recently created being at top and shift the tasks between two tracks and delete the tasks from both tracks.

**StopWatch** - a tool which helps students to stay focused and helps them to level up their speed and analytical thinking in critical environments.

**Quotes** - gives the user a new random Quote everytime they visit the page, quotes can help boost confidence in students, by providing a choice, it makes them more confident to finish the tasks more effectively.

### Distinctiveness and Complexity
This project is distinctive compared to the previous projects, as they mostly have information sharing between users in different forms like mails, comments, and a sample of public website. But in this case, there is no need to share the information between the users.

The project provides tools for the user and keeps track of the information given by the user in the database and there is no connection between the users to communicate or share responses like in other previous projects. The main aspect of this project concentrates on the students/users to improve themselves everyday. 

This project revovles around the students and supports them in the core aspects.
The complexity is in the frontend design, where I have included animations for certain elements and designed the logo in figma and included it in the project to make it look professional and also improved the design in iterative format until the last moment, connecting the backend framework with the frontend and debugging the errors. 

The project consists of more than one tool and this rises the complexity to include the tools in the application and to make it easy for the user to navigate the tools within the application. It has utilized 2 models on the backend and javascript in the front-end. It is mobile-responsive as the meta link was used in the `layout.html` file. 

The tools are small in number but not overwhelming to use and keeps it packed which could help students to be more efficient. These features focuses on the core aspects in this busy world to be of help for students to stay focused.

### Details

- `capstone folder` contains the capstone Django project files which are exists when a Django project is created and including the applications urls in the `urls.py` is crucial.

- `studyspace folder` is the application of the capstone project. It contains the static, templates folders, and pre-built files.

- `models.py`, which contains models of the application tools Info & Tasks and `views.py` which contains the functions which processes the requests from the frontend and stores the information in the database, also connects the `urls.py` file, which is used to traverse through different pages in the application. 

- `layout.html` is the base template file. It contains the navabar and necessary links of Bootstrap version 5.3 (CSS & JS), Material icon, and static `style.css` CSS and `script.js` JS files.

- `index.html` inherited the `layout.html` file and is the main page after users signed in to their account and also a landing page for new users. This page provides the links as buttons to navigate to different tools and some animations related to the elements in the file.

- `register.html` inherited the `layout.html` and this is the gateway for new users to create an account to use the tools. It contains logo and input boxes for information and register button to save the details in the database.

- `login.html` also inherited `layout.html` file and it is the gateway for existing users to signin and to see their saved Info and tasks.

- `list.html` also inherited the `layout.html` file and the main page of InfoStore tool, which has all the information stored in the card format. Each card has a view and a delete option.

- `add.html` also inherited the base template file and it was created to store the information in the database by using a Save option. The user have to give the title and text content and the created on will be automatically stored in the database through django. It also contains necessary javascript code to save the content using fetch and method post.

- `display.html` also inherited from base template file and connects the view button of the `list.html` file. The purpose is to display the information like title, text, and created on date in the more open space. It also has a Edit option to edit the content of the card, which connects to `add.html` with pre-exisiting information.

- `quotes.html` also inherited from the base template file and displays images from picsum and random quote taken from dummyjson.com for developement purposes. On every refresh the image and the quote will change and new ones will be displayed. It also contains script block to use the fetch api to fetch new quote on refreshing the page.

- `task.html` also inherited from the base template file and it displays a mini Kanban style task tracker where new task can be added and existing tasks can be shifted from task and completed columns through icon buttons. There is a delete option for all tasks irrespective of the grouping, where the tasks can be deleted forever.

- `stopwatch.html` also inherited from the base template file and it displays the hours,mins and seconds time watch where buttons are provided to start/pause, flag the time which will be displayed below and renew the timer to start from zero.

- `static/Frame 1 (1).svg` contains the design of the logo of the website. Designed using Figma resources.

- `static/script.js` contains the javascript code related to the base and remaining template files.

- `static/style.css` contains the css styling code related to the base and remaining template file.


### How to run

To run the project from terminal and access the files you can use the following steps:

Download the project zip file and use `cd` to navigate into the root project folder `capstone` and install the necessary dependencies by running the command 
> pip install requirements.txt

in the terminal and run the following command in terminal

> python manage.py runserver  

to run the django server and paste the link

> http://127.0.0.1:8000/

in the browser to go to the website.


### Additional info
I have created a simple logo using figma and saved it in `svg` format to use in the project for a refined look.