#
# jorts.py
#
# Left Wing Office Cat
# Original game concept and rules by Oliver Darkshire: Henry Sotherans, LTD.
# https://twitter.com/deathbybadger/status/1572558910564995073
#
# Coded by Imaginos the Quantum Magician 20220921
#

import sys

from random import randint

# Declare variable offsets
TRASHCAN = 0
BUTTERED = 1
UNION = 2
TABLE = 3
TEXT = 4

# Initialize the variables.
vars = [0, 0, 0, 0]

#
# Now, define the methods
#

# The Introduction.
def Introduction():
    print("\nLeft Wing Office Cat\n\tA digital implementation of an Oliver Darkshire game.")
    print("\t(You can support him at the link below:)")
    print("\thttps://www.patreon.com/deathbybadger\n")
    print("You are the office cat and you enjoy trash cans.\n")
    print("Alas, your colleagues are determined to butter you.\n")
    print("The good news is, if the cats can unionize,")
    print("you can put an end to this unprofessional behavior.\n")

def PickATable():
    """Give the user the information on what tables are choosable."""

    # The user is picking a table:
    print("\nWhat table would you like to roll on?")
    print("\tFeline Frolics? (Enter a 1)")
    print("\tA Cat Nap? (Enter a 2)")
    print("\tOr Provide Labour? (Enter a 3)\n")

def ItsADisaster(offset, vars):
    """Stuck in a trash can, or buttered, but help might be available."""
    saved_message = [
        "They manage to bump the trash can off your head.",
        "They lick some of the butter from your fur.",
    ]
    dire_message = [
"""
You're stuck in a trash can real bad.
You bang into a few doors, then decide to wait for rescue.
""",
"""
You're captured by a well meaning miscreant,
who slathers you in butter, to try to teach you hygiene.

You do not understand.
""",
    ]

    # Can we be saved from our dire fate? Lets roll the dice.
    saved = randint(1, 6)
    # 2, 3, 4, 5 says yes!
    if saved > 1 and saved < 6:
        # Saved by a comrade!
        vars[offset] = 9
        print("Solidarity, comrade! You've been saved by a smarter office cat.")
        print(saved_message[offset])
        # Let the user pick the table again.
        vars[TABLE] = 0
    else:
        # You must suffer your fate, and try again in another session.
        print("\nOh, dear. You're about to be Twitter famous.")
        print(dire_message[offset])
        sys.exit(0)

def basicResponse(happenstance, roll, events, vars):
    """
    The basic response to a new happenstance.
    Whatever the happenstance, the basic response is the same.
    Print out the happenstance category, the event, and then
    adjust running totals as needed.
    """

    # Typical programming adjustment from count to zero-based indexing.
    eventsIndex = event - 1
    # Let the user know what's happening.
    print(happenstance, end = "\t")
    print(events[eventsIndex][TEXT])
    # Update all the running totals of trashcan, buttered, and union as appropriate.
    for offset in range(0, TABLE):
        # NOTE: events array uses same indices as vars array. 
        vars[offset] += events[eventsIndex][offset]
    # Table is a choice, not a running total, handle differently.
    vars[TABLE] = events[eventsIndex][TABLE]

# FELINE FROLICS: Let's find out which one.
def FelineFrolics(event, vars):
    # Array layout is trashcan, buttered, union, table, text.
    events = [
        [1, 0, 0, 0, "You smell food. It's nearby in the delicious trash cans."],
        [0, 1, 0, 0, "You stroll by human resources. This is a mistake."],
        [0, 2, 0, 0, "You go outside, and have to be let back in again."],
        [0, 1, 0, 0, "You get stuck in a toilet stall."],
        [0, 0, 1, 0, "You stumble into a friendly cat. They must be brought on board."],
        [0, 0, 0, 2, "You changed your mind. You want a CAT NAP instead."],
    ]

    basicResponse("FELINE FROLICS:", event, events, vars)

# A CAT NAP: What could go wrong?
def ACatNap(event, vars):
    # Array layout is trashcan, buttered, union, table, text.
    events = [
        [0, 0, 1, 0, "You dream of Marx, and you plot the revolution."],
        [0, 1, 0, 0, "You awaken one inch from a butter knife."],
        [1, 0, 0, 0, "You take a nap inside your favourite garbage can."],
        [1, 0, 0, 0, "You roll into a bin."],
        [1, 0, 0, 0, "You sleepwalk into peril."],
        [0, 0, 0, 1, "Nah. You're not tired. You want some FELINE FROLICS."],
    ]

    basicResponse("A CAT NAP:", event, events, vars)

# PROVIDE LABOUR: Yes, Oliver speaks the King's English.
def ProvideLabour(event, vars):
    # Array layout is trashcan, buttered, union, table, text.
    events = [
        [0, 0, 1, 0, "You knock over a stack of papers in revolt."],
        [0, 1, 0, 0, "You attend your annual performance review."],
        [1, 0, 0, 0, "You give a seminar on the delights of garbage hunting."],
        [0, 0, 0, 2, "This is awful. You want a CAT NAP instead."],
        [0, 0, 0, 1, "BORED NOW. You want some FELINE FROLICS."],
        [0, 1, 0, 0, "You get stuck in a photocopier."],
    ]

    basicResponse("PROVIDE LABOUR:", event, events, vars)

def WhatHappened(table, vars):
    if table == 1:
        FelineFrolics(event, vars)
    elif table == 2:
        ACatNap(event, vars)
    elif table == 3:
        ProvideLabour(event, vars)


def show_status(vars):
    """Status display: X for a filled slot, . for an currently empty one."""
    message = 'Trashcan: ' + (vars[TRASHCAN]*'X') + ((10 - vars[TRASHCAN])*'.') + "\n"
    message += 'Buttered: ' + (vars[BUTTERED]*'X') + ((10 - vars[BUTTERED])*'.') + "\n"
    message += 'Union:    ' + (vars[UNION]*'X') + ((10 - vars[UNION])*'.')
    print(message)

if __name__ == "__main__":
    # Let the user know what they're in for.
    Introduction()

    # Give them the run down on what their choices are.
    PickATable()
    
    # Play until you've created a union, or disaster strikes.
    while vars[UNION] < 10:
        print("")
        
        # Do the dice roll right now.
        event = randint(1, 6)
    
        # Is the user picking a table, or has their choice been forced?
        if vars[TABLE] == 0:
            # User gets to pick the table.
            try:
                choice = int(input("Your table choice: "))
            except:
                print("Please enter only a 1, or 2, or 3.")
                continue
            if (choice < 1 or choice > 3):
                print("Please enter only a 1, or 2, or 3.")
                continue
            else:
                # Set the table to the user's choice.
                vars[TABLE] = choice

        print('You rolled a ' + str(event) + '.')
        # Let the user know what happened.
        WhatHappened(vars[TABLE], vars)

        # If we've hit 10 on either trashcan or buttered, it could be a disaster.
        if (vars[TRASHCAN] >= 10):
            ItsADisaster(TRASHCAN, vars)
        elif (vars[BUTTERED] >= 10):
            ItsADisaster(BUTTERED, vars)

        # Show the current state of things.
        show_status(vars)

    # It's a union!
    print(
"""

You have successfully convinced your fellow felines
to band together in common purpose against
the predations of the ruling class.

You will never be buttered again.

"""
        )
