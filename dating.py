#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Dec 2021
# This program uses a compound boolean statement to check if the user
# can date the grandchild

def main():

    # Get user input
    user_wealth_input = input("Are you rich? enter(y/n): ")
    user_looks_input = input("Are you handsome? enter(y/n): ")
    print("")

    # Check if the user is rich and handsome to date the grandchild
    if user_wealth_input == "Y" or user_wealth_input == "y"\
       or user_looks_input == "Y" or user_looks_input == "y":
        print("Approved! You can date our grandchild")
        print("")
        print("Thanks for participating")
    elif user_wealth_input == "N" or user_wealth_input == "n"\
            and user_looks_input == "N" or user_looks_input == "n":
        print("We appreciate the effort but you cannot date our grandchild")
        print("")
        print("Thanks for participating ")
    else:
        print("Please enter either y/n.")
        print("")
        print("Thanks for participating")


if __name__ == "__main__":
    main()
