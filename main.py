# -*- coding: utf-8 -*-
""" exercise main """


class Supervisor:
    """ Holds PhD student instances """

    def __init__(self, forename, surname, *args, **kwargs):
        """Initialises the object"""
        self.forename = forename
        self.surname = surname

    def __str__(self):
        """ Object string representation """
        return str('{} {}'.format(self.forename, self.surname))

    def print_forename(self):
        """ Prints forname """
        raise NotImplementedError()

    def print_surname(self):
        """ Prints surname """
        raise NotImplementedError()

    def print_fullname(self):
        """ Prints fullname """
        raise NotImplementedError()


def main():
    phd_supervisor = Supervisor("Qianni", "Zhang")
    print(phd_supervisor)


if __name__ == '__main__':
    main()
