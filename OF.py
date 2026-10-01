# Данное Свободное Программное Обеспечение распространяется по лицензии GPL-3.0-only или GPL-3.0-or-later
# Вы имеете право копировать, изменять, распространять, взимать плату за физический акт передачи копии, и вы можете по своему усмотрению предлагать гарантийную защиту в обмен на плату
# ДЛЯ ИСПОЛЬЗОВАНИЯ ДАННОГО СВОБОДНОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ВАМ НЕ ТРЕБУЕТСЯ ПРИНЯТИЕ ЛИЦЕНЗИИ Gnu GPL v3.0 или более поздней версии
# В СЛУЧАЕ РАСПРОСТРАНЕНИЯ ОРИГИНАЛЬНОЙ ПРОГРАММЫ И/ИЛИ МОДЕРНИЗИРОВАННОЙ ВЕРСИИ И/ИЛИ ИСПОЛЬЗОВАНИЕ ИСХОДНИКОВ В СВОЕЙ ПРОГРАММЕ, ВЫ ОБЯЗАНЫ ЗАДОКУМЕНТИРОВАТЬ ВСЕ ИЗМЕНЕНИЯ В КОДЕ И ПРЕДОСТАВИТЬ ПОЛЬЗОВАТЕЛЯМ ВОЗМОЖНОСТЬ ПОЛУЧИТЬ ИСХОДНИКИ ВАШЕЙ КОПИИ ПРОГРАММЫ, А ТАКЖЕ УКАЗАТЬ АВТОРСТВО ДАННОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
# ПРИ РАСПРОСТРАНЕНИИ ПРОГРАММЫ ВЫ ОБЯЗАНЫ ПРЕДОСТАВИТЬ ВСЕ ТЕЖЕ ПРАВА ПОЛЬЗОВАТЕЛЮ ЧТО И МЫ ВАМ, А ТАКЖЕ ЛИЦЕНЗИЯ GPL v3
# Прочитать полную версию лицензии вы можете по ссылке Фонда Свободного Программного Обеспечения - https://www.gnu.org/licenses/gpl-3.0.html
# Или в файле COPYING.txt в архиве с установщиком
# Copyleft 🄯 NEO Organization, Departament K 2024 - 2026
# Coded by AnonimNEO (Github)

# Интерфейс
import tkinter as tk
from tkinter import ttk, Menu

from languages import l
from config import THEME

OTHER_FUNCTION_VERSION = "0.14.9 Beta"


