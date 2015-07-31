__author__ = 'jakerosenberg'
from modification_parser import getmass


def ion_dictionary(sequence):
    std_aa_mass = {
        'G': 57.02146,
        'A': 71.03711,
        'S': 87.03203,
        'P': 97.05276,
        'V': 99.06841,
        'T': 101.04768,
        'C': 103.00919,
        'L': 113.08406,
        'I': 113.08406,
        'N': 114.04293,
        'D': 115.02694,
        'Q': 128.05858,
        'K': 128.09496,
        'E': 129.04259,
        'M': 131.04049,
        'H': 137.05891,
        'F': 147.06841,
        'R': 156.10111,
        'Y': 163.06333,
        'W': 186.07931,
    }

    getmassresult = getmass(sequence)
    seq_nomod = getmassresult[0]
    moddict = getmassresult[1]
    seqlen = len(seq_nomod)

    def getmodmass(resn):
        return std_aa_mass[seq_nomod[resn-1]] + moddict[resn]

    iondict = {'a': [0], 'a+': [0], 'b': [0], 'y': [0], 'y-': [0], 'y--': [0], 'x': [0], 'x+': [0], 'c': [0], 'z': [0]}

    sum1 = 0
    sum2 = 0
    for i in range(1, len(seq_nomod)):

        sum1 += getmodmass(i)

        iondict['a'].append(sum1 - 27.9949)
        iondict['a+'].append(sum1 - 27.9949 + 1.007825)
        iondict['b'].append(sum1)
        iondict['c'].append(sum1 + 17.026549)

        i2 = seqlen - i +1
        sum2 += getmodmass(i2)

        iondict['x'].append(sum2 + 43.989830)
        iondict['x+'].append(sum2 + 43.989830 + 1.007825)
        iondict['y'].append(sum2 + 18.010565)
        iondict['y-'].append(sum2 + 18.010565 - 1.007825)
        iondict['y--'].append(sum2 + 18.010565 - 2 * 1.007825)
        iondict['z'].append(sum2 + + 17.002740 - 14.003074 - 1.007825)

    return iondict


