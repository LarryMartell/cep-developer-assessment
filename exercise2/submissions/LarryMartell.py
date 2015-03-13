#!/usr/bin/python2.7

# CEP Exercise2 by Larry Martell 15-03-13

import scipy.stats as stats
import traceback, sys, csv
from collections import defaultdict

class Exercise2():

    def __init__(self):
        self.meanFile = '../input/mean.csv'
        self.outFile = './pct.csv'
        self.questions = ['fldimp', 'undrfld', 'advknow', 'pubpol', 'comimp', 'undrwr', 'undrsoc', 'orgimp', 'impsust']

    def run(self):
        self.genPercentiles()

    def genPercentiles(self):
        percentiles = defaultdict(dict)
        ratings = defaultdict(list)
        means = defaultdict(float)
        try:
            with open(self.meanFile) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    for question in self.questions:
                        ratings[question].append(row[question])
                        means[row['fdntext'], question] = row[question]

            for key in means:
                (fdntext, question) = key
                percentiles[fdntext].update({question: stats.percentileofscore(ratings[question], means[key], 'mean')})

            f = open(self.outFile, 'w')
            f.write('fdntext,'+','.join(self.questions)+'\n')
            for fdntext in sorted(percentiles.keys()):
                thisRow = percentiles[fdntext]
                rowData = []
                f.write(fdntext+',')
                for question in self.questions:
                    rowData.append(str(thisRow[question]))

                f.write(','.join(rowData)+'\n')
                
            f.close()

        except Exception, e:
            (type, value, tb) = sys.exc_info()
            traceback.print_exception(type, value, tb)
            sys.stdout.flush()
            print >>sys.stderr, '%s' % e
            sys.exit(1)


if __name__ == "__main__":
    e2 = Exercise2()
    e2.run()
    exit(0)
