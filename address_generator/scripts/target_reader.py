#
# dat - the changed DAT
# rows - a list of row indices
# cols - a list of column indices
# cells - the list of cells that have changed content
# prev - the list of previous string contents of the changed cells
#

address_storage = op("address_storage")
in_op = op("address_storage_in")
clip_selection = op("clips")
address_list = []


def read_ingredients():
    address_storage.clear()
    ingredients = op("address_ingredients").col(0, val=True)
    scope = ingredients[0]
    effect_name = ingredients[1]
    param_name = ingredients[2]
    if effect_name != None and param_name != None:
        return {
            "scope": scope,
            "effect name": effect_name,
            "parameter name": param_name,
        }
    else:
        return None


def check_input(effect_name, param_name, scope, value):
    if effect_name != None and param_name != None:
        field_check = True
        return field_check
    else:
        # print("no")
        field_check = False
        return field_check


def layer_address(layer, effect_name, param_name, on_off):
    ingredients = op("address_ingredients").col(0, val=True)
    address_storage.clear()
    address = "/composition/layers/{}/video/effects/{}/effect/{}/".format(
        layer, effect_name, param_name
    )
    # print(address)
    if (
        on_off == 1
        and address_storage.row(address) == None
        and in_op.row(address) == None
        and ingredients[1] != None
    ):
        address_storage.appendRow(address)
    elif on_off == 0 and address_storage.row(address) != None:
        address_storage.deleteRows(address)
    return


def comp_address(effect_name, param_name):
    # op("pre_write").clear()
    address = "/composition/effects/{}/effect/{}".format(effect_name, param_name)
    if (
        # check_input(effect_name, param_name) == True
        address_storage.row(address)
        == None
    ):
        print(address)
        address_storage.appendRow(address)
    elif address_storage.row(address) != None:
        # address_storage.deleteRow(address)
        pass


def clip_address(mapped, effect_name, param_name):
    # address_storage.clear()

    for pair in mapped:
        layer = pair[0].row + 1
        column = pair[0].col + 1
        current = int(pair[0].val)
        previous = int(pair[1])

        address = "/composition/layers/{}/clips/{}/effects/{}/effect/{}".format(
            layer, column, effect_name, param_name
        )
        if (
            check_input(effect_name, param_name) == True
            and address_storage.row(address) == None
            and previous == 0
        ):
            # print(address)
            address_storage.appendRow(address)
        elif previous == 1 and address_storage.row(address) != None:
            address_storage.deleteRow(address)
    return


def onTableChange(dat):
    return


def onRowChange(dat, rows):
    # op("pre_write").clear()
    inputs = read_ingredients()
    # print(inputs)
    incoming = str(dat).split("/")[-1]
    effect_name = inputs.get("effect name")
    param_name = inputs.get("parameter name")
    scope = inputs.get("scope")
    row = rows[0]
    # print(scope)
    if scope == "Layer" and incoming == "layers":
        source = op("layers")
        layer_val = source[row, 0]
        on_off = int(source[row, 1])
        layer_address(str(layer_val)[-1], effect_name, param_name, on_off)
    elif scope == "Composition":  # and incoming == "address_ingredients":
        comp_address(effect_name, param_name)
        # elif scope == "Clip" and incoming == "address_ingredients":
        # clip_address(
        pass
    return


def onColChange(dat, cols):
    return


def onCellChange(dat, cells, prev):
    inputs = read_ingredients()
    # address_storage.clear()
    effect_name = inputs.get("effect name")
    param_name = inputs.get("parameter name")
    incoming = str(dat).split("/")[-1]
    if incoming == "scope":
        if inputs.get("scope") != prev[0]:
            address_storage.clear()
    elif incoming == "clips":
        mapped = zip([cell for cell in cells], prev)
        clip_address(mapped, effect_name, param_name)
    return


def onSizeChange(dat):
    return
