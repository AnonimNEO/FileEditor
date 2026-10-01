# Данное Свободное Программное Обеспечение распространяется по лицензии GPL-3.0-only или GPL-3.0-or-later
# Вы имеете право копировать, изменять, распространять, взимать плату за физический акт передачи копии, и вы можете по своему усмотрению предлагать гарантийную защиту в обмен на плату
# ДЛЯ ИСПОЛЬЗОВАНИЯ ДАННОГО СВОБОДНОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ВАМ НЕ ТРЕБУЕТСЯ ПРИНЯТИЕ ЛИЦЕНЗИИ Gnu GPL v3.0 или более поздней версии
# В СЛУЧАЕ РАСПРОСТРАНЕНИЯ ОРИГИНАЛЬНОЙ ПРОГРАММЫ И/ИЛИ МОДЕРНИЗИРОВАННОЙ ВЕРСИИ И/ИЛИ ИСПОЛЬЗОВАНИЕ ИСХОДНИКОВ В СВОЕЙ ПРОГРАММЕ, ВЫ ОБЯЗАНЫ ЗАДОКУМЕНТИРОВАТЬ ВСЕ ИЗМЕНЕНИЯ В КОДЕ И ПРЕДОСТАВИТЬ ПОЛЬЗОВАТЕЛЯМ ВОЗМОЖНОСТЬ ПОЛУЧИТЬ ИСХОДНИКИ ВАШЕЙ КОПИИ ПРОГРАММЫ, А ТАКЖЕ УКАЗАТЬ АВТОРСТВО ДАННОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
# ПРИ РАСПРОСТРАНЕНИИ ПРОГРАММЫ ВЫ ОБЯЗАНЫ ПРЕДОСТАВИТЬ ВСЕ ТЕЖЕ ПРАВА ПОЛЬЗОВАТЕЛЮ ЧТО И МЫ ВАМ, А ТАКЖЕ ЛИЦЕНЗИЯ GPL v3
# Прочитать полную версию лицензии вы можете по ссылке Фонда Свободного Программного Обеспечения - https://www.gnu.org/licenses/gpl-3.0.html
# Или в файле COPYING.txt в архиве с установщиком
# Copyleft 🄯 NEO Organization, Departament K 2024 - 2026
# Coded by AnonimNEO (Github)

import tkinter as tk
from tkinter import ttk, Menu

from languages import l
from config import THEME

OTHER_FUNCTION_VERSION = "0.14.9 Beta"


def _tint(w, theme):
    """Красит один уже созданный tk-виджет по его классу."""
    cls = w.winfo_class()
    bg, fg, abg, afg = theme["bg"], theme["fg"], theme["abg"], theme["afg"]
    bbg, bfg = theme["bbg"], theme["bfg"]

    cfg = {
        "Tk":         {"background": bg},
        "Toplevel":   {"background": bg},
        "Frame":      {"background": bg},
        "Labelframe": {"background": bg},
        "Label":      {"background": bg, "foreground": fg},
        "Text":       {"background": bg, "foreground": fg, "insertbackground": fg,
                       "selectbackground": abg, "selectforeground": afg},
        "Entry":      {"background": bg, "foreground": fg, "insertbackground": fg,
                       "selectbackground": abg, "selectforeground": afg},
        "Button":     {"background": bbg, "foreground": bfg,
                       "activebackground": abg, "activeforeground": afg},
        "Checkbutton":{"background": bg, "foreground": fg,
                       "activebackground": abg, "activeforeground": afg, "selectcolor": abg},
        "Radiobutton":{"background": bg, "foreground": fg,
                       "activebackground": abg, "activeforeground": afg, "selectcolor": abg},
        "Scrollbar":  {"background": bbg, "troughcolor": bg, "activebackground": abg},
        "Menu":       {"background": bg, "foreground": fg,
                       "activebackground": abg, "activeforeground": afg},
    }.get(cls)

    if cfg:
        try:
            w.configure(**cfg)
        except tk.TclError:
            pass


def update_existing_widgets(widget, theme):
    """Рекурсивно перекрашивает уже созданные классические tk-виджеты."""
    _tint(widget, theme)
    try:
        for child in widget.winfo_children():
            update_existing_widgets(child, theme)
    except tk.TclError:
        pass


