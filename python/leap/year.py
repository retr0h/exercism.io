def is_leap_year(year):
    """ In the Gregorian Calendar, leap years are evenly divisible
    by 4, with the exception of centurial years that are not evenly
    divisible by 400.
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
