#!/usr/bin/env python
import os
import sys

from logs.mylog import flogger

from zoo.zoo_func import handle_zoo


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zoowatch.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    flogger.info("before execute")

    handle_zoo()

    execute_from_command_line(sys.argv)
    flogger.info("after execute")

