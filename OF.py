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
from tkinter import ttk, Menu
import tkinter as tk
from languages import l
from config import THEME

OTHER_FUNCTION_VERSION = "0.14.9 Beta"

def apply_global_theme(window, current_theme):
    """
    Функция для применения темы к окну tkinter
    window - окно tkinter
    current_theme - Текущая тема для интерфейса (не сам кортеж, а название кортежа)
    return - функция ничего не возвращает!
    """
    style = ttk.Style()
    style.theme_use("clam")

    # Настройка стандартных tk-виджетов (включая верхнюю панель/меню)
    window.option_add("*Background", current_theme["bg"])
    window.option_add("*Foreground", current_theme["fg"])
    window.option_add("*Menu.activeBackground", current_theme["abg"])
    window.option_add("*Menu.activeForeground", current_theme["afg"])

    # Стилизация текстовых полей (tk.Text)
    window.option_add("*Text.Background", current_theme["bg"])
    window.option_add("*Text.Foreground", current_theme["fg"])
    window.option_add("*Text.InsertBackground", current_theme["fg"])
    window.option_add("*Text.SelectBackground", current_theme["abg"])
    window.option_add("*Text.SelectForeground", current_theme["afg"])

    # Стилизация чекбоксов (tk.Checkbutton)
    window.option_add("*Checkbutton.Background", current_theme["bg"])
    window.option_add("*Checkbutton.Foreground", current_theme["fg"])
    window.option_add("*Checkbutton.activeBackground", current_theme["abg"])
    window.option_add("*Checkbutton.activeForeground", current_theme["afg"])
    window.option_add("*Checkbutton.selectColor", current_theme["abg"])

    # Стилизация обычных кнопок (tk.Button)
    window.option_add("*Button.Background", current_theme["bbg"])
    window.option_add("*Button.Foreground", current_theme["bfg"])
    window.option_add("*Button.activeBackground", current_theme["abg"])
    window.option_add("*Button.activeForeground", current_theme["afg"])

    # Настройка базового стиля для всех ttk виджетов
    style.configure(".",
                    background=current_theme["bg"],
                    foreground=current_theme["fg"],
                    fieldbackground=current_theme["bg"],
                    bordercolor=current_theme["bbg"],
                    lightcolor=current_theme["bg"],
                    darkcolor=current_theme["bg"])

    # Таблицы
    style.configure("Treeview",
                    background=current_theme["bg"],
                    foreground=current_theme["fg"],
                    fieldbackground=current_theme["bg"],
                    rowheight=25)

    style.map("Treeview",
              background=[("selected", current_theme["abg"])],
              foreground=[("selected", current_theme["afg"])])

    style.configure("Treeview.Heading",
                    background=current_theme["bbg"],
                    foreground=current_theme["fg"],
                    relief="flat",
                    font=("default", 10, "bold"))

    style.map("Treeview.Heading",
              background=[("active", current_theme["abg"]), ("pressed", current_theme["abg"])],
              foreground=[("active", current_theme["afg"])])

    # Чекбоксы
    style.configure("TCheckbutton",
                    background=current_theme["bg"],
                    foreground=current_theme["fg"])

    style.map("TCheckbutton",
              background=[("active", current_theme["bg"])],
              foreground=[("active", current_theme["abg"])],
              indicatorcolor=[("selected", current_theme["abg"]), ("active", current_theme["bg"])])

    # Кнопки
    style.configure("TButton",
                    background=current_theme["bbg"],
                    foreground=current_theme["bfg"])
    style.map("TButton",
              background=[("active", current_theme["abg"])],
              foreground=[("active", current_theme["afg"])])

    # Поля ввода
    style.configure("TEntry",
                    fieldbackground=current_theme["bg"],
                    foreground=current_theme["fg"],
                    bordercolor=current_theme["bbg"])

    # Вкладки
    style.configure("TNotebook", background=current_theme["bg"], borderwidth=0)
    style.configure("TNotebook.Tab",
                    background=current_theme["bbg"],
                    foreground=current_theme["bfg"],
                    padding=[10, 2])
    style.map("TNotebook.Tab",
              background=[("selected", current_theme["abg"])],
              foreground=[("selected", current_theme["afg"])])

    # Фон самого главного окна
    window.configure(bg=current_theme["bg"])



def restart_gui_for_theme(GUI, user_theme):
    #global current_theme
    current_theme = THEME[user_theme]
    apply_global_theme(GUI, current_theme)



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
    for label, theme_name in themes:
        theme_menu.add_checkbutton(label=l(label), command=lambda tn=theme_name: restart_gui_for_theme(GUI, tn))
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