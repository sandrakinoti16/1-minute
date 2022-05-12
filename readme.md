# 1-minute
# Description
This is a flask application that allows people to pitch their ideas in one minutes as well as interact and make their pitches lively by adding in between jokes or comments which other people can upvote or downvote if they find the pitch ideas interesting. lastly users are also able to create their own pitches.

## Author
Sandra Kinoti

## User Story

* Comment on the different pitches posted py other uses.
* See the pitches posted by other uses.
* Vote on s pitch they have viwed by giving it a upvote or a downvote.
* Register to be allowed to log in to the application
* View pitches from the different categories.
* Submit a pitch to a specific category of their choice.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all posts, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with app pitches based on categories and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|

## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)
## Known Bugs
* There are no known bugs currently but contact if you spot any 😄
## Contact Information 

If you have any question or contributions, please email me 📧 at [sandrakinya6@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2022 **sandra kinoti**

