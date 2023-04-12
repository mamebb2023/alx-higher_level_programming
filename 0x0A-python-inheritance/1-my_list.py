#!/usr/bin/python3
""" Creating a class that inherits from list """


class MyList(list):
    """ A class that inherites form list """

    def print_sorted(self):
        """ Prints the list of ints in asending sort """
        print(sorted(self))
