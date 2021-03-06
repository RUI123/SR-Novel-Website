# SR-Novel-Website
## 1. Overview 

### 1.1 Member:    
        Shipeng Yu, Ruifeng Zhang

### 1.2 Goal:  

Using Python, Django, bootstrap and other HTML, and CSS, to build a website that extends our knowledge of developing websites.

### 1.3 Website purpose:    	
   
As the development of SR-Novel Websit goes, we first have an idea on creating a website, that allows users to share their books by uploading each chapters of books.  After that, users can just read through each chapters of books which they like. Users can enjoy reading through our website.  However, it is not a good idea to just share book directly due to copyright of books.  As result, we decide to focus on a purpose to let users to write and share their own books on our websites. Each user can be a writer. They just write what ever they like.  If one of writer finds a book is interesting, they can just click a like.  As the process goes, our website will develop a new community of new writers for writing books.  It can also be a place to inspire writers with new idea of writing a book.


### 1.4 Website Design:	

Our project uses Django, bootstrap, and existed website templates to implement a website. With the desire of having a well-formed Front-End, the revised templates of our website are needed. However, the project does not mainly focus on Front-End. As result, we put more effors on securing urls of website and implementing functional services that website provides. More details of the website will appear on the section of UI Design.

## Getting Started

These instructions to run the project will be int the follwoing under Windows10 Operating System.

### Project Run requirement

        The latest version of Python3
        The latest version of Django
        Download packages tool pip
        Django packages with Crispy Forms and Pillow
        Setting Environment Variables

### Installing

 1. Installing Python3 and Django.
        The following website will have the full instruction to download Python3, pip, and Django
        https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment

 2.  Make a copy of current project to your local machine
 
 3. Having a running Command Prompt, and swtich intto the project folder with manage.py file
 
 4. Before running the program, two packages and two environment variables need to be set up
 
 5. Run following commands to install two packages, Crispy Forms and Pillow
 
        pip install Pillow
        pip install django-crispy-forms
 6. Setting environment variables for your real email address and password
 
        1) search for environment variables in your windows10 machine
        2) go to advance setting, and then click on evironment variables
        3) click on new to create a new environment variable, 
        set the variable name as [EMAIL_USERNAME] with value, [your email address]. 
        4) save the previous variable, then create another new variable 
        with name [EMAIL_PASSWORD], and value [your email password]
        5) Again save the variable for password, it is better to close the 
        Command Prompt and reopen it again to let the environment take effect.
        It may fail the setting without reopen the Command Prompt
        
 7. Now in the Command Prompt, you can run following command to run the project
 
        py -3 manage.py runserver
        
 8. Enter following address on your blowser
 
        127.0.0.1:8000/
        
 9. You are now able to running the website from browser in your local machine
 

The detail figures of the running website will be in the UI secction.


## Built With
Django, Python, HTML, CSS, Javascript



## UI(User Interface) Section

### 4.1 User

4.1.1 Sign up

4.1.2 Login in

4.1.3 Forget password/Change password by Email

4.1.4 Create Book/Chapters

4.1.5 Delete Chapters (author required)

4.1.6 Edit Book information/Chapter information(author required)

4.1.7 Add Favorite for book, which is book like number add 1, one of evaluation for ranking.

4.1.8 Add marker for chapters, which allows user mark this chapter and add the link to profile page.

4.1.9 Own Profile Page

4.1.9.1 Username

4.1.9.2 Email address

4.1.9.3 Profile image

4.1.9.4 About me

4.1.9.5 Favorite books including book link

4.1.9.6 Marked Chapters including chapter link

4.1.9.7 Number of Created book


### 4.2Book

4.2.1 Book Chapters/content

4.2.2 Book Detail

4.2.2.1 Title

4.2.2.2 Author

4.2.2.3 Genre

4.2.2.4 Like Number

4.2.2.5 ISBN

4.2.2.6 Word Count

4.2.2.7 Chapter Count

4.2.2.8 Date upload

4.2.2.9 Summary


### 5. Details and Design Of Website, like memtioned before we are not super focus on front-end (UI Folder)
Of course, their are more page that we did not show over here.

5.1 Main page

![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/index.png?raw=true)

5.2 User Part (The only part that We do not user default form style, instead using free templates to connect our back-end)
5.2.1 Create Account 
![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Create%20Account%20Page.png?raw=true)

5.2.2 Login Page
![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Login%20Page.png?raw=true)

5.2.3 Reset Password by receive email from website
![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Email%20Send.png?raw=true email send)

![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Email%20from%20website.png?raw=true)

![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Password%20Reset%20Page.png?raw=true)

5.3 Account Drop Down (If user logged, then it will show username, otherwise will show "login" allow user to login

![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Account%20Drop%20Down.png?raw=true)

5.4 Book Detail Page (If user is author It will show update book and add new chapter button)

![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Book%20Detai%20Page%20with%20Author.png?raw=true)
![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Book%20Detail%20Page.png?raw=true)
![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Chapter%20List%20Botton%20side%20of%20Book%20Detail%20Page.png?raw=true)

5.5 Book Library Page which contains all the book in the website

![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Book%20Library.png?raw=true)
![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Book%20Library%20Bottom%20side.png?raw=true)

5.6 Book Upload Page allow user Create book

![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Book%20Update%20Page.png?raw=true)
![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Book%20Update%20Page%20bottom%20side.png?raw=true)

5.7 Book content page (different if user is author or not) 
![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Content%20Page%20not%20author.png?raw=true)
![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Content%20page%20author.png?raw=true)


5.8 Chapter Delete and Upload Page (if User is the author of this book, he will have permission to do this 

![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Chapter%20Delete%20Page.png?raw=true)
![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/Chapter%20Update%20Page.png?raw=true)

5.9 Profile Page
![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/ProfilePage2.png?raw=false)


## Acknowledgments
Inspire by the online novel websites




