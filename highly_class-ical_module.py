with open("fontolor.py","w") as f:
    f.write("""class Fontolor():
    class Text():
        def __init__():
            pass
        def italicize(text,color=51):
            if color != 52 and color > 0 and color < 9:
                tcolor = color+89
            if color == 52:
                return f"\033[{color};3m {text}"
        def highlight(text,color=4):
            if color > 0 and color < 9:
                tcolor = color+39
                return f"\033[{tcolor};5m {text}"
            else:
                pass
        def mix_code(text,code):
            return f"\033[{code}m {text}"
        def underline(text,color=28):
            if color != 28 and color > 0 and color < 9:
                tcolor = color + 89
            if color == 28:
                return f"\033[{color};4m {text}"
        def color_text(text,RGB):
            return f"\033[38;2;{RGB[0]};{RGB[1]};{RGB[2]}m {text}"
            """)
