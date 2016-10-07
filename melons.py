from random import choice
from datetime import datetime as dt


"""This file should have our order classes in it."""


class AbstractMelonOrder(object):
    """ Basic information for all melon orders. """


    def __init__(self, species, qty, order_type, tax):
        """ Initialize melon order attributes. """
        
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.base_price = None


    def get_total(self):
        """ Returns total price including tax. """

        # self.base_price = self.get_base_price()

        if self.species == "Christmas":
            self.base_price *= 1.5
        total = (1 + self.tax) * self.qty * self.base_price
        return total


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


    def get_base_price(self):
        """ Chooses a random base price between 5 and 9 (inclusive). """
        now = dt.now()
        self.base_price = choice(range(5, 10))

        if now.weekday() < 5 and now.hour in range(8,11):
            self.base_price += 4
        return self.base_price


class GovernmentMelonOrder(AbstractMelonOrder):
    """ No tax on government orders """


    def __init__(self, species, qty):
        self.passed_inspection = False
        super(GovernmentMelonOrder, self).__init__(species, qty, "government", 0)
        

    def mark_inspection(self, passed):
        """Set passed_inspection to true if passed is True."""

        if passed:
            self.passed_inspection = True
        else:
            self.passed_inspection = False


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""


    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""


    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
        self.country_code = country_code


    def get_total(self):
        """ Returns total price including tax. """

        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            return total + 3
        return total


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