def apply_global_theme(window, current_theme):
    """
    Применяет тему к окну и всем виджетам (ttk и обычные tkinter).
    
    current_theme должен содержать ключи:
        bg  — основной фон
        fg  — основной цвет текста
        abg — фон активного или выбранного элемента
        afg — цвет текста активного или выбранного элемента
        bbg — фон кнопок и заголовков
        bfg — цвет текста кнопок и заголовков
    """
    
    style = ttk.Style(window)
    
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass
    
    bg = current_theme["bg"]
    fg = current_theme["fg"]
    active_bg = current_theme["abg"]
    active_fg = current_theme["afg"]
    button_bg = current_theme["bbg"]
    button_fg = current_theme["bfg"]
    
    # Фон основного окна
    window.configure(background=bg)
    
    # === НАСТРОЙКА СТИЛЕЙ TTK-ВИДЖЕТОВ ===
    
    # Общий стиль ttk
    style.configure(
        ".",
        background=bg,
        foreground=fg,
        fieldbackground=bg,
        bordercolor=button_bg,
        lightcolor=bg,
        darkcolor=bg,
        troughcolor=bg,
        selectbackground=active_bg,
        selectforeground=active_fg,
    )
    
    # Рамки
    style.configure("TFrame", background=bg)
    
    style.configure(
        "TLabelframe",
        background=bg,
        foreground=fg,
        bordercolor=button_bg,
    )
    
    style.configure(
        "TLabelframe.Label",
        background=bg,
        foreground=fg,
    )
    
    # Надписи
    style.configure("TLabel", background=bg, foreground=fg)
    
    # Кнопки
    style.configure(
        "TButton",
        background=button_bg,
        foreground=button_fg,
        bordercolor=button_bg,
        lightcolor=button_bg,
        darkcolor=button_bg,
        padding=(10, 5),
    )
    
    style.map(
        "TButton",
        background=[("pressed", active_bg), ("active", active_bg), ("disabled", bg)],
        foreground=[("pressed", active_fg), ("active", active_fg), ("disabled", button_fg)],
        bordercolor=[("active", active_bg), ("pressed", active_bg)],
    )
    
    # Поля ввода ttk.Entry
    style.configure(
        "TEntry",
        fieldbackground=bg,
        foreground=fg,
        bordercolor=button_bg,
        padding=5,
    )
    
    style.map(
        "TEntry",
        fieldbackground=[("focus", bg), ("disabled", button_bg)],
        foreground=[("disabled", button_fg)],
        bordercolor=[("focus", active_bg)],
    )
    
    # Выпадающий список
    style.configure(
        "TCombobox",
        fieldbackground=bg,
        background=button_bg,
        foreground=fg,
        bordercolor=button_bg,
        arrowcolor=fg,
        padding=5,
    )
    
    style.map(
        "TCombobox",
        fieldbackground=[("readonly", bg), ("focus", bg)],
        foreground=[("readonly", fg), ("focus", fg)],
        selectbackground=[("focus", active_bg)],
        selectforeground=[("focus", active_fg)],
        arrowcolor=[("active", active_fg)],
    )
    
    # Флажки
    style.configure(
        "TCheckbutton",
        background=bg,
        foreground=fg,
        focuscolor=bg,
    )
    
    style.map(
        "TCheckbutton",
        background=[("active", bg), ("selected", bg)],
        foreground=[("active", active_fg), ("selected", fg)],
        indicatorcolor=[("selected", active_bg), ("active", active_bg)],
    )
    
    # Переключатели
    style.configure(
        "TRadiobutton",
        background=bg,
        foreground=fg,
        focuscolor=bg,
    )
    
    style.map(
        "TRadiobutton",
        background=[("active", bg), ("selected", bg)],
        foreground=[("active", active_fg), ("selected", fg)],
        indicatorcolor=[("selected", active_bg), ("active", active_bg)],
    )
    
    # Таблица
    style.configure(
        "Treeview",
        background=bg,
        foreground=fg,
        fieldbackground=bg,
        bordercolor=button_bg,
        rowheight=25,
    )
    
    style.map(
        "Treeview",
        background=[("selected", active_bg)],
        foreground=[("selected", active_fg)],
    )
    
    style.configure(
        "Treeview.Heading",
        background=button_bg,
        foreground=button_fg,
        bordercolor=button_bg,
        relief="flat",
        padding=(5, 4),
        font=("TkDefaultFont", 10, "bold"),
    )
    
    style.map(
        "Treeview.Heading",
        background=[("active", active_bg), ("pressed", active_bg)],
        foreground=[("active", active_fg), ("pressed", active_fg)],
    )
    
    # Вкладки
    style.configure(
        "TNotebook",
        background=bg,
        borderwidth=0,
        tabmargins=(0, 0, 0, 0),
    )
    
    style.configure(
        "TNotebook.Tab",
        background=button_bg,
        foreground=button_fg,
        bordercolor=button_bg,
        padding=(10, 5),
    )
    
    style.map(
        "TNotebook.Tab",
        background=[("selected", active_bg), ("active", active_bg)],
        foreground=[("selected", active_fg), ("active", active_fg)],
    )
    
    # Полоса прокрутки
    style.configure(
        "TScrollbar",
        background=button_bg,
        troughcolor=bg,
        bordercolor=bg,
        arrowcolor=fg,
        lightcolor=button_bg,
        darkcolor=button_bg,
    )
    
    style.map(
        "TScrollbar",
        background=[("active", active_bg), ("pressed", active_bg)],
        arrowcolor=[("active", active_fg), ("pressed", active_fg)],
    )
    
    # Прогресс-бар
    style.configure(
        "TProgressbar",
        background=active_bg,
        troughcolor=bg,
        bordercolor=button_bg,
        lightcolor=active_bg,
        darkcolor=active_bg,
    )
    
    # Ползунок
    style.configure(
        "TScale",
        background=bg,
        troughcolor=button_bg,
        bordercolor=button_bg,
    )
    
    # Разделитель
    style.configure("TSeparator", background=button_bg)
    
    # Spinbox
    style.configure(
        "TSpinbox",
        fieldbackground=bg,
        foreground=fg,
        bordercolor=button_bg,
        arrowcolor=fg,
    )
    
    style.map(
        "TSpinbox",
        fieldbackground=[("focus", bg)],
        bordercolor=[("focus", active_bg)],
    )
    
    # === ОБНОВЛЕНИЕ ВСЕХ СУЩЕСТВУЮЩИХ TKINTER-ВИДЖЕТОВ ===
    
    
