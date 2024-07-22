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
char_dict = {"1": chr(0x000025B2), "0": chr(0x000025BC)}


def onTableChange(dat):
    return


def onRowChange(dat, rows):
    effect = op("effect_name")[0, 0].val
    button_state = op("display_param")[0, 0].val
    #print(button_state)
    parent_state = op("display_param")[1, 0].val
    op("effect").par.label = "{}\t {}".format(char_dict.get(button_state), effect)
    param_height = op('params').par.h
    op(parent()).par.h = 32 + param_height
    op("params").par.display = button_state


    # if button_state == '0': parent().par.height == parent
    return


def onColChange(dat, cols):
    return


def onCellChange(dat, cells, prev):
    return


def onSizeChange(dat):
    return
