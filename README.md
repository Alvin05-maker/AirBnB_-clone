Console Application: AirBnB Clone
Project Description
This project involves building a command-line interpreter to manage AirBnB objects, laying the foundation for a full-scale web application: the AirBnB clone. This initial step is crucial as it forms the backbone for subsequent tasks, including HTML/CSS templating, database storage, API development, and front-end integration.

Command Interpreter Overview
The command interpreter allows users to manage AirBnB objects through a series of commands. It provides functionalities for object creation, modification, deletion, and display. The interpreter operates in both interactive and non-interactive modes, catering to different user preferences.

How to Start the Console
To start the console, run the following command:

./console.py

How to Use the Console
Once the console is running, you can enter various commands to interact with AirBnB objects. Available commands include:

create: Creates a new instance of a specified class.
Example: create BaseModel

show: Displays the string representation of an instance based on the class name and ID.
Example: show BaseModel 1234-5678

destroy: Deletes an instance based on the class name and ID.
Example: destroy BaseModel 1234-5678

all: Displays the string representation of all instances or instances of a specific class.
Example: all or all BaseModel

update: Updates an instance based on the class name and ID by adding or updating attributes.
Example: update BaseModel 1234-5678 name "New Name"

quit or EOF: Exits the console.

Examples
1. Creating a new User instance:

(hbnb) create User

2. Showing details of a specific User instance:

(hbnb) show User 1234-5678

3. Updating the name of a Place instance:

(hbnb) update Place 8765-4321 name "New Place Name"

4. Displaying all instances of BaseModel class:

(hbnb) all BaseModel

Console Construction Steps
The construction of the console involved the following key steps:

Write a Command Interpreter: Develop a user-friendly command-line interpreter to manage AirBnB objects.

Implement Serialization/Deserialization Flow: Establish a serialization/deserialization process for instances, dictionaries, JSON strings, and files.

Create BaseModel Class: Develop a parent class (BaseModel) to handle object initialization, serialization, and deserialization.

Build AirBnB Classes: Create classes (User, State, City, Place, etc.) that inherit from the BaseModel class.

Develop Storage Engine: Implement a file storage engine for managing object data persistently.

Write Unit Tests: Develop comprehensive unit tests to validate all classes and storage functionalities.
