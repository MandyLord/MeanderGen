"""
MeanderGen - svg_writer.py

Writes a Path to a simple SVG file.
"""

from pathlib import Path as FilePath

class SVGWriter:
    @staticmethod
    def path_to_svg(path, width=100, height=100, stroke_width=2):
        pts = path.points()
        if not pts:
            raise ValueError("Path contains no points.")
        d = f"M {pts[0].x} {pts[0].y} " + " ".join(
            f"L {p.x} {p.y}" for p in pts[1:]
        )
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{width}" height="{height}"
     viewBox="0 0 {width} {height}">
  <path d="{d}"
        fill="none"
        stroke="black"
        stroke-width="{stroke_width}"
        stroke-linecap="round"
        stroke-linejoin="round"/>
</svg>"""

    @staticmethod
    def write(path, filename, width=100, height=100):
        svg = SVGWriter.path_to_svg(path, width, height)
        FilePath(filename).write_text(svg, encoding="utf-8")

