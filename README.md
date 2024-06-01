![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
  * [Overview](#overview)
  * [Features](#features)
  * [Prerequisites](#prerequisites)
- [How it was done](#how-it-was-done)
  * [The Set Up](#the-set-up)
  * [Usage of the Expenses Tracker App](#usage-of-the-expenses-tracker-app)
  * [Creating the Heroku app](#creating-the-heroku-app)
  * [Future Features](#future-features)
  * [Encountered Issues](#encountered-issues)
- [Tutorials and Guides used](#tutorials-and-guides-used)
  * [Real Python](#real-python)
  * [W3Schools Python Tutorial](#w3schools-python-tutorial)
  * [Stack Overflow](#stack-overflow)
  * [Code Institute Python module materials](#code-institute-python-module-materials)
  * [Python.org Community](#pythonorg-community)
  * [Youtube videos](#youtube-videos)
- [Demo](#demo)

## Overview

The Expense Tracker App is a command-line application written in Python that allows users to track their expenses. It uses the Google Sheets API to store and retrieve expense data. Users can add new expenses, view a summary of their expenses, and ensure they do not exceed a set monthly spending limit.

## Features

- Add Expense: Users can add a new expense with a description, category, amount, and date.
- View Summary: Users can view all their recorded expenses.
- Monthly Spending Limit: The app checks if the new expense will exceed the predefined monthly limit and notifies the user.

## Prerequisites
- Python 3
- Google account with access to Google Sheets
- Google Sheets API enabled
- Service account credentials JSON file (creds.json)

# How it was done
## The Set Up
1. Used the Code Institute Template (https://github.com/Code-Institute-Org/p3-template) when creating the repository.
   ![image](https://github.com/lavenderweche/expenses-tracker-project/assets/30617453/64778c0f-1ba4-4c56-ba93-6bfc92259fb4)
   
2. Set up the Google Sheets and Google Drive API through the Google cloud platform as shown in the Love Sandwiches module which included:
   
   Creating a project in the Google Developers Console and enable the Google Drive and Google Sheets API.
   
   Create a service account and download the JSON credentials file.
   
   Share your Google Sheet with the service account email.
   
3. Set up Google Sheets document

   Create a new Google Sheet named expense_tracker.

   Set up the first worksheet with the following headers in the first row: **Date, Description, Category, Amount.**

## Usage of the Expenses Tracker App

- The code is added in the *run.py* file.
- The dependencies must be placed in the `requirements.txt` file

On run of the app, there is an Expense Tracker menu:

- Add an expense: Enter the details of your expense (description, category, amount, and date).

Enter the description, category, amount, and date (in DD-MM-YYYY format) of the expense.

If the date is left blank, it defaults to today's date.

The app validates the inputs and checks if the expense will exceed the monthly limit.

  <img width="1440" alt="image" src="https://github.com/lavenderweche/expenses-tracker-project/assets/30617453/d50a19de-a293-4e15-b08b-99e68b29e22e">
  
- View expenses summary: Display all recorded expenses.

Displays all recorded expenses in the console.

  <img width="1440" alt="image" src="https://github.com/lavenderweche/expenses-tracker-project/assets/30617453/3f8918d7-00bd-4743-a5d9-ac291b7b45e2">
  
- Exit: Exit the application.
  <img width="1440" alt="image" src="https://github.com/lavenderweche/expenses-tracker-project/assets/30617453/e35fbf9e-ca4d-42d0-8e23-8984616abc14">


## Creating the Heroku app

When creating the app, as shown in the course deployment module video, I added two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`
   ![image](https://github.com/lavenderweche/expenses-tracker-project/assets/30617453/92d52648-7dc1-4e71-bf84-151fd8876346)


Afterwards, created a _Config Var_ called `PORT`. Set this to `8000`

Another _Config Var_ called `CREDS` was added and pasted the JSON into the value field.

![image](https://github.com/lavenderweche/expenses-tracker-project/assets/30617453/011fcdbe-221d-4859-94c6-6e08fc0ffe8e)

Connect your GitHub repository and deploy as normal. In this project, I used the manual deployment option but would look into using the automated featur4e for future projects.
![image](https://github.com/lavenderweche/expenses-tracker-project/assets/30617453/90e15f49-fa0e-4aca-9672-858564c6e7c9)



## Future Features
- To make the app more interactive, for now the app is very simple and only does entry and viewing of the details. However, in future, I would like to include more features like having the user define their monthly expenses and if the user enters something that is not in the list, they are notified.
- Check for duplicates
- Add the currency for the money used


## Encountered Issues
- I initially had done the same project in a different repository but during deployment, an error that there were missing modules kept appearing even after installing the app. Therefore, I decided to start overe with a new repository, I did things the same way and the second time, the deployment was successful.
- I forgot to add the gspread and datetime packages in the requirements document and was therefore getting an error. This was fixed by including them in the *requirements.txt* file.
- Some of the validations were not workig as expected, this required troubleshpoting and also looking up solutions on Google. 

# Tutorials and Guides used
## Real Python

Offers a wide range of Python tutorials, including guides on working with APIs, data handling, and various Python libraries.
## W3Schools Python Tutorial

A beginner-friendly resource for learning Python programming concepts and syntax.
## Stack Overflow

A valuable community-driven Q&A site where developers can find solutions to a wide variety of programming challenges and issues.
## Code Institute Python module materials
The content provided by code institute during the course has been really helpful and I used most of it for the development of this project. 

## Reddit

A helpful community where Python learners and developers share tips, ask questions, and discuss best practices.
## Python.org Community

Provides access to Python-related mailing lists, forums, and special interest groups for connecting with other Python developers.
## Youtube videos

There were very many youtube videos that helped in troubleshooting problems and in also understanding some concepts which in turn maded it possible for me to build the app. 

https://www.youtube.com/watch?v=HTD86h69PtE


https://www.youtube.com/watch?v=xV0B1Y0tem0


# Demo


https://github.com/lavenderweche/expenses-tracker-project/assets/30617453/aa8d1d7b-76eb-48af-9807-b20e2c007810


