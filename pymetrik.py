import pandas as pd

def getSamePeaks(df, keycolumn):
    grouped = df.groupby(keycolumn)
    samePeakDfs = []
    for k,v in grouped.groups.iteritems():
        if len(v) > 1:
            samePeakDfs.append(grouped.get_group(k))
    return samePeakDfs

