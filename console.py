#!/usr/bin/python3
"""Entry point to the console"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Representation of the console class"""
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def __init__(self):
        super().__init__()

    def handle_non_interactive_commands(self):
        """Handle commands in non-interactive mode"""
        for line in sys.stdin:
            if line.strip():
                self.onecmd(line.strip())
    def do_EOF(self, line):
        """Exit the console"""
        return True
    def do_quit(self, line):
        """Exit the console"""
        return True
    def help_quit(self):
        """Print help message for the quit command."""
        print("Quit command to exit the program")

    def do_create(self, line):
        """Create an instance of BaseModel.Usage: create <model name>"""
        args = line.split()
        class_name = args[0]
        if len(args) == 0:
            print("** class name missing **")
        elif class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            storage.save()
            print(new_instance.id)
    def do_show(self, line):
        """Print the string representation of an instance based on the class name.
        Usage: show <class_name> <instance_id>
        """
        args = line.split()
        class_name = args[0]
        instance_id = args[1]
        objects_dict = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if len(args) == 0:
            print("** class name missing **")
        elif class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif key not in objects_dict:
            print("** no instance found **")
        else:
            print(objects_dict["{}.{}".format(args[0], args[1])])
    
    def do_destroy(self, line):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id.
        """
        args = line.split()
        objects_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objects_dict.keys():
            print("** no instance found **")
        else:
            del objects_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based on class name."""
        args = line.split()
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            instances  = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    instances.append(obj.__str__())
                elif len(args) == 0:
                    instances.append(obj.__str__())
            print(instances)
if __name__ == "__main__":
    HBNBCommand().cmdloop()
