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
out_op = op("address_to_file")
in_op = op("address_storage_in")
source = op("addresses_sorted")
# active_addresses = op("active_addresses")
pre_write = op("pre_write")


def de_dupe():
    if len(pre_write.rows(val=True)) > 0:
        for address in pre_write.rows(val=True)[0]:
            if in_op.row(address) != None:
               # print(address)
                try:
                    pre_write.deleteRow(address)
                except ValueError:
                    pass


def check_and_append(dat):
    if len(pre_write.rows(val=True)) > 0:
        for address in pre_write.rows(val=True)[0]:
            if source.row(address) == None:
                try:
                    pre_write.deleteRow(address)
                except ValueError:
                    pass
    for address in dat.rows(val=True)[0]:
        # print(in_op.row(address))
        if in_op.row(address) == None and pre_write.row(address) == None:
            pre_write.appendRow(address)
        elif in_op.row(address) != None:
            try:
                pre_write.deleteRow(address)
            except ValueError:
                pass
        # for row in pre_write.rows(val=True):
    # print(row)


def save(dat):
    de_dupe()
    save = int(dat[0, 1])
    clear = dat[1, 1]
    out_op.par.append = 0
    out_op.par.write.expr = save
    in_op.par.refreshpulse = save


def onTableChange(dat):
    return


# if address[0] in active_addresses.rows(val=True):
#     pass
# else:
#     pre_write.appendRow(address)
def onRowChange(dat, rows):

    dat_name = str(dat).split("/")[-1]

    if dat_name == "controls":
        save(dat)
    if dat_name == "addresses_sorted":
        pre_write.clear()
        check_and_append(dat)

    if int(in_op.numRows) == 0:
        out_op.par.append = 0
    if int(in_op.numRows) > 0:
        out_op.par.append = 1

    # else:
    #     out_op.par.write = save
    # print(save)
    #     for row in op("address_storage").rows(val=True):
    #         address = row[0]
    #         with open("addresses.csv") as fd:
    #             fd.write(address)
    #             fd.close()

    return


def onColChange(dat, cols):
    return


def onCellChange(dat, cells, prev):
    return


def onSizeChange(dat):
    return
