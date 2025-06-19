### Welcome to the interactive simulation of a toy robot, the Mars Rover
### This is an exercise in Object-Oriented Programming

This repo has been updated to extend its functionality and log robot controller errors. The original repo had one `Robot class` which was handling several complex behaviours. These have now been split into new classes, more in line with the Single Responsibility Principle of classes. 

All classes and files are described below. 

The <ins>rover.py</ins> code has two parts:
- A `Robot class` that defines the attributes and behaviours of the toy robot. On initialisation, the `Robot class` relies on other classes in <ins>other_classes.py</ins> to check if initialisation values are valid and if not, raises the `InvalidRobotSpecsError`.
- A `main` function which is a recursive function enabling interactive control of the robot.

A second file <ins>other_classes.py</ins> contains classes and exceptions that <ins>rover.py</ins> rely on:
- A `Table class` defining the boundaries of the table. The original task involved a 5 x 5 table, this class expands the possibilities. The class can raise an `OutOfBounds` error for any coordinate outside the defined boundaries.
- A `Facing class` defining the direction of the robot. The original task defined 4 directions (North, East, South, West). Once again, this class expands the possibilities. The class can raise a `DirectionInvalidError` which is useful for typos. 

A third file <ins>test_rover_methods.py</ins> has a series of tests for the `Robot class` methods and the `main` function. Test data is also included there. 

### Instructions:
First, clone the repo.

To start the simulation from the command line, run `python rover.py` and follow the on-screen instructions.

Some tests are written in  <ins>test_rover_methods.py</ins>. To run the test, install the pytest module first. Then type `pytest test-rover-methods.py -v` on the command line.

Enjoy 😊

-Annette

![image](https://github.com/user-attachments/assets/6cab5626-eb6c-4627-884d-13a2ae801e07)


