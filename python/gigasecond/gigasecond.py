import datetime


def add_gigasecond(t):
    """ A gigasecond is one billion (10**9) seconds. """
    u = (t - datetime.datetime(1970, 1, 1)).total_seconds()
    gigasecond = u + 10**9

    return datetime.datetime.utcfromtimestamp(gigasecond)
