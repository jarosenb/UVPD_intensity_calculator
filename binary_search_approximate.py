__author__ = 'jakerosenberg'
# search through a mass spectrum(in list form) for ions within 10ppm.


def search(givenval,tosearch,ppm,rightpointer = None,leftpointer=0):

    if not rightpointer:
        rightpointer = len(tosearch)

    midpoint = (rightpointer + leftpointer) / 2
    lowbound= tosearch[midpoint]-tosearch[midpoint] / (1000000/ppm)
    highbound= tosearch[midpoint]+tosearch[midpoint] / (1000000/ppm)

    if rightpointer-leftpointer==1 and not (lowbound< givenval <highbound):
        return -1

    elif lowbound < givenval < highbound:
        return midpoint

    elif givenval>tosearch[midpoint]:
        leftpointer=midpoint
        return search(givenval, tosearch, ppm, rightpointer, leftpointer)

    elif givenval<tosearch[midpoint]:
        rightpointer=midpoint
        return search(givenval, tosearch, ppm, rightpointer, leftpointer)