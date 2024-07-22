base_path_clip = "/composition/layers/{}/clips/{}/video/effects/{}/effect/{}"
base_path_source = "/composition/layers/{}/clips/{}/video/source/{}/{}"
speed_path_clip = (
    "/composition/layers/{}/clips/{}/video/effects/{}/effect/{}/behaviour/speed"
)
opacity_path_clip = "/composition/layers/{}/clips/{}/video/effects/{}/{}"


base_path_layer = "/composition/layers/{}/video/effects/{}/effect/{}"
speed_path_layer = "/composition/layers/{}/video/effects/{}/effect/{}/behaviour/speed"
opacity_path_layer = "/composition/layers/{}/video/effects/{}/{}"


base_path_comp = "/composition/video/effects/{}/effect/{}"
opacity_path_comp = "/composition/video/effects/{}/{}"
speed_path_comp = "/composition/video/effects/{}/effect/{}/behaviour/speed"


def layer_address(layer, effect_name, param_name, address_type):
    if address_type == "Standard":
        address_base = (
            base_path_layer if param_name.lower() != "opacity" else opacity_path_layer
        )
        address = address_base.format(layer[-1], effect_name, param_name)
    elif address_type == "Speed":
        address_base = (
            speed_path_layer
            if "mosaic" not in effect_name
            else speed_path_layer.replace("behaviour", "behavior")
        )
        address = address_base.format(layer[-1], effect_name, param_name)
    return address


def comp_address(effect_name, param_name, address_type):
    if address_type == "Standard":
        address_base = (
            base_path_comp if param_name.lower() != "opacity" else opacity_path_comp
        )
        address = address_base.format(effect_name, param_name)
        return address

    elif address_type == "Param_Speed":
        address_base = speed_path_comp
        address = address_base.format(effect_name, param_name)
        return address


def clip_address(layer_index, clip_index, effect_name, param_name, address_type):
    if address_type == "Standard":
        address_base = (
            base_path_clip if param_name.lower() != "opacity" else opacity_path_clip
        )
        address = address_base.format(layer_index, clip_index, effect_name, param_name)
    elif address_type == "Speed":
        address_base = (
            speed_path_clip
            if "mosaic" not in effect_name
            else speed_path_clip.replace("behaviour", "behavior")
        )
        address = address_base.format(layer_index, clip_index, effect_name, param_name)
    elif address_type == "Generator":
        address_base = base_path_source
        address = address_base.format(layer_index, clip_index, effect_name, param_name)
    # print(address)
    return address
