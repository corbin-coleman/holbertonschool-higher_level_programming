#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as e:
        error = "Exception: " + str(e) + "\n"
        sys.stderr.write(error)
        return None
