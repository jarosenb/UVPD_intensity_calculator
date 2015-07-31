__author__ = 'jakerosenberg'
# input = dumped text file(\t-delimited)
# return dict of {mass:intensity}


def peakdict(qualout):
    dtext = qualout.split("\n")
    peaksdict = {}
    for line in dtext:
        ln = line.split('\t')
        try:
            peaksdict[float(ln[0])] = float(ln[1])
        except ValueError:
            pass
        except IndexError:
            pass

    return peaksdict

