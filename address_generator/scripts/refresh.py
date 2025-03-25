# me - this DAT.
#
# dat - the changed DAT
# rows - a list of row indices
# cols - a list of column indices
# cells - the list of cells that have changed content
# prev - the list of previous string contents of the changed cells
#
# Make sure the corresponding toggle is enabled in the DAT Execute DAT.
#
# If rows or columns are deleted, sizeChange will be called instead of row/col/cellChange.


def onTableChange(dat):
    # op('custom_replicate').par.recreatemissing.pulse()
    # for x in [op('item{}'.f).par
    # op(name).par.alignorder = op('saved_names_sorted').col(0).index(name)
    r = range(0, op("saved_names_sorted").numRows, 1)
    for a in r:
        try:
            n = op("item{}/value_name".format(a)).row(0, val=True)
            i = op("saved_names_sorted").col(0, val=True).index(n[0])
            op("item{}".format(a)).par.alignorder = i
            print(i)
        except:
            print('check refresh script dat in value assignment')
            pass
    return


def onRowChange(dat, rows):
    r = range(0, op("saved_names_sorted").numRows, 1)
    for r in range:
        n = op("item{}/value_name".format(r)).row(0, val=True)
        i = op("saved_names_sorted").col(0, val=True).index(n)
        print(i)
    return


def onColChange(dat, cols):
    return


def onCellChange(dat, cells, prev):
    return


def onSizeChange(dat):
    return
