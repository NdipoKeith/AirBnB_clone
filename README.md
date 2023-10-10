# AirBnB_clone - The Console
![image](https://user-images.githubusercontent.com/106776383/203980085-11fbf721-1f19-4e74-a98c-7f635313c518.png)

[AirBnB Clone - The Console](https://alx-intranet.hbtn.io/concepts/74)

For further information, click on the above link

# 0x00. AirBnB clone - The console

## Description

This is the ALX AirBnB Clone project, focusing on creating a command-line interface (CLI) or console to manage AirBnB objects. The project will gradually evolve to encompass various aspects of web development, including HTML/CSS templating, database storage, APIs, and front-end integration.

### Key Tasks:

- Implement a parent class (BaseModel) for object initialization, serialization, and deserialization.
- Establish a flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Create classes representing AirBnB objects (e.g., User, State, City, Place) that inherit from BaseModel.
- Develop the first abstracted storage engine for the project: File storage.
- Create comprehensive unit tests to validate all classes and the storage engine.

## Command Interpreter

The command interpreter is a Python-based CLI that allows you to interact with the Airbnb objects. You can create, retrieve, update, and delete objects, as well as perform various operations on them.

## How to Start

To start the command interpreter, follow these steps:

1. Clone the project repository:

   ```shell
   git clone https://github.com/NdipoKeith/AirBnB_clone.git
   ```
2. Change into the project directory:

   ```
   cd AirBnB_clone
   ```
3. Run the command interpreter:

   ```
   ./console.py
   ```

## How to Use

Once the command interpreter is running, you can use various commands to manage Airbnb objects. Here are some examples of commands you can use:

* `create <classname>`: Create a new instance of a class.
* `show <classname> <id>`: Show details of a specific instance.
* `update <classname> <id> <attribute> "<value>"`: Update an instance's attribute.
* `all <classname>`: List all instances of a class.
* `destroy <classname> <id>`: Delete a specific instance.
* `quit` or `EOF`: Exit the command interpreter.

For a full list of commands and their usage, type `help` in the command interpreter.

## Examples

Here are some usage examples:

```
(hbnb) create User
(hbnb) show User 12345
(hbnb) update User 12345 first_name "John"
(hbnb) all User
(hbnb) destroy User 12345
(hbnb) quit
```

## Helpful Links
* [Python Docs: Cmd](https://docs.python.org/3.4/library/cmd.html)
* [Python Docs: Modules / Packages](https://docs.python.org/3.4/tutorial/modules.html#packages)
* [Python Docs: UUID](https://docs.python.org/3.4/library/uuid.html)
* [Python Docs: datetime](https://docs.python.org/3.4/library/datetime.html)
* [Python Docs: Unit test](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [Python Tips: args and kwargs](https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)
* [All about cmd](https://pymotw.com/2/cmd/)
* [Give Python a shell](https://coderwall.com/p/w78iva/give-your-python-program-a-shell-with-the-cmd-module)


## Authors

The following individuals have contributed to this project:

* [NdipoKeith](https://github.com/NdipoKeith "@NdipoKeith")
* [DAVENJAGI](https://github.com/DAVENJAGI "@DAVENJAGI")

Please refer to the [AUTHORS]() file for more details about author
