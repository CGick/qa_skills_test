from unittest import TestCase, main
import requests


def get_usernames(file_name):
    """
    Reads a list of usernames from a file.

    :param file_name: String of path and file name to be opened
    :return: List of usernames
    """
    with open(file_name, 'r') as infile:
        users = [user.rstrip('\n') for user in infile.readlines()]
    return users


def login(username):
    """
    Makes an HTTP request to website with username inserted into the url.

    :param username: String username to login into site with
    :return: HTTP Response object
    """
    url = 'http://www.example.com/login/{}/'.format(username)
    response = requests.request('GET', url)
    return response


def run_login():
    """
    Collects a list of users from a file and attempts to log into website with each user.

    :return: List of Tuples containing username and HTTP status codes for each login attempt
    """
    users = get_usernames('roles.txt')
    results = [(user, login(user).status_code) for user in users]
    return results


class LoginTests(TestCase):
    def test_login(self):
        self.assertItemsEqual(run_login(), [('user1', 200), ('admin1', 200), ('partern1', 200)])

    def test_login_fail(self):
        self.assertItemsEqual(run_login(), [('user1', 404), ('admin1', 404), ('partern1', 404)])


if __name__ == "__main__":
    main()
