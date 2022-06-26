
# Metacoin

In this assignment we were given a smart contract called MetaCoin,
 which implements 
a basic token which the accounts can give to each other 
with the sendCoin function, and see their balance with 
the getBalance function. We had to extend the functionality of 
this smart contract so that it could deposit loans and settle them.

The following functions were implemented:
1. getCompoundInterest(): This function can be used to calculate the
amount of interest for the given principle, rate and time. It is a public
function as it should be usable by anyone. It is also a pure function 
as it does not modify the state variables.
Another function div() was created before getCompoundInterest() to help 
calculate the value to be incremented each time. This was done as 
solidity does not offer proper support for fixed point numbers so rate 
had to be input as uint. The resources provided in the template were
used to write the formula for the div() function. This is also a public 
function and is pure as it does not modify any state variables.

2. reqLoan(): This is a public function as it can be used by any
creditor
to request to settle the loan. 

3. getOwnerBalance(): This is also a public function as it is accesible 
to anyone who wishes to get to know the balance of the owner's account.

4. viewDues(): This function has a modifier onlyOwner to make sure
that only the owner can access it. It is used to view the amount 
of loan owed to a certain creditor address.

5. settleDues(): This function also uses the modifier onlyOwner so
that only the owner can call it. This function is used to settle the 
loans taken.

How to use the smart contract using remix:
1. Compile metacoin.sol from the compilation tab.
2. Select Javascript VM as the envirionment.
3. Select account from the dropdown.
4. Select Loan-metacoin.sol from the contract dropdown.
5. Deploy the contract.
6. The various functions implemented will be visible in
the deployed contract and can be used, as long as the modifier
conditions are satisfied.

Sample input:

Owner address = 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4 

reqLoan: principle = 1000; rate = 2; time = 1

sendCoin: 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4

amount: 200

receiver address: 0x617F2E2fD72FD9D5503197092aC168c91465E7f2

getbalance: for sender: 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4

expected output for Owner = 99800

for receiver: 0x617F2E2fD72FD9D5503197092aC168c91465E7f2

expected output for creditor = 200

settleDues: creditor address: 0x617F2E2fD72FD9D5503197092aC168c91465E7f2


