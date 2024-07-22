# edits custom operator network for value assignment
def onTableChange(dat):
    return


def onRowChange(dat, rows):
    return


def onColChange(dat, cols):
    return


def onCellChange(dat, cells, prev):
    if op("null1")[0, 0].val == "edit":
        viewer = ui.panes.createFloating(
            type=PaneType.NETWORKEDITOR, name=op("value_name")[0, 0].val
        )
        viewer.owner = op("value_ops")
    return


def onSizeChange(dat):
    return
