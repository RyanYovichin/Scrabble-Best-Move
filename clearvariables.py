for var in list(globals().keys()):
    if var not in ['__builtins__', '__file__', '__name__', '__doc__']:
        del globals()[var]
