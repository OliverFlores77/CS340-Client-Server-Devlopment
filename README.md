# CS340-Client-Server-Devlopment
SNHU course

CS 340 README

About the Project/Project Title/Purpose
This project is a Python module that allows a user to perform all four CRUD (Create, Read, Update, Delete) operations on a MongoDB database. As outlined in the project scenario, this module is designed to work with animal shelter data to help an organization called Grazioso Salvare identify dogs for their search-and-rescue training program. The code is written in an object-oriented style using an AnimalShelter class to make it reusable and easy to understand.

Motivation
The main goal of this project is to complete the first phase of development for the CS 340 course project. The assignment scenario involves building a tool for Grazioso Salvare, a company that trains search-and-rescue dogs. They need a way to filter through shelter data to find dogs that fit specific profiles, such as being under a certain age or of a particular breed.

This Python module is the first step in building that tool. It serves as the bridge between the database holding the animal information and the user-facing application that will be built later. By creating methods to handle the Create, Read, Update, and Delete functions, this module provides the essential back-end functionality needed for the application to work.

Getting Started
To get a local copy of this project up and running for testing, you first need to ensure the database environment is correctly configured.

MongoDB Instance: A local MongoDB server must be running.

Database and Collection: An aac database must exist with an animals collection containing the shelter outcome data.

User Account: A user named aacuser must be created with readWrite privileges to the aac database.

Installation
This project requires Python 3 and the pymongo library.
Python Driver: The pymongo library was chosen as it is the official and recommended Python driver for working with MongoDB. It provides a straightforward, Pythonic API for executing database commands, managing connections, and handling data, making it the industry standard for connecting Python applications to MongoDB.
Installation Command: Ensure pip is installed with your Python distribution. Install the pymongo library by running the following command in your terminal: pip install pymongo


Usage
The primary use of this module is to interact with the animal shelter database. The intended usage for this assignment is to test the module's functionality from a Jupyter Notebook.

Configure Password: Open the CRUD_Python_Module.py file and replace the placeholder 'your_password_here' with the actual password for the aacuser.

Open Notebook: Launch Jupyter Lab and open the ModuleFourTestScript.ipynb file.

Execute Script: Run the code cell within the notebook. 

Verify Output: Observe the output printed below the cell. A successful execution will confirm that a record was created and then successfully read from the database. A screenshot of this output is the final deliverable.

 



Code Example
The core functionality is encapsulated in the AnimalShelter class. The key methods are:

create(self, data): Inserts a new document into the collection.
Input: A Python dictionary (data) representing the document.
Output: Returns True on successful insertion, False otherwise.

read(self, query): Queries for documents in the collection.
Input: A Python dictionary (query) specifying the search criteria.
Output: Returns a list of matching documents. Returns an empty list [] if none are found.

update(self, query, new_data): Updates one or more documents that match a query.
Input: A query dictionary to find the documents and a new_data dictionary containing the fields to be changed.
Output: Returns the number of documents that were modified.

delete(self, query): Deletes one or more documents that match a query.
Input: A query dictionary to find the documents to be deleted.
Output: Returns the number of documents that were deleted.




Tests
The testing is performed by the ModuleFourTestScript.ipynb script. It imports the AnimalShelter class, creates a new animal record, and then reads that record to verify its existence.
The following code demonstrates the test procedure:



Demonstration of Functional Operations
MongoDB import execution


User authentication execution






















CRUD Functionality test execution





Contact
Your name: Oliver Flores