def apply_global_theme(window, current_theme):
    """
    Применяет тему к окну.
      1) option_add — цвета для БУДУЩИХ tk-виджетов;
      2) ttk.Style  — единый стиль для ttk-виджетов.
    """
    style = ttk.Style(window)
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    t = current_theme
    bg, fg, abg, afg, bbg, bfg = t["bg"], t["fg"], t["abg"], t["afg"], t["bbg"], t["bfg"]

    # === 1. ОПЦИИ ДЛЯ БУДУЩИХ TK-ВИДЖЕТОВ ===
    # (класс): [(суффикс опции, значение)]
    tk_options = {
        "":            [("Background", bg), ("Foreground", fg)],
        "Menu":        [("background", bg), ("foreground", fg),
                        ("activeBackground", abg), ("activeForeground", afg),
                        ("selectColor", abg)],
        "Text":        [("Background", bg), ("Foreground", fg), ("InsertBackground", fg),
                        ("SelectBackground", abg), ("SelectForeground", afg)],
        "Entry":       [("Background", bg), ("Foreground", fg), ("InsertBackground", fg),
                        ("SelectBackground", abg), ("SelectForeground", afg)],
        "Checkbutton": [("Background", bg), ("Foreground", fg),
                        ("activeBackground", abg), ("activeForeground", afg),
                        ("selectColor", abg)],
        "Radiobutton": [("Background", bg), ("Foreground", fg),
                        ("activeBackground", abg), ("activeForeground", afg),
                        ("selectColor", abg)],
        "Button":      [("Background", bbg), ("Foreground", bfg),
                        ("activeBackground", abg), ("activeForeground", afg)],
    }
    for cls, opts in tk_options.items():
        for suffix, value in opts:
            window.option_add(f"*{cls}.{suffix}" if cls else f"*{suffix}", value)

    # === 2. СТИЛИ ДЛЯ TTK-ВИДЖЕТОВ ===
    # Общий стиль
    style.configure(".", background=bg, foreground=fg, fieldbackground=bg,
                    bordercolor=bbg, lightcolor=bg, darkcolor=bg,
                    troughcolor=bg, selectbackground=abg, selectforeground=afg)

    # (имя стиля, {опции}, {карты состояний})
    styles = [
        ("TFrame",       {"background": bg}, {}),
        ("TLabelframe",  {"background": bg, "foreground": fg, "bordercolor": bbg}, {}),
        ("TLabelframe.Label", {"background": bg, "foreground": fg}, {}),
        ("TLabel",       {"background": bg, "foreground": fg}, {}),
        ("TButton",      {"background": bbg, "foreground": bfg, "bordercolor": bbg,
                          "lightcolor": bbg, "darkcolor": bbg, "padding": (10, 5)},
                         {"background": [("pressed", abg), ("active", abg), ("disabled", bg)],
                          "foreground": [("pressed", afg), ("active", afg), ("disabled", bfg)],
                          "bordercolor": [("active", abg), ("pressed", abg)]}),
        ("TEntry",       {"fieldbackground": bg, "foreground": fg,
                          "bordercolor": bbg, "padding": 5},
                         {"fieldbackground": [("focus", bg), ("disabled", bbg)],
                          "foreground": [("disabled", bfg)],
                          "bordercolor": [("focus", abg)]}),
        ("TCombobox",    {"fieldbackground": bg, "background": bbg, "foreground": fg,
                          "bordercolor": bbg, "arrowcolor": fg, "padding": 5},
                         {"fieldbackground": [("readonly", bg), ("focus", bg)],
                          "foreground": [("readonly", fg), ("focus", fg)],
                          "selectbackground": [("focus", abg)],
                          "selectforeground": [("focus", afg)],
                          "arrowcolor": [("active", afg)]}),
        ("TCheckbutton", {"background": bg, "foreground": fg, "focuscolor": bg},
                         {"background": [("active", bg), ("selected", bg)],
                          "foreground": [("active", afg), ("selected", fg)],
                          "indicatorcolor": [("selected", abg), ("active", abg)]}),
        ("TRadiobutton", {"background": bg, "foreground": fg, "focuscolor": bg},
                         {"background": [("active", bg), ("selected", bg)],
                          "foreground": [("active", afg), ("selected", fg)],
                          "indicatorcolor": [("selected", abg), ("active", abg)]}),
        ("Treeview",     {"background": bg, "foreground": fg, "fieldbackground": bg,
                          "bordercolor": bbg, "rowheight": 25},
                         {"background": [("selected", abg)],
                          "foreground": [("selected", afg)]}),
        ("Treeview.Heading", {"background": bbg, "foreground": bfg, "bordercolor": bbg,
                              "relief": "flat", "padding": (5, 4),
                              "font": ("TkDefaultFont", 10, "bold")},
                             {"background": [("active", abg), ("pressed", abg)],
                              "foreground": [("active", afg), ("pressed", afg)]}),
        ("TNotebook",    {"background": bg, "borderwidth": 0, "tabmargins": (0, 0, 0, 0)}, {}),
        ("TNotebook.Tab",{"background": bbg, "foreground": bfg, "bordercolor": bbg,
                          "padding": (10, 5)},
                         {"background": [("selected", abg), ("active", abg)],
                          "foreground": [("selected", afg), ("active", afg)]}),
        ("TScrollbar",   {"background": bbg, "troughcolor": bg, "bordercolor": bg,
                          "arrowcolor": fg, "lightcolor": bbg, "darkcolor": bbg},
                         {"background": [("active", abg), ("pressed", abg)],
                          "arrowcolor": [("active", afg), ("pressed", afg)]}),
        ("TProgressbar", {"background": abg, "troughcolor": bg, "bordercolor": bbg,
                          "lightcolor": abg, "darkcolor": abg}, {}),
        ("TScale",       {"background": bg, "troughcolor": bbg, "bordercolor": bbg}, {}),
        ("TSeparator",   {"background": bbg}, {}),
        ("TSpinbox",     {"fieldbackground": bg, "foreground": fg,
                          "bordercolor": bbg, "arrowcolor": fg},
                         {"fieldbackground": [("focus", bg)],
                          "bordercolor": [("focus", abg)]}),
    ]
    for name, opts, maps in styles:
        style.configure(name, **opts)
        for key, val in maps.items():
            style.map(name, **{key: val})

    window.configure(background=bg)


