# . Arbitrary Keyword Arguments (**kwargs)
# Use **kwargs to pass any number of keyword arguments.
def profile(**info):
    for key in info.items():
        print(key)

profile(a = 12,v = 12)