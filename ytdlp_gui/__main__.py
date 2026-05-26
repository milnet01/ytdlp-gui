"""Entry point for running as: python -m ytdlp_gui"""

from . import HAS_DND


def main():
    if HAS_DND:
        from tkinterdnd2 import TkinterDnD
        root = TkinterDnD.Tk(className="YT-DLP")
    else:
        import tkinter as tk
        root = tk.Tk(className="YT-DLP")

    from .app import YTDLPGui
    app = YTDLPGui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
