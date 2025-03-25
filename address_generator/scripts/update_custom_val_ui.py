# me - this DAT
#
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
#
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.


def onOffToOn(channel, sampleIndex, val, prev):
    parent_name = op("value_name")[0, 0].val
    order = op('../saved_names_sorted').col(0, val=True)
    try: 
        align_order = order.index(parent_name)
    except:
        align_order = 99
    if parent().par.alignorder != align_order:
        try:
            parent().par.alignorder = align_order
        except:
            pass
    if channel.name != parent_name:
        op("select_val").par.value0.reset()
    # print(channel.name)
    return


def whileOn(channel, sampleIndex, val, prev):
    return


def onOnToOff(channel, sampleIndex, val, prev):
    return


def whileOff(channel, sampleIndex, val, prev):
    return


def onValueChange(channel, sampleIndex, val, prev):
    return
