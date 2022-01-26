# Gamer Stories

## Contents

### 1. Introduction

### 2. UX

- User Goals

- Creator Goals

- Development Plans
 
I. Strategy

II. Scope

III. Structure

IV. Skelton

V. Surface


### 3. Features

### 4. Issues

### 5. Technologies

#### Languages used:

### 6. Testing

### 7. Deployment

### 8. Credits

# Gamer Stories

## Gamer stories is a blog targeting peoples who love video games. Could be anyone who plays or watch or read or make games, it is all about games. It is a place where stories can be shared with others. Talk about the latest video game releases or experiences from your favourite games.

## User Goals:

### 1. First time visitor:

- A gamer blog website what is easy to use

- A gamer blog website where the user can share their thoughts

- A gamer blog website where the user can connect with other pasionet gamers

### 2. Returning visitor:

- A gamer blog website where they can come back to share their stories with in a daily bases

- A gamer blog website where they have fun

## Creator Goals:

- User friendly site

- screen responsive on all devices

- to build a community and share passion about games

- connect people

## UX

I. Strategy

#### The focus of the blog:

Target audience:

- anyone who love video games

- new and returning bloggers

Demographics:

- age is not relevant

Psyhographics:

- playing games is a lifestyle

- people who want to join a gamer community

- play together

- talk about games

II. Scope

User requirements:

- Sign up or log in to the site by providing username and password

- post a comment

- edit or delete a comment

- like or dislike a comment

Admin requirements:

- has all the functionality as a user

- approve comments

- delete comments

III. Structures

![diagram](media/gamerstories.png)

#### Organization of structure:

Home page, new comment page, account page. 



IV. Skelton 

Balsamiq wireframe for windows and mobile screen

![gamer-stories](media/gamerstories-wireframe.png)

### 3. Features

Existing features:

On all pages :

- navbar

- sign in and out options

- On Comment page:

- logged in users can comment and like 

- from main page users can register, log in

#### Features to implement:

- create a post as a user:

- modify and delete a post as a user

- avatars can be selected when user is making registration

### Issues

Solved issues

- pagination issue

Empty page error

I run into that bug after implementing the createview feature in my views. I got the error message after loading the page in, the error came from the pagination, in models.py where the pagination number was given, that was causing the problem, it was to small, changed that for bigger number and than the bug was solved.

![pagination_error](media/errormsgpag.png)

Known issues and bugs to be solved

- page not found

After implementing the createview function, so users could post too, this error came up, after as a user logged in and tried to create a new post. Still working on this bug to solve it, tried to find it on [stackoverflow](https://stackoverflow.com/questions/60590738/the-current-path-post-didnt-match-any-of-these)
but unfortunately i could not solve this bug yet. 

![page_not_found](media/errormsg.png)

- alert message

Alert messages for notifications to the users, the message itself is showing and fading just as planned, but the box style is not displaying

![alert_msg](media/alertmsg.png)

### Technologies

#### Languages used:

- HTML

- CSS

- JavaScript

- Python

#### Frameworks and libraries

- Django framework 

- Bootstrap 4

- Font Awesome:

Icons from each page were taken from font awesome

- Google fonts

Google fonts were used to import Dongle font into style.css

- Multiavatar

[Multiavatar](https://multiavatar.com/)

- Git

Git was used for version control

- Github

to store the project code

- Heroku

heroku was used to deploy the website

- Wireframe

Balsamiq wireframe to create the wireframe

- Coolors

Find colors from a wide selection

[Coolors](https://coolors.co/9f9aa4-e7cfcd-536565-b5c9c3-cab1bd)

- DBD diagram

dbd diagram was used to create the diagram

### 6. Testing

- HTML testing

[html_validator](https://validator.w3.org/#validate_by_input)

- CSS validator

[css_validator](https://jigsaw.w3.org/css-validator/)

- PEP8 

[pep8](http://pep8online.com/)

#### Manual testing:



