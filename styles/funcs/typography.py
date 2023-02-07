from nicegui.element import Element
from styles.types import typography


class Typography:
    def __init__(self, element: Element) -> None:
        self.element = element

    def add(self, Class: str) -> None:
        self.element.classes(add=Class)

    def font_family(self, family: typography.FontFamily):
        self.add(f"font-{family}")
        return self

    def font_size(self, size: typography.FontSize):
        self.add(f"text-{size}")
        return self

    def font_smoothing(self, smoothing: typography.FontSmoothing):
        self.add(smoothing)
        return self

    def font_style(self, style: typography.FontStyle):
        self.add(style)
        return self

    def font_weight(self, weight: typography.FontWeight):
        self.add(f"font-{weight}")
        return self

    def font_variant_numeric(self, variant: typography.FontVariantNumeric):
        self.add(variant)
        return self

    def letter_spacing(self, spacing: typography.LetterSpacing):
        self.add(spacing)
        return self

    def line_height(self, height: typography.LineHeight):
        self.add(f"leading-{height}")
        return self

    def list_style_type(self, type: typography.ListStyleType):
        self.add(f"list-{type}")
        return self

    def list_style_position(self, position: typography.ListStylePosition):
        self.add(f"list-{position}")
        return self

    def text_align(self, align: typography.TextAlign):
        self.add(f"text-{align}")
        return self

    def text_color(self, color: typography.TextColor):
        self.add(f"text-{color}")
        return self

    def text_decoration(self, decoration: typography.TextDecoration):
        self.add(decoration)
        return self

    def text_decoration_color(self, color: typography.TextDecorationColor):
        self.add(f"decoration-{color}")
        return self

    def text_decoration_style(self, style: typography.TextDecorationStyle):
        self.add(f"decoration-{style}")
        return self

    def text_decoration_thickness(self, thickness: typography.TextDecorationThickness):
        self.add(f"decoration-{thickness}")
        return self

    def text_underline_offset(self, underline: typography.TextUnderlineOffset):
        self.add(f"underline-{underline}")
        return self

    def text_transform(self, transform: typography.TextTransform):
        self.add(transform)
        return self

    def text_overflow(self, overflow: typography.TextOverflow):
        self.add(overflow)
        return self

    def text_indent(self, indent: typography.TextIndent):
        self.add(f"indent-{indent}")
        return self

    def vertical_align(self, align: typography.VerticalAlign):
        self.add(f"vertical-{align}")
        return self

    def whitespace(self, whitespace: typography.Whitespace):
        self.add(f"whitespace-{whitespace}")
        return self

    def word_break(self, wbreak: typography.WordBreak):
        self.add(f"break-{wbreak}")
        return self
