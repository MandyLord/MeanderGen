"""
MeanderGen - svg_writer.py

Writes a Path to a simple SVG file.
"""

from pathlib import Path as FilePath


class SVGWriter:

    @staticmethod
    def path_to_svg(
        path,
        width=100,
        height=100,
        stroke_width=2,
        development=False,
    ):
        pts = path.points()

        if not pts:
            raise ValueError("Path contains no points.")

        d = f"M {pts[0].x} {pts[0].y} " + " ".join(
            f"L {p.x} {p.y}" for p in pts[1:]
        )

        background = ""
        markers = ""
        stroke = "black"

        if development:
            stroke = "#1B5E20"

            background = f"""
  <rect x="0" y="0"
        width="{width}"
        height="{height}"
        fill="white"/>
"""

            markers = f"""
  <circle cx="{pts[0].x}" cy="{pts[0].y}" r="2.5"
          fill="limegreen"/>

  <circle cx="{pts[-1].x}" cy="{pts[-1].y}" r="2.5"
          fill="red"/>
"""

        return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{width}" height="{height}"
     viewBox="0 0 {width} {height}">
{background}
  <text x="10"
        y="22"
        font-family="Arial"
        font-size="14"
        fill="#444">
        MeanderGen - Development Preview
        </text>
  <path d="{d}"
        fill="none"
        stroke="{stroke}"
        stroke-width="{stroke_width}"
        stroke-linecap="round"
        stroke-linejoin="round"/>
{markers}
</svg>"""

    @staticmethod
    def write(
        path,
        filename,
        width=100,
        height=100,
        development=False,
    ):
        svg = SVGWriter.path_to_svg(
            path,
            width,
            height,
            development=development,
        )
        FilePath(filename).write_text(svg, encoding="utf-8")