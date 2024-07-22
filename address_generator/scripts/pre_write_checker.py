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
# active_addresses = op("active_addresses")
pre_write = op("pre_write")
address_ingredients = op("address_ingredients") 

def onTableChange(dat):
    return


# if address[0] in active_addresses.rows(val=True):
#     pass
# else:
#     pre_write.appendRow(address)
def onRowChange(dat, rows):
    dat_name = str(dat).split("/")[-1]
    print(dat_name)
    rowVals = dat.Rows(rows, val=True)
    print(dat.rows(val=True))
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
