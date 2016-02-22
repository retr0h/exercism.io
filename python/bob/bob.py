import re
def hey(what):
    what = what.strip()
    if what.isupper():
        return 'Whoa, chill out!'
    elif not what:
        return 'Fine. Be that way!'
    elif re.search(r'\?$', what):
        return 'Sure.'
    else:
        return 'Whatever.'
