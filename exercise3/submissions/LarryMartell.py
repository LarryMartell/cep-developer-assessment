#!/usr/bin/python2.7

# CEP Exercise3 by Larry Martell 15-03-13

import traceback, sys, csv, json

class Exercise3():

    def __init__(self):
        self.meanFile = '../input/mean.csv'
        self.statsFile = '../input/stats.csv'
        self.pctFile = '../input/pct.csv'
        self.outFile = './output.json'
        self.client = 'Tremont 14S'
        self.questions = ['fldimp', 'undrfld', 'advknow', 'pubpol', 'comimp', 'undrwr', 'undrsoc', 'orgimp', 'impsust']

        self.jsonMap = {"version": "1.0",
                        "reports": [] }


    def run(self):
        self.makeJSON()

    def makeJSON(self):
        percentiles = {}
        stats = {}
        means = {}
        try:
            with open(self.meanFile) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['fdntext'] == self.client:
                        for question in self.questions:
                            means[question] = row[question]

            with open(self.statsFile) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    for question in self.questions:
                        stats[row[''],question] = row[question]

            with open(self.pctFile) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['fdntext'] == self.client:
                        for question in self.questions:
                            percentiles[question] = row[question]

            absoluteTypes = ['min', '25%', '50%', '75%', 'max']
            report = {"name": "Tremont 14S Report",
                      "title": "Tremont 14S Report",
                      "cohorts": [],
                      "segmentations": [],
                      "elements": {}
                     }

            for question in self.questions:
                absolutes = []
                for absoluteType in absoluteTypes:
                    absolutes.append(stats[absoluteType, question])
                current = {"name": "2014",
                           "value": means[question],
                           "percentage": percentiles[question]}
                element = {question: 
                            {'type': 'percentileChart', 
                             'absolutes': absolutes,
                             'current': current,
                             'cohorts': [],
                             'past_results': [],
                             'segmentations': [] }
                          }

                report['elements'].update(element)

            self.jsonMap['reports'].append(report)

            jsonOut = json.dumps(self.jsonMap, indent=4, separators=(',', ': '))[:]

            f = open(self.outFile, 'w')
            f.write(jsonOut)
            f.close()

        except Exception, e:
            (type, value, tb) = sys.exc_info()
            traceback.print_exception(type, value, tb)
            sys.stdout.flush()
            print >>sys.stderr, '%s' % e
            sys.exit(1)


if __name__ == "__main__":
    e3 = Exercise3()
    e3.run()
    exit(0)
