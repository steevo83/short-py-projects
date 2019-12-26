def float_range(*args):
    # print(len(args))
    numargs = len(args)
    if numargs == 0:
        raise TypeError("At least one argument needed.")
    elif numargs > 3:
        raise TypeError(f'Expected 1-3 arguments and got {numargs}')
    else:
        if numargs == 1:
            stop = args[0]
            start = 0
            step = 1
        elif numargs == 2:
            (start, stop) = args
            step = 1
        elif numargs == 3:
            (start, stop, step) = args
        i = start
        if step > 0:
            while i < stop:
                yield float(i)
                i += step
        if step < 0:
            while i > stop:
                yield float(i)
                i += step