def update_existing_widgets(widget, theme):
    """
    Рекурсивно обновляет уже созданные стандартные tkinter-виджеты.

    ttk-виджеты здесь специально не перенастраиваются —
    они автоматически используют ttk.Style.
    """

    widget_class = widget.winfo_class()

    try:
        # Корневое окно и обычные фреймы
        if widget_class in ("Tk", "Toplevel", "Frame", "Labelframe"):
            widget.configure(
                background=theme["bg"],
            )

        # Обычный tkinter.Label
        elif widget_class == "Label":
            widget.configure(
                background=theme["bg"],
                foreground=theme["fg"],
            )

        # Обычный tkinter.Text
        elif widget_class == "Text":
            widget.configure(
                background=theme["bg"],
                foreground=theme["fg"],
                insertbackground=theme["fg"],
                selectbackground=theme["abg"],
                selectforeground=theme["afg"],
            )

        # Обычный tkinter.Entry
        elif widget_class == "Entry":
            widget.configure(
                background=theme["bg"],
                foreground=theme["fg"],
                insertbackground=theme["fg"],
                selectbackground=theme["abg"],
                selectforeground=theme["afg"],
            )

        # Обычная tkinter.Button
        elif widget_class == "Button":
            widget.configure(
                background=theme["bbg"],
                foreground=theme["bfg"],
                activebackground=theme["abg"],
                activeforeground=theme["afg"],
            )

        # Обычный tkinter.Checkbutton
        elif widget_class == "Checkbutton":
            widget.configure(
                background=theme["bg"],
                foreground=theme["fg"],
                activebackground=theme["abg"],
                activeforeground=theme["afg"],
                selectcolor=theme["abg"],
            )

        # Обычный tkinter.Radiobutton
        elif widget_class == "Radiobutton":
            widget.configure(
                background=theme["bg"],
                foreground=theme["fg"],
                activebackground=theme["abg"],
                activeforeground=theme["afg"],
                selectcolor=theme["abg"],
            )

        # Обычный tkinter.Scrollbar
        elif widget_class == "Scrollbar":
            widget.configure(
                background=theme["bbg"],
                troughcolor=theme["bg"],
                activebackground=theme["abg"],
            )


    except tk.TclError:
        pass

    # Рекурсивная обработка дочерних виджетов
    try:
        for child in widget.winfo_children():
            update_existing_widgets(child, theme)
    except tk.TclError:
        pass


