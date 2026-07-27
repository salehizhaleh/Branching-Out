"""
User Filtering Application

This module provides functionality to filter users by name, age, or email.
It loads user data from a JSON file and provides various filtering options.
"""

import json


def load_users(filename="users.json"):
    """
    Load users from a JSON file.

    Args:
        filename (str): Path to the JSON file containing user data.

    Returns:
        list: A list of user dictionaries.

    Raises:
        FileNotFoundError: If the JSON file does not exist.
        json.JSONDecodeError: If the JSON file is malformed.
    """
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not valid JSON.")
        return []


def filter_by_name(users, name):
    """
    Filter users by their name (case-insensitive).

    Args:
        users (list): List of user dictionaries.
        name (str): The name to search for.

    Returns:
        list: A list of users matching the name.
    """
    return [
        user for user in users
        if user["name"].lower() == name.lower()
    ]


def filter_by_age(users, age):
    """
    Filter users by their age.

    Args:
        users (list): List of user dictionaries.
        age (int): The age to search for.

    Returns:
        list: A list of users matching the age.
    """
    return [user for user in users if user["age"] == age]


def filter_by_email(users, email):
    """
    Filter users by their email address (case-insensitive).

    Args:
        users (list): List of user dictionaries.
        email (str): The email to search for.

    Returns:
        list: A list of users matching the email.
    """
    return [
        user for user in users
        if user["email"].lower() == email.lower()
    ]


def display_users(users):
    """
    Display users in a formatted way.

    Args:
        users (list): List of user dictionaries to display.
    """
    if not users:
        print("No users found.")
        return

    for user in users:
        print(f"ID: {user['id']}, Name: {user['name']}, "
              f"Age: {user['age']}, Email: {user['email']}")


def main():
    """
    Main function to run the user filtering application.
    Handles user input and displays filtered results.
    """
    users = load_users("users.json")

    if not users:
        print("Could not load users. Exiting.")
        return

    while True:
        print("\n" + "=" * 50)
        print("User Filtering System")
        print("=" * 50)
        print("Filter options: name, age, email, exit")
        print("-" * 50)

        filter_option = (
            input("What would you like to filter by? ").strip().lower()
        )

        if filter_option == "exit":
            print("Goodbye!")
            break

        elif filter_option == "name":
            name = input("Enter a name to filter users: ").strip()
            results = filter_by_name(users, name)
            display_users(results)

        elif filter_option == "age":
            try:
                age = int(input("Enter an age to filter users: ").strip())
                results = filter_by_age(users, age)
                display_users(results)
            except ValueError:
                print("Error: Please enter a valid age (number).")

        elif filter_option == "email":
            email = input("Enter an email to filter users: ").strip()
            results = filter_by_email(users, email)
            display_users(results)

        else:
            print("Error: Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()