# Welcome to Guess The Number

You can play as much as you like and see how quickly you can guess the correct number. Hints if you are too high or too low are given to help you along.

My live site can be [Viewed Here](https://project-3-number-guess.herokuapp.com)

![python-responsive-project-3](https://user-images.githubusercontent.com/100090476/179019168-fccf0d92-408b-4504-982e-23d3fd089b94.png)

## About The Game and How To Play

Guess The Number is a fun and engaging game. To start off you must pick a number, the higher the number you choose, the harder you will make the game for yourself. As remember, you must guess one correct number chosen my the computer between 0 and whatever number you fist choose. When you guess the number, the game will tell you if you have guessed to high or too low. Finally, once you have guessed correctly the game will tell you!

## Features

![screen-shot-1-python](https://user-images.githubusercontent.com/100090476/179019995-7a3952a0-3bc9-4587-a7e4-7c6e0fae144a.png)

```
Computer asks for a number to use as the range
Player guesses what the number is
```
![screen-shot-2-python](https://user-images.githubusercontent.com/100090476/179021629-0976017b-752f-4bd9-96f4-e181745b7cb1.png)

```
Computer tells player if their guess was too high or low
```

![screen-3-python](https://user-images.githubusercontent.com/100090476/179022250-8d9eea09-c66a-4540-ae6b-dfaa74b3f6ac.png)

```
Input validation and testing stop the player entering anything except numbers
```

## Testing

I have manually tested this project by doing the following:

* Passed the code through PEP8 linter and confirmed there are no problems
* Given invalid inputs: strings when numbers are expected
* Tested in my local terminal and the Code Institute Heroku terminal

### Bugs

* When i ran the code through the PEP8 I discovered there was `white space within my code`
  * Solution was to add /n at the end of some print statemnts and to backspace on other lines of code

### Remaining Bugs

* No bugs remaining

### Validator Testing

* Passed PEP8 validator with no errors on final test

![python-validator-pass-project-3](https://user-images.githubusercontent.com/100090476/179025386-71f2123b-fe04-405d-8358-220b776535ea.png)

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

* Steps for deployment:
  * Fork or clone this repository
  * Create a new Heroku app
  * Set the buildbacks to `Python` and `NodeJS` in that exact order
  * Link the Heroku app to the repository
  * Click on _Deploy_

## Credits

* Code Institute for the deployment terminal
* Youtube for game idea 








