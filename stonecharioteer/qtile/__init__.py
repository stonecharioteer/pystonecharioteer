"""QTile configuration submodule"""


def config():
    """This function modifies the global variables, injecting
    parameters required to customize qtile."""
    
    from libqtile.utils import guess_terminal
    from stonecharioteer.qtile.groups import groups
    from stonecharioteer.qtile.inputs import MOD
    from stonecharioteer.qtile.layouts import layouts
    from stonecharioteer.qtile.screens import configure_screens

    globals()["mod"] = MOD
    globals()["groups"] = groups
    globals()["terminal"] = guess_terminal()
    globals()["layouts"] = layouts
    globals()["screens"] = configure_screens()
    
