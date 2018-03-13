"""Print out all the melons in our inventory."""


from melons import melons


def print_melons(melons):
    """Print each melon followed by it's attributes

    Example:

    CANTALOUPE
      flesh_color: None
      price: 0.99
      rind_color: None
      seedless: False
      weight: None

    """

    for name, melon in sorted(melons.items()):
        print name.upper()
        for attribute, value in sorted(melon.items()):
            print "  {}: {}".format(attribute, value)
        print ""

print_melons(melons)
