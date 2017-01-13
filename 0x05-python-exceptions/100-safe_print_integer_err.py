#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        error = "Error: " + str(e) + "\n"
        sys.stderr.write(error)
        return False
