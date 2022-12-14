from libqtile import layout

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=1, margin=5),
    layout.Max(),
    layout.Tile(),
    layout.Zoomy(),
]
