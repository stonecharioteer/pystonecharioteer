======================
pystonecharioteer
======================

This is a helper module that I'm maintaining for my own utils and configs.
At the outset, I'm using this to maintain my :code:`qtile` config.

------------------
Installation
------------------

.. code:: bash

    pip install stonecharioteer

-------------------------
`qtile` Configuration
-------------------------

In your :code:`~/.config/qtile/config.py` file, add the following:

.. code:: python

    from stonecharioteer.qtile import config

    c = config()

    mod = c["mod"]
    groups = c["groups"]
    terminal = c["terminal"]
    layouts = c["layouts"]
    screens = c["screens"]
    keys = c["keys"]
    dgroups_key_binder = c["dgroups_key_binder"]
    dgroups_app_rules = c["dgroups_app_rules"]
    follow_mouse_focus = c["follow_mouse_focus"]
    bring_front_click = c["bring_front_click"]
    cursor_warp = c["cursor_warp"]
    auto_minimize = c["auto_minimize"]

Eventually, I want to enable :code:`toml` based configuration for :code:`qtile`.

Obligatory Rice
=================

.. image:: docs/rice-001.png
