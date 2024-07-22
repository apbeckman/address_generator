source = op("osc_table")


def row_to_osc(row):
    try:
        out = op("oscres").sendOSC(source[row, 0].val, [float(source[row, 1].val)])
    except:
        out = op("oscres").sendOSC(
            "/" + source[row, 0].val, [float(source[row, 1].val)]
        )
    # print(row)
    return out


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
