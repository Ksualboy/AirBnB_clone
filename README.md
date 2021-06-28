<image src="imgs/Holberton_AirBnB_Logo.png">

# AirBnB Clone - The Console

[Description]

# The Command interpreter

[Description]

## <b> How to bring life to our interpreter </b>

Just clone this repository using the classical git command:
``````
git clone <Repository_URL>
```````
now you are able to execute
<i>console.py</i>
to appreciate the birth of the interpreter

<image src="imgs/starting console.png">


## <b> How to use it? </b>

Now inside the console you are able to do those operations:
    
- ## create new instances
    
    using <i>create</i> command you can create an instance of every class and save it into a Json file
    ``````
    (hbnb) create <class_name>
    ``````

- ## show a specific instance

    using <i>show</i> command prints the string representation of a specified instance by class name and id
    ``````
    (hbnb) show <class_name> <object_id>
    ``````

- ## delete an instance

    using <i>destroy</i> command the user is able to remove an instance, specifing it's class name and id
    ``````
    (hbnb) destroy <class_name> <object_id>
    ``````

- ## show EVERYTHING!

    using <i>all</i> command prints the string representation of every instance saved, allows to specify a class to not show the other classess instances
    ``````
    (hbnb) all
    ``````
    or
    ``````
    (hbnb) all <class_name>
    ``````

- ## update an instance attributes

    using <i>update</i> command allows the user to select an instance to modify by specify it's class name and id, followed by the attribute name and value
    ``````
    (hbnb) update <class_name> <object_id> <attribute_name> <attribute_value>
    ``````


# Examples

Here we will show you how to do some simple things with this console software in practice:

<image src="imgs/example_1.png">

Here we created a new user with the <i>create</i> command, then we displayed it content with the <i>show</i> command using it's class (User) and it's id generated randomly by the previous command.

User <i>b8170d94-cc87-4261-9a84-8ded2d47b2e6</i> is a little bit shy, he don't like to speak that much, do you?

User <i>b8170d94-cc87-4261-9a84-8ded2d47b2e6</i>: ...

Ok, so let's mark him with that trait using the <i>update</i> command:

<image src="imgs/example_2.png">

As we see we correctly setted a new attribute for our dear User <i>b8170d94-cc87-4261-9a84-8ded2d47b2e6</i> 

# That's everything for now!

Atte:

- [Hernan Montenegro](https://github.com/HernanMontenegro)

- [Daniel Millan](https://github.com/Ksualboy)
