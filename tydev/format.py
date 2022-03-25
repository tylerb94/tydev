def number_add_commas(number):

    neg = number < 0.0
    finished = ""

    halfs = str(number).split(".")
    half1 = halfs[0]

    while len(half1) > 3:
        for n in range(3):
            finished += half1[-1]
            half1 = half1[:-1]
        finished = "," + finished

    finished = half1 + finished

    if len(halfs) == 2:

        dec = halfs[1]
        if len(dec) == 1:
            dec = dec + "0"
        finished += "." + dec

    if neg:
        finished = "-" + finished
    return finished