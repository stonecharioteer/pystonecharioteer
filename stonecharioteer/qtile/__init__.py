"""QTile configuration submodule"""


def qtile_config():
    """This function modifies the global variables, injecting
    parameters required to customize qtile."""
    from stonecharioteer.qtile.panels import panels
    from stonecharioteer.qtile.groups import groups
    from stonecharioteer.qtile.keymaps import keymaps, mod

    globals()["panels"] = panels
    globals()["mod"] = mod
    globals()["keymaps"] = keymaps
    globals()["groups"] = groups
