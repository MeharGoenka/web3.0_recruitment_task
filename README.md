# web3.0_recruitment_task
The code I have written for this recruitment task involving a loaning service is as follows:
The system consists of lenders and borrowers connected by a service. The service starts with an initial amount and the rest of the money is deposited by the lenders.This money is then used to give out loans to borrowers. 
In my code there is a class called Loaning_system which stores the bank balance, rates, etc (basically info common across all customers irrespective of anything). It also contains a dictionary that contains key value pairs of customer id and customer objects.
Then there is a class called account which contains all account details like account id and balance. There are two subclasses of an account i.e. lender and borrower which include functions to lend and borrow money respectively.
Then there is a class called customer which contains all the customer details like name, age and then further all the accounts that a customer has stored in a list.
This way all functions can logically be called and the loaning service can function.
Currently, it is very tedious to type out the entire command to execute or display anything but I was not able to implement a better user interface due to time constraints.
