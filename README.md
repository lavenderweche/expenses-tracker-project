![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

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
  <img width="1440" alt="image" src="https://github.com/lavenderweche/expenses-tracker-project/assets/30617453/d50a19de-a293-4e15-b08b-99e68b29e22e">

- View expenses summary: Display all recorded expenses.
- Exit: Exit the application.

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
