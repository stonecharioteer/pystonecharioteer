"""QTile configuration submodule"""


def config():
    """This function modifies the global variables, injecting
    parameters required to customize qtile."""

    from libqtile.utils import guess_terminal
    from stonecharioteer.qtile.groups import groups
    from stonecharioteer.qtile.inputs import MOD
    from stonecharioteer.qtile.layouts import layouts
    from stonecharioteer.qtile.screens import configure_screens
    from stonecharioteer.qtile.keymaps import configure_keymaps

    screens = configure_screens()
    globals()["mod"] = MOD
    globals()["groups"] = groups
    globals()["terminal"] = guess_terminal()
    globals()["layouts"] = layouts
    globals()["screens"] = screens
    globals()["keys"] = configure_keymaps(groups=groups)

    # FIXME: Remove these later, or investigate if they're required.
    dgroups_key_binder = None
    globals()["dgroups_key_binder"] = dgroups_key_binder
    dgroups_app_rules = []  # type: List
    globals()["dgroups_app_rules"] = dgroups_app_rules
    follow_mouse_focus = True
    globals()["follow_mouse_focus"] = follow_mouse_focus
    bring_front_click = False
    globals()["bring_front_click"] = bring_front_click
    cursor_warp = False
    globals()["cursor_warp"] = cursor_warp
    auto_minimize = True
    globals()["auto_minimize"] = auto_minimize
