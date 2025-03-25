# edits custom operator network for value assignment
def onTableChange(dat):
    return


def onRowChange(dat, rows):
    return


def onColChange(dat, cols):
    return


def onCellChange(dat, cells, prev):
    value_name = op("value_name")[0, 0].val
    if op("null1")[0, 0].val == "edit":
        viewer = ui.panes.createFloating(
            type=PaneType.NETWORKEDITOR, name=op("value_name")[0, 0].val
        )
        viewer.owner = op("value_ops")
    elif op("null1")[0, 0].val == "delete":
        op("../create_custom/created_vals").deleteRow(value_name)
        parent().destroy()
    return


def onSizeChange(dat):
    return
