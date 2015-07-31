__author__ = 'jakerosenberg'
from read_qual_output import peakdict
from IonCalculator import ion_dictionary
from binary_search_approximate import search
from modification_parser import getmass

def assign(sequence,raw_input):


    seqaa = getmass(sequence)[0]
    lenseq = len(seqaa)

    idict = ion_dictionary(sequence)
    pkd = peakdict(raw_input)

    intsbypos = {k:0 for k in range(1,lenseq+1)}

    nterm_types = [k for k in idict if k[0] in('a', 'b', 'c')]
    cterm_types = [k for k in idict if k[0] in('x', 'y', 'z')]


    for iontype in nterm_types:
        the_ions = idict[iontype]

        for ion in pkd:
            res = search(ion, the_ions, 10)
            if res > 0:
                intsbypos[res] += pkd[ion]

    for iontype in cterm_types:
        the_ions = idict[iontype]

        for ion in pkd:
            res = search(ion, the_ions, 10)
            if res > 0:
                intsbypos[lenseq - res + 1] += pkd[ion]

    dictrange = range(1,len(intsbypos)+1)


    outputformat =[]
    for thing in dictrange:
        outputformat.append(str(thing)+', '+str(intsbypos[thing]))

    return '<br>'.join(outputformat)