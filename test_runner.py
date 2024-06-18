"""
Test Runner script for the Django REST application.

The script and the test cases are custom coded with inspiration from
sources listed in the README chapter Credits, Content].

This module sets up & runs tests for the Django application. The script
ensures that Django is properly initialized & configured before
executing the test cases.
"""

if __name__ == '__main__':
    import os
    import sys
    from django.conf import settings
    from django.test.utils import get_runner
    import django
    # Set the environment variable for Django settings module
    os.environ['DJANGO_SETTINGS_MODULE'] = 'drf_api.settings' 

    # Initialize Django
    django.setup()

    # Get the test runner class from settings
    TestRunner = get_runner(settings)

    # Create an instance of the test runner
    test_runner = TestRunner()

     # Run the tests in the specified modules
    failures = test_runner.run_tests(
        ['comments.tests', 'hashtags.tests', 'posts.tests']
    )

    # Exit the script with a status code based on the test results
    sys.exit(bool(failures))
