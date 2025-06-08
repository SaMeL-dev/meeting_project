<<<<<<< HEAD
#!/usr/bin/env python
=======
 #!/usr/bin/env python
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meeting_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
