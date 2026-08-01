from .arc import build as arc


def build(
    x,
    y,
    heading,
):

    return arc(
        x=x,
        y=y,
        heading=heading,
        radius=220,
        angle=40,
    )