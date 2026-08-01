from math import cos, radians, sin


def build(
    x,
    y,
    heading,
    radius,
    angle,
    step=3.5,
):

    points = []

    turn = step / radius
    turn = turn * 57.2958  # radians -> degrees

    stitches = int((angle / turn) + 0.5)

    for _ in range(stitches):

        heading += turn

        x += cos(radians(heading)) * step
        y += sin(radians(heading)) * step

        points.append(
            (
                round(x),
                round(y),
            )
        )

    return (
        points,
        x,
        y,
        heading,
    )