def restart_gui_for_theme(GUI, user_theme):
    """Применяет тему «на лету»: ttk + перекраска уже созданных tk-виджетов."""
    theme = THEME[user_theme]
    apply_global_theme(GUI, theme)
    update_existing_widgets(GUI, theme)


def create_menubar(GUI, RUN_IN_RECOVERY, component_func=None, component_func2=None,
                   component_func3=None, component_func4=None,
                   component_func5=None, component_func6=None):
    """
    Создаёт стандартную верхнюю панель.
    GUI               — окно tkinter
    RUN_IN_RECOVERY   — True, если код работает в среде восстановления
    component_func…6  — функции пунктов меню
    """
    menubar = Menu(GUI)

    # Файл
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=l("file"), menu=file_menu)
    for lbl, cmd, acc in [
        (l("open"),    component_func,  "Ctrl+O"),
        (l("save"),    component_func2, "Ctrl+S"),
        (l("save_as"), component_func3, "Ctrl+Shift+S"),
    ]:
        file_menu.add_command(label=lbl, command=cmd, accelerator=acc)
    file_menu.add_separator()
    file_menu.add_command(label=l("exit"), command=component_func4, accelerator="Alt+F4")

    # Вид
    view_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=l("view"), menu=view_menu)

    font_menu = tk.Menu(view_menu, tearoff=0)
    view_menu.add_cascade(label=l("font"), menu=font_menu)
    for font in ["Courier", "Arial", "Times New Roman", "Helvetica", "Verdana", "Consolas"]:
        font_menu.add_command(label=font, command=lambda f=font: component_func5(f))

    size_menu = tk.Menu(view_menu, tearoff=0)
    view_menu.add_cascade(label=l("font_size"), menu=size_menu)
    for size in [8, 10, 11, 12, 14, 16, 18, 20, 24]:
        size_menu.add_command(label=str(size), command=lambda s=size: component_func6(s))

    # Темы
    theme_menu = Menu(menubar, tearoff=0)
    GUI._current_theme = tk.StringVar(master=GUI, value="dark")
    for label, theme_name in [
        ("dark", "dark"), ("white", "white"), ("red", "red"), ("green", "lime"),
        ("contrast", "black"), ("gray", "gray"), ("orange", "orange"),
    ]:
        theme_menu.add_radiobutton(
            label=l(label),
            variable=GUI._current_theme,
            value=theme_name,
            command=lambda: restart_gui_for_theme(GUI, GUI._current_theme.get()),
        )
    menubar.add_cascade(label=l("themes"), menu=theme_menu)

    # Поверх всех окон
    higher = tk.BooleanVar(value=not RUN_IN_RECOVERY)

    def toggle_topmost():
        higher.set(not higher.get())
        GUI.attributes("-topmost", higher.get())
        status = l("on2") if higher.get() else l("off2")
        menubar.entryconfig(topmost_index, label=f'{l("topmost")}: {status}')

    menubar.add_command(label=f'{l("topmost")}: {l("on2")}', command=toggle_topmost)
    topmost_index = menubar.index("end")

    GUI.config(menu=menubar)

    if not RUN_IN_RECOVERY:
        GUI.attributes("-topmost", True)