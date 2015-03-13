#!/usr/bin/python2.7

# CEP Exercise1 by Larry Martell 15-03-13

import numpy as np
import pandas as ps
import traceback, sys, re, csv

class Exercise1():

    def __init__(self):
        ps.set_option('precision', 16)
        self.inputFile = '../input/xl.csv'
        self.meanFile = './mean.csv'
        self.statsFile = './stats.csv'

        self.questions = ['fldimp', 'undrfld', 'advknow', 'pubpol', 'comimp', 'undrwr', 'undrsoc', 'orgimp', 'impsust']
        self.notInterested = [77, 88]

    def run(self):
        self.genStats()

    def genStats(self):
        try:
            df = ps.read_csv(self.inputFile)

            # recode answers we're not interested in to nan
            for question in self.questions:
                for na in self.notInterested:
                    df.loc[df[question] == na, question] = np.nan

            meanData = df.groupby('fdntext')[self.questions].agg(np.mean)

            f = open(self.meanFile, 'w')
            # remove the trailing zeros
            f.write(re.sub(r'(\.\d+?)0+\b', r'\1', meanData.to_csv(None, float_format='%0.16f')))
            f.close()

            f = open(self.statsFile, 'w')
            f.write(re.sub(r'(\.\d+?)0+\b', r'\1', meanData.describe().to_csv(None, float_format='%0.16f')))
            f.close()

            # stats data
            #statsKeys = ['median', 'std', 'min', '25%', '50%', '75%', 'max']
            #stats = {}
            #stats['min'] =  meanData.min().to_dict()
            #stats['max'] = meanData.max().to_dict()
            #stats['median'] = meanData.median().to_dict()
            #stats['std'] = meanData.std().to_dict()
            #stats['25%'] = meanData.quantile(.25).to_dict()
            #stats['50%'] = meanData.quantile(.50).to_dict()
            #stats['75%'] = meanData.quantile(.75).to_dict()
#
#            with open(self.statsFile, 'wb') as csvfile:
#                w = csv.writer(csvfile)
#                w.writerow(['']+self.questions)
#                r = ['count']
#                for question in self.questions:
#                    r += ["%0.1f" % len(meanData)]
#                w.writerow(r)
#                for s in statsKeys:
#                    r = [s]
#                    for question in self.questions:
#                        r += [stats[s][question]]
#                    w.writerow(r)
#
#            csvfile.close()


        except Exception, e:
            (type, value, tb) = sys.exc_info()
            traceback.print_exception(type, value, tb)
            sys.stdout.flush()
            print >>sys.stderr, '%s' % e
            sys.exit(1)


if __name__ == "__main__":
    e1 = Exercise1()
    e1.run()
    exit(0)
