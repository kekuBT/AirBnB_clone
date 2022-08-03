![logo](/logo.png)

# AirBnB clone - The console
Is a command interpreter and the main purpose is to manage, manipulate and access the data in the backend through the console (command line tool ) very quickly and easily (like in shell project).

  - We’ll manipulate data with JSON serialization/Deserialization (First DB engine).
  - Manipulate Python packages
  - Implement cmd module
  - Implement uuid module
  - args/kwargs
  - datetime

## Install

```
git clone https://github.com/kekubt/AirBnB_clone.git

cd AirBnb_clone

```

## CMD Commands

| Command | Description | Sample Usage
| --- | --- | --- |
| Help | Show all available commands | help  |
| Quit | Exit to the prompt | quit |
| Create | Create a new object | create class |
| Show | Retrieve an object from a file | show class name id |
| All | Display all objects in class | all class |
| Update | Update objects and attributes | update class id name key |
| Destroy | Destroy specified object | destroy class |
| Count | Retrieve the number of instances of a class | class.count |


## Usage of command interpreter
Interactive Mode:
1. Run program and show prompt with help command.
```sh
PROMPT~> ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb)
(hbnb)
(hbnb) quit
PROMPT~>
```
## Usage Create:
With the create command, a new instance is created

```sh
(hbnb) create BaseModel
a45ac806-1c59-4392-99a4-b15327584938
(hbnb)
```

## Usage All:
With the all command, all instances are displayed, returning a serialized json (string).

```sh
(hbnb) all BaseModel a45ac806-1c59-4392-99a4-b15327584938
["[BaseModel] (a45ac806-1c59-4392-99a4-b15327584938) {'id': 'a45ac806-1c59-4392-99a4-b15327584938', 'created_at': datetime.datetime(2020, 2, 20, 9, 33, 40, 732983), 'updated_at': datetime.datetime(2020, 2, 20, 9, 33, 40, 733064)}"]
(hbnb)

```
 ## Usage Show:
With the show command, the instance is displayed, returning a dictionary of the id instance.

```sh
(hbnb) show BaseModel a45ac806-1c59-4392-99a4-b15327584938
[BaseModel] (a45ac806-1c59-4392-99a4-b15327584938) {'id': 'a45ac806-1c59-4392-99a4-b15327584938', 'created_at': datetime.datetime(2020, 2, 20, 9, 33, 40, 732983), 'updated_at': datetime.datetime(2020, 2, 20, 9, 33, 40, 733064)}
(hbnb)

 ```
## Usage Update:
With the update command, the attributes of the instances are updated.

```sh
(hbnb) update BaseModel a45ac806-1c59-4392-99a4-b15327584938 first_name "Keku"
(hbnb) show BaseModel a45ac806-1c59-4392-99a4-b15327584938
[BaseModel] (a45ac806-1c59-4392-99a4-b15327584938) {'id': 'a45ac806-1c59-4392-99a4-b15327584938', 'created_at': datetime.datetime(2020, 2, 20, 9, 33, 40, 732983), 'updated_at': datetime.datetime(2020, 2, 20, 9, 33, 40, 733064), 'first_name': '"Keku"'}
(hbnb)

```

## Usage Count:
With the count command, count the number of instances.

```sh
(hbnb) BaseModel.count()
2
(hbnb)
```

## Usage Destroy:
With the Destroy command, instances are destroyed.

```sh
(hbnb) destroy BaseModel 346a5b73-d419-4c81-9bb9-39a84311cdac
(hbnb) show BaseModel 346a5b73-d419-4c81-9bb9-39a84311cdac
** no instance found **
(hbnb)

```

## non-interactive mode:
Run the program passing argumments with pipes

```sh
PROMPT~> echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
PROMPT~>
PROMPT~> cat test_help
help
PROMPT~>
PROMPT~> cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
PROMPT~>
```
## Author:
[Keku Belina](https://github.com/kekubt)
