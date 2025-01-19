#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
from sys import path, argv
from pathlib import Path


path.append(str(Path(__file__).resolve().parent.parent))

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DetMals.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(argv)


if __name__ == '__main__':
    main()
