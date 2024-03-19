# AirBnB Clone Project

Welcome to the AirBnB clone project! This project aims to create an AirBnB clone web application using Python. Before getting started, please read the AirBnB concept page for a better understanding of the project goals and objectives.

## Command Interpreter

The first step of the project involves writing a command interpreter to manage AirBnB objects. This command interpreter is crucial as it will be used throughout the project to interact with various objects such as users, states, cities, places, etc. The tasks involved in this step include:

- Implementing a parent class (`BaseModel`) to handle the initialization, serialization, and deserialization of future instances.
- Creating a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Creating classes for AirBnB objects (e.g., `User`, `State`, `City`, `Place`, etc.) that inherit from `BaseModel`.
- Developing the first abstracted storage engine of the project: File storage.
- Writing unit tests to validate all classes and storage engine.

## What's a Command Interpreter?

The command interpreter, similar to a shell, is a tool used to manage objects within the AirBnB project. It allows users to perform various operations such as creating new objects, retrieving objects from files or databases, performing operations on objects, updating attributes, and destroying objects.

## Learning Objectives

By the end of this project, you are expected to:

- Understand how to create a Python package.
- Develop a command interpreter in Python using the `cmd` module.
- Implement unit testing in a large project.
- Serialize and deserialize a Class.
- Read and write JSON files.
- Handle datetime operations.
- Understand the concept of UUID.
- Utilize `*args` and `**kwargs` in function arguments.
- Manage named arguments in functions.

## Requirements

### Python Scripts

- **Allowed Editors:** vi, vim, emacs
- **Operating System:** Ubuntu 20.04 LTS
- **Python Version:** 3.8.5
- **Line Endings:** All files should end with a new line
- **Shebang Line:** The first line of all files should be exactly `#!/usr/bin/python3`
- **README.md:** A README.md file, at the root of the folder of the project, is mandatory
- **Code Formatting:** Your code should use the pycodestyle (version 2.8.*)
- **Executable Files:** All your files must be executable
- **Module Documentation:** All your modules should have documentation
- **Class Documentation:** All your classes should have documentation
- **Function Documentation:** All your functions (inside and outside a class) should have documentation

### Python Unit Tests

- **Allowed Editors:** vi, vim, emacs
- **Line Endings:** All files should end with a new line
- **Test Files:** All your test files should be inside a folder named `tests`
- **Test Module:** You have to use the unittest module for testing
- **Test File Format:** All your test files should be Python files (extension: .py)
- **Test File Naming:** All your test files and folders should start with `test_`
- **Test Discovery:** All your tests should be executed using `python3 -m unittest discover tests`
- **Module Documentation:** All your modules should have documentation
- **Class Documentation:** All your classes should have documentation
- **Function Documentation:** All your functions (inside and outside a class) should have documentation

### GitHub

- **Repository:** There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.

## Execution

The shell should work in both interactive and non-interactive modes. In interactive mode, the shell prompt should display `(hbnb)` while in non-interactive mode, it should execute the provided command and display the output accordingly.

Interactive Mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

Non-Interactive Mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
