# me - this DAT
#
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
#
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.


def onOffToOn(channel, sampleIndex, val, prev):
    value_name = op("value_name")[0, 0].val
    if op("edit_delete")[0] == 1.0:
        viewer = ui.panes.createFloating(
            type=PaneType.NETWORKEDITOR, name=op("value_name")[0, 0].val
        )
        viewer.owner = op("value_ops")
    elif op("edit_delete")[1] == 1.0:
        source_table = op(parent().parent().parent() + "/create_custom/created_vals")
        try:
            source_table.deleteRow(value_name)
            parent().destroy()
        except:
            parent().destroy()
    return

    def whileOn(channel, sampleIndex, val, prev):
        return

    def onOnToOff(channel, sampleIndex, val, prev):
        return

    def whileOff(channel, sampleIndex, val, prev):
        return

    def onValueChange(channel, sampleIndex, val, prev):

        return
