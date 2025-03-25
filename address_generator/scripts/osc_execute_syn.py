source = op("osc_table_syn")


def row_to_osc(row):
    try:
        out = op("oscsyn").sendOSC(source[row, 0].val, [float(source[row, 1].val)])
        return out
    except:
        pass
    # print(row)


def onTableChange(dat):
    return


def onRowChange(dat, rows):
    for row in range(source.numRows):
        row_to_osc(row)
    return


def onColChange(dat, cols):
    return


def onCellChange(dat, cells, prev):
    return


def onSizeChange(dat):
    return
