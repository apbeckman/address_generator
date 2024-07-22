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
    return


def onRowChange(dat, rows):
    scope = op("scope")[0, 0].val
    if scope == "Clip":
        parent().par.w = op("parent_width")[0]
        op("clip_select").par.display = 1
        op('layer_select').par.value0.reset()
        op('layer_select').par.uvbuttonsleft = 0
    elif scope == "Layer":
        parent().par.w = op("button_width")[0]
        op("clip_select").par.display = 0
        op('layer_select').par.value0 = 1
        op('layer_select').par.uvbuttonsleft = 1
    return


def onColChange(dat, cols):
    return


def onCellChange(dat, cells, prev):
    return


def onSizeChange(dat):
    return
