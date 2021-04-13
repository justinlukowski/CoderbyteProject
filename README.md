# CoderbyteProject

## Project Description:
Requirements
At least the following flow should be implemented:

Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw

For simplification, there are only 1 dollar bills in this world, no cents. Thus account balance can be represented in integer.

Your code doesn't need to integrate with a real bank system, but keep in mind that we may want to integrate it with a real bank system in the future. It doesn't have to integrate with a real cash bin in the ATM, but keep in mind that we'd want to integrate with that in the future. And even if we integrate it with them, we'd like to test our code. Implementing bank integration and ATM hardware like cash bin and card reader is not a scope of this task, but testing the controller part (not including bank system, cash bin etc) is within the scope.

A bank API wouldn't give the ATM the PIN number, but it can tell you if the PIN number is correct or not.

Based on your work, another engineer should be able to implement the user interface. You don't need to implement any REST API, RPC, network communication etc, but just functions/classes/methods, etc.

You can simplify some complex real world problems if you think it's not worth illustrating in the project.

## Message from creator:
I was not completely sure on the directions of the project but I did my best to fulfill the requirements. 

The program first asks the user to insert their card (enter a card number). Then the user is prompted to enter a PIN. If the user gives an incorrect PIN three times in a row, then their account is locked. Upon successful entry of their PIN number, the user can select which bank account to access: checkings or savings. After selection, their current balance is shown and they can then withdraw or deposit money. The program ensures that the user cannot withdraw more money than they have in their account. At any point, the user can go back a "page" or logout. The program can run forever, but a '-1' for a card input will cause the program to stop running.

I ran the program using Pycharm, but can be ran from the command line by python program.py.

There are three users already defined in the program at the top of the main function. These are the basic test cases I used but can be altered by changing the values inside. The main values used are card number, PIN number, checkings balance, and savings balance. 