def restart_gui_for_theme(GUI, user_theme):
    """
    Применяет выбранную тему к GUI и уже существующим виджетам.

    user_theme — ключ темы из словаря THEME.
    """

    current_theme = THEME[user_theme]

    # Применение стилей ко всем ttk-виджетам
    apply_global_theme(
        GUI,
        current_theme,
    )

    # Обновление стандартных tkinter-виджетов
    update_existing_widgets(
        GUI,
        current_theme,
    )

# Создаём пункты в панели
def create_menubar(GUI, RUN_IN_RECOVERY, component_func=None, component_func2=None, component_func3=None, component_func4=None, component_func5=None, component_func6=None):
    """
    Функция для создания стандартной верхней панели
    GUI - окно tkinter
    RUN_IN_RECOVERY - Код работает в среде восстановления? Тогда True
    component_func - 1 Функция компонента которая будет вызываться из панели.
    component_func2 - 2 Функция компонента которая будет вызываться из панели.
    component_func3 - 3 Функция компонента которая будет вызываться из панели.
    component_func4 - 4 Функция компонента которая будет вызываться из панели.
    component_func5 - 5 Функция компонента которая будет вызываться из панели.
    component_func6 - 6 Функция компонента которая будет вызываться из панели.
    return - функция ничего не возвращает!
    """
    menubar = Menu(GUI)
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=l("file"), menu=file_menu)
    file_menu.add_command(label=l("open"), command=component_func, accelerator="Ctrl+O")
    file_menu.add_command(label=l("save"), command=component_func2, accelerator="Ctrl+S")
    file_menu.add_command(label=l("save_as"), command=component_func3, accelerator="Ctrl+Shift+S")
    file_menu.add_separator()
    file_menu.add_command(label=l("exit"), command=component_func4, accelerator="Alt+F4")

    view_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=l("view"), menu=view_menu)

    font_menu = tk.Menu(view_menu, tearoff=0)
    view_menu.add_cascade(label=l("font"), menu=font_menu)

    fonts = ["Courier", "Arial", "Times New Roman", "Helvetica", "Verdana", "Consolas"]
    for font in fonts:
        font_menu.add_command(label=font, command=lambda f=font: component_func5(f))

    size_menu = tk.Menu(view_menu, tearoff=0)
    view_menu.add_cascade(label=l("font_size"), menu=size_menu)

    sizes = [8, 10, 11, 12, 14, 16, 18, 20, 24]
    for size in sizes:
        size_menu.add_command(label=str(size), command=lambda s=size: component_func6(s))
    custom = 0

    theme_menu = Menu(menubar, tearoff=0)
    themes = [("dark", "dark"), ("white", "white"), ("red", "red"), ("green", "lime"), ("contrast", "black"), ("gray", "gray"), ("orange", "orange")]
    # Переменная хранит текущую тему
    GUI._current_theme = tk.StringVar(
        master=GUI,
        value="dark"
    )

    for label, theme_name in themes:
        theme_menu.add_radiobutton(
            label=l(label),
            variable=GUI._current_theme,
            value=theme_name,
            command=lambda: restart_gui_for_theme(
                GUI,
                GUI._current_theme.get()
            )
        )
    menubar.add_cascade(label=l("themes"), menu=theme_menu)

    # Переменные состояния
    higher = tk.BooleanVar(value=not RUN_IN_RECOVERY)

    # Сохраняем индексы с учётом смещения
    topmost_index = (menubar.index("end") + 1 if menubar.index("end") else 1) + custom
    menubar.add_command(label=f'{l("topmost")}: {l("on2")}')

    # Функции переключения
    def toggle_topmost():
        higher.set(not higher.get())
        GUI.attributes("-topmost", higher.get())
        status = l("on2") if higher.get() else l("off2")
        menubar.entryconfig(topmost_index, label=f'{l("topmost")}: {status}')

    # Присваиваем команды
    menubar.entryconfig(topmost_index, command=toggle_topmost)

    GUI.config(menu=menubar)

    # Активируем защиту в обычной среде
    if not RUN_IN_RECOVERY:
        GUI.attributes("-topmost", True)