# Finance Calculator

## Table of Contents

1. [Project Description](#project_description)
2. [Installation](#installation) 
3. [Usage](#usage)
4. [Credit and Contribution](#credit_and_contribution)
5. [License](#license)

## Project Description <a name="project_description"><a>

This program enables users to use two calculators: an investment calculator and a home loan or bond repayment calculator.
  
For the investment calculator, users are able to calculate the future value of their investment for both simple and compound interest
scenarios.
  
For the home loan repayment calculator, users are able to calculate the amount they will repay each month on the loan amount they receive to finance their home.
  
## Installation <a name="installation"><a> 
  
1. Download the file in the repository named the following: finance_calculator.py
2. Create a project folder named finance_calculator.
3. Move and save the downloaded files in the finance_calculator folder created.
4. Open your local Integrated Development Environment (IDE) such as VSCode.
5. Add the finance_calculator folder to your IDE.
6. Open the file named finance_calculator.py from the finance_calculator folder and run.
7. Use the program in the IDE terminal (i.e. this is where you can input the data for the task manager and view output).
  
## Usage <a name="usage"><a>
  
When you run your IDE, ensure that you are in the correct project directory.

Check your location by typing:

```
 pwd
```
If you are not in the appropriate directory, enter:

```
cd finance_calculator
```
  
### Investment calculator
  
  1. From the menu provided, select "investment".
  
<img width="776" alt="Screenshot 2023-04-20 at 16 41 43" src="https://user-images.githubusercontent.com/127111801/233401621-d034f69a-db04-4eaa-b6e1-90553b405b36.png">

2. Simple interest: Follow the prompts and input the values you would like to include in the calculation.
  
These include (in order of how they will appear):
  - Investment amount deposited
  - Interest rate
  - Number of years you plan to invest
  - Enter "**simple**" to select simple interest

<img width="776" alt="Screenshot 2023-04-20 at 16 48 21" src="https://user-images.githubusercontent.com/127111801/233411277-a2a636d1-1f03-49b5-b24a-a85198696224.png">

Based on the input numbers above, the output result of the future value of the investment will print as follows (where the amount will differ based on the input values entered):
  
<img width="776" alt="Screenshot 2023-04-20 at 17 14 52" src="https://user-images.githubusercontent.com/127111801/233410673-c97dd3df-800c-4f0d-b70b-46ade0dde057.png">

3. Compound interest: Follow the prompts and input the values you would like to include in the calculation.
  
These include (in order of how they will appear):
  - Investment amount deposited
  - Interest rate
  - Number of years you plan to invest
  - Enter "**compound**" to select compound interest
  
  <img width="776" alt="Screenshot 2023-04-20 at 17 19 57" src="https://user-images.githubusercontent.com/127111801/233412035-ca71c0aa-04a7-432c-83ee-953cd77b8fcc.png">
  
Based on the input numbers above, the output result based on compound interest will print as follows (where the amount will differ based on the input values entered):
  
  <img width="776" alt="Screenshot 2023-04-20 at 17 20 09" src="https://user-images.githubusercontent.com/127111801/233412084-37807748-0f41-4b7d-b544-593d50e0d7c5.png">
  
### Home loan repayment calculator

  1. From the menu provided, select "bond".
  
  <img width="776" alt="Screenshot 2023-04-20 at 17 23 35" src="https://user-images.githubusercontent.com/127111801/233412952-a5421671-abc0-4c00-91af-affb3baabf85.png">

 2. Follow the prompts and input the values you would like to include in the calculation.
  
These include (in order of how they will appear):
  - Present value of the house (i.e. the home loan/bond value)
  - Interest rate
  - Number of years you plan to repay the bond/loan

  <img width="776" alt="Screenshot 2023-04-20 at 17 24 45" src="https://user-images.githubusercontent.com/127111801/233413406-66deb316-7ced-40d6-90de-a39589b24bb4.png">

Based on the input numbers above, the the monthly repayment amount for the loan will print as follows (where the amount will differ based on the input values entered):
  
  <img width="776" alt="Screenshot 2023-04-20 at 17 26 27" src="https://user-images.githubusercontent.com/127111801/233413860-86b9f3f1-9fe4-4ce9-a6b7-407c2b6ca6a6.png">

### Error Handling for Calculator
  
The program will notify if there are errors with the inputs provided that make the inputs invalid. In these instances, follow the prompts provided and try again to re-enter valid inputs.
  
The following is the list of invalid input situations with the associated screenshots of the prompts that you will see:
  
1. If you enter an option other than "investment" or "bond" in the main menu.
  
  <img width="776" alt="Screenshot 2023-04-20 at 17 48 11" src="https://user-images.githubusercontent.com/127111801/233419438-5584e17e-07fe-4d0f-bd03-270a8ef97e47.png">

#### Investment Calculator
  
  2. Investment amount deposited: If you enter a value that is not a number and if you enter a negative number.
  
  <img width="776" alt="Screenshot 2023-04-20 at 17 49 10" src="https://user-images.githubusercontent.com/127111801/233419826-43e6d1b9-dd0b-4f86-bca9-587b5211c3d9.png">

  3. Interest rate: If you enter a value that is not a number.
  
  <img width="776" alt="Screenshot 2023-04-20 at 17 51 24" src="https://user-images.githubusercontent.com/127111801/233420241-b7080464-2ba4-4f5e-b7c1-33acad08896c.png">

  4. Number of years you plan to invest: If you enter a value that is not a number and if you enter a negative number.
  
  <img width="776" alt="Screenshot 2023-04-20 at 17 52 56" src="https://user-images.githubusercontent.com/127111801/233420689-97714387-5c06-40ff-a301-0c9c6d4878a6.png">

  5. Simple or compound interest: If you enter an item that is not from the menu options of "simple" or "compound" interest.
  
  <img width="777" alt="Screenshot 2023-04-20 at 17 54 34" src="https://user-images.githubusercontent.com/127111801/233421013-a338f151-fe52-44ee-a6f8-2a2be4c9cbf5.png">

#### Home loan repayment calculator
  
  6. Present value of the house (i.e. the home loan/bond value): If you enter a value that is not a number and if you enter a negative number.
  
  <img width="777" alt="Screenshot 2023-04-20 at 17 59 58" src="https://user-images.githubusercontent.com/127111801/233422390-062f409e-6228-4c85-86aa-ea81e7c9f54a.png">
  
  7. Interest rate: If you enter a value that is not an integer.

  <img width="777" alt="Screenshot 2023-04-20 at 18 01 59" src="https://user-images.githubusercontent.com/127111801/233422906-d48b5779-04e5-4674-8927-7f20a318f75c.png">

  8. Number of years you plan to repay the bond/loan: If you enter a value that is not a number and if you enter a negative number.
  
  <img width="777" alt="Screenshot 2023-04-20 at 18 02 44" src="https://user-images.githubusercontent.com/127111801/233423091-c5320427-419b-4175-b179-be66225c1ac0.png">
  
## Credit and Contribution <a name="credit_and_contribution"><a> 

This project has been developed by Bonolo Ramasedi.

## License <a name="license"><a> 
  
This project is not licensed and is intended for display purposes only. All rights reserved. No usage, distribution, or modification rights are granted.
