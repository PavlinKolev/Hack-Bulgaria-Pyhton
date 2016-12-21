def accepts(*args):
    types = args

    def accepter(func):
        def check_arguments_types(*args):
            if len(types) != len(args):
                raise TypeError("Not equals lengths.")
            for i in range(len(types)):
                if type(args[i]) is not types[i]:
                    output = "Argument {} of {} is not {}!".format(
                                                        i + 1,
                                                        func.__name__,
                                                        types[i].__name__)
                    raise TypeError(output)
            return func(*args)
        return check_arguments_types
    return accepter
