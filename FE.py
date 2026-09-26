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
from tkinter import filedialog, messagebox, simpledialog
try:
    from OF import Logger
    logger = Logger()
except:
    from loguru import logger
import os

from languages import l
from AES import AES
from OF import apply_global_theme, create_menubar

FILE_EDITOR_VERSION = "0.4.3 Beta"

class FileEditor:
    def __init__(self, FE_GUI):
        self.FE_GUI = FE_GUI
        self.FE_GUI.title(l("FE"))
        self.FE_GUI.geometry("650x400")

        self.current_file = None
        self.is_modified = False

        # Переменные для стилей
        self.font_family = "Default"
        self.font_size = 12
        self.line_numbers_enabled = False

        # Список для хранения позиций совпадений
        self.matches_positions = []
        self.current_match_index = -1

        # Создаём меню
        create_menubar(self.FE_GUI, False, self.open_file, self.save_file, self.save_as_file, self.on_closing, self.change_font, self.change_font_size)

        # Создаём панель поиска
        self.create_search_panel()

        # Создаём строку состояния
        self.create_status_bar()

        # Создаём главный фрейм
        self.main_frame = tk.Frame(self.FE_GUI)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Создаём текстовое поле
        self.create_text_widget()

        # Создаём контекстное меню
        self.create_context_menu()

        # Привязываем сочетания клавиш
        self.bind_shortcuts()

        # Обработчик закрытия окна
        self.FE_GUI.protocol("WM_DELETE_WINDOW", self.on_closing)



    def create_context_menu(self):
        self.context_menu = tk.Menu(self.FE_GUI, tearoff=0)
        self.context_menu.add_command(label=l("cancel"), command=lambda: self.text_widget.edit_undo())
        self.context_menu.add_command(label=l("repeat"), command=lambda: self.text_widget.edit_redo())
        self.context_menu.add_separator()
        self.context_menu.add_command(label=l("cut"), command=self.cut_text)
        self.context_menu.add_command(label=l("copy"), command=self.copy_text)
        self.context_menu.add_command(label=l("paste"), command=self.paste_text)
        self.context_menu.add_separator()
        self.context_menu.add_command(label=l("select_all"), command=self.select_all)

        # Привязываем показ контекстного меню на ПКМ
        self.text_widget.bind("<Button-3>", self.show_context_menu)



    def show_context_menu(self, event):
        try:
            self.context_menu.tk_popup(
                event.x_root,
                event.y_root
            )
        finally:
            self.context_menu.grab_release()



    def bind_shortcuts(self):
        # Привязываем к текстовому полю вместо главного окна
        self.text_widget.bind("<Control-f>", lambda e: self.toggle_search_panel())
        self.text_widget.bind("<Control-o>", lambda e: self.open_file())
        self.text_widget.bind("<Control-s>", lambda e: self.save_file())
        self.text_widget.bind("<Control-Shift-s>", lambda e: self.save_as_file())
        self.text_widget.bind("<Control-z>", lambda e: self.text_widget.edit_undo())
        self.text_widget.bind("<Control-y>", lambda e: self.text_widget.edit_redo())
        self.text_widget.bind("<Control-x>", lambda e: self.cut_text())
        self.text_widget.bind("<Control-c>", lambda e: self.copy_text())
        self.text_widget.bind("<Control-v>", lambda e: self.paste_text())
        self.text_widget.bind("<Control-a>", lambda e: self.select_all())



    def change_font(self, font_name):
        self.font_family = font_name
        self.text_widget.config(font=(self.font_family, self.font_size))



    def change_font_size(self, size):
        self.font_size = size
        self.text_widget.config(font=(self.font_family, self.font_size))



    def create_text_widget(self):
        frame = tk.Frame(self.main_frame)
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Прокрутка
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Текстовое поле
        self.text_widget = tk.Text(
            frame,
            yscrollcommand=scrollbar.set,
            wrap=tk.WORD,
            font=(self.font_family, self.font_size),
            undo=True,
            maxundo=-1
        )
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.text_widget.yview)

        # Привязываем события для обновления позиции
        self.text_widget.bind("<KeyRelease>", lambda e: [
            self.on_text_change(e),
            self.update_cursor_position(e)
        ])
        self.text_widget.bind("<Button-1>", self.update_cursor_position)
        self.text_widget.bind("<Motion>", self.update_cursor_position)



    def update_cursor_position(self, event=None):
        """Обновляет отображение текущей позиции курсора"""
        pos = self.text_widget.index(tk.INSERT)
        line, col = pos.split(".")
        self.position_label.config(text=f"{l("line")}: {line}, {l("column")}: {col}")



    def create_status_bar(self):
        self.status_bar = tk.Frame(self.FE_GUI, height=20)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.status_bar.pack_propagate(False)

        # Левая часть (информация о файле)
        self.status_label = tk.Label(
            self.status_bar,
            text=l("new_file"),
            #bg="gray90",
            font=(self.font_family, 9)
        )
        self.status_label.pack(side=tk.LEFT, padx=5, pady=2)

        # Правая часть (позиция курсора)
        self.position_label = tk.Label(
            self.status_bar,
            text=f"{l("line")}: 1, {l("column")}: 1",
            #bg="gray90",
            font=(self.font_family, 9)
        )
        self.position_label.pack(side=tk.RIGHT, padx=5, pady=2)



    def update_status_bar(self):
        """Обновляет строку состояния"""
        modified_indicator = " *" if self.is_modified else ""
        self.status_label.config(text=f'{l("new_file")}{modified_indicator}')



    def on_text_change(self, event=None):
        if not self.is_modified:
            self.is_modified = True
            self.update_status_bar()
        # Обновляем поиск
        if self.search_active:
            self.perform_search()



    def open_file(self):
        file_path = filedialog.askopenfilename(
            parent=self.FE_GUI,
            title=l("select_file"),
            filetypes=[(l("text_file"), "*.txt"), ("MarkDown", "*.md"), ("JSON", "*.json"), (l("all_files"), "*.*")]
        )
        if file_path:
            self.load_file(file_path)



    def load_file(self, file_path):
        try:
            if not os.path.exists(file_path):
                messagebox.showerror(l("error"), f'{l("file")} {l("not_found")}: {file_path}', parent=self.FE_GUI)
                return

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            if messagebox.askyesno(l("open"), l("decrypt_file"), parent=self.FE_GUI):
                try:
                    CLYTH = simpledialog.askstring(l("open"), l("enter_clyth"), parent=self.FE_GUI)
                    content = AES(content, CLYTH, True)
                except:
                    pass

            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(1.0, content)

            self.current_file = file_path
            self.is_modified = False
            self.update_status_bar()
        except Exception as e:
            logger.exception(f'FE - {l("error")} {l("load_file")}')
            messagebox.showerror(l("error"), str(e), parent=self.FE_GUI)



    def save_file(self):
        if not self.current_file:
            self.save_as_file()
            return
        try:
            content = self.text_widget.get(1.0, tk.END)
            if messagebox.askyesno(l("save_file2"), l("encrypt_file"), parent=self.FE_GUI):
                try:
                    CLYTH = simpledialog.askstring(l("enter_clyth"), l("enter_clyth"), parent=self.FE_GUI)
                    content = AES(content, CLYTH)
                except:
                    pass
            with open(self.current_file, "w", encoding="utf-8") as file:
                file.write(content)
            self.is_modified = False
            self.update_status_bar()
            messagebox.showinfo(l("success_saved"), f'{l("file")} {l("success_saved")}!', parent=self.FE_GUI)
        except Exception as e:
            logger.exception(f'FE - {l("error")} {l("save_file")}: {self.current_file}', parent=self.FE_GUI)
            messagebox.showerror(l("error"), str(e))



    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(
            parent=self.FE_GUI,
            title=l("save_file2"),
            defaultextension=".txt",
            filetypes=[(l("text_file"), "*.txt"), ("MarkDown", "*.md"), ("JSON", "*.json"), (l("all_files"), "*.*")]
        )
        if file_path:
            try:
                content = self.text_widget.get(1.0, tk.END)
                if messagebox.askyesno(l("save_file2"), l("encrypt_file"), parent=self.FE_GUI):
                    try:
                        CLYTH = simpledialog.askstring(l("enter_clyth"), l("enter_clyth"), parent=self.FE_GUI)
                        content = AES(content, CLYTH)
                    except:
                        pass
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(content)
                self.current_file = file_path
                self.is_modified = False
                self.update_status_bar()
                messagebox.showinfo(l("success_saved"), f'{l("file")} {l("success_saved")}!', parent=self.FE_GUI)
            except Exception as e:
                logger.exception(f'FE - {l("error")} {l("save_file")}: {file_path}')
                messagebox.showerror(l("error"), str(e), parent=self.FE_GUI)



    def cut_text(self):
        try:
            self.text_widget.event_generate("<<Cut>>")
        except:
            pass



    def copy_text(self):
        try:
            self.text_widget.event_generate("<<Copy>>")
        except:
            pass



    def paste_text(self):
        try:
            self.text_widget.event_generate("<<Paste>>")
        except:
            pass



    def select_all(self):
        self.text_widget.tag_add(tk.SEL, "1.0", tk.END)
        self.text_widget.mark_set(tk.INSERT, "1.0")
        self.text_widget.see(tk.INSERT)
        return "break"



    def on_closing(self):
        if self.is_modified:
            response = messagebox.askyesnocancel(l("save_file2"), l("save_changes?"), parent=self.FE_GUI)
            if response is None: # Отмена
                return
            elif response: # Да
                self.save_file()
        self.FE_GUI.destroy()



    # Создаём панель поиска
    def create_search_panel(self):
        self.search_active = True
        self.search_panel = tk.Frame(self.FE_GUI, bd=1, relief=tk.RAISED)
        self.search_panel.pack(side=tk.TOP, fill=tk.X)
        # Текстовое поле поиска
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.search_panel, textvariable=self.search_var)
        self.search_entry.pack(side=tk.LEFT, padx=5, pady=2, fill=tk.X, expand=True)
        self.search_entry.bind("<KeyRelease>", lambda e: self.perform_search())

        # Чекбоксы
        self.case_var = tk.BooleanVar(value=True)
        self.word_var = tk.BooleanVar(value=False)

        self.case_check = tk.Checkbutton(self.search_panel, text=l("match_case"), variable=self.case_var, command=self.perform_search)
        self.word_check = tk.Checkbutton(self.search_panel, text=l("whole_words"), variable=self.word_var, command=self.perform_search)

        self.case_check.pack(side=tk.LEFT, padx=5)
        self.word_check.pack(side=tk.LEFT, padx=5)

        # Кнопки навигации
        self.prev_button = tk.Button(self.search_panel, text=l("back"), command=self.search_prev)
        self.next_button = tk.Button(self.search_panel, text=l("next"), command=self.search_next)
        self.prev_button.pack(side=tk.LEFT, padx=2)
        self.next_button.pack(side=tk.LEFT, padx=2)

        # Кнопка закрытия поиска
        self.close_search_button = tk.Button(self.search_panel, text="×", command=self.toggle_search_panel)
        self.close_search_button.pack(side=tk.RIGHT, padx=2)



    # Показываем или скрывает панель поиска
    def toggle_search_panel(self):
        if self.search_active:
            self.search_panel.pack_forget()
            self.search_active = False
            self.clear_search_highlight()
        else:
            self.search_panel.pack(side=tk.TOP, fill=tk.X, before=self.main_frame)
            self.search_active = True
            self.search_var.set("")
            self.matches_positions = []
            self.current_match_index = -1
            self.clear_search_highlight()



    # Выполняем поиск и выделяем совпадения
    def perform_search(self):
        self.clear_search_highlight()
        pattern = self.search_var.get()
        if not pattern:
            return
        content = self.text_widget.get("1.0", tk.END)
        flags = 0
        if not self.case_var.get():
            pattern = pattern.lower()
            content_cmp = content.lower()
        else:
            content_cmp = content

        self.matches_positions = []

        import re
        if self.word_var.get():
            regex = r"\b{}\b".format(re.escape(pattern))
        else:
            regex = re.escape(pattern)

        for match in re.finditer(regex, content_cmp):
            start_idx = match.start()
            end_idx = match.end()
            start = self.text_widget.index(f"1.0+{start_idx}c")
            end = self.text_widget.index(f"1.0+{end_idx}c")
            self.matches_positions.append((start, end))

        # Выделяем все совпадения одним цветом
        self.text_widget.tag_remove("search_highlight", "1.0", tk.END)
        for start, end in self.matches_positions:
            self.text_widget.tag_add("search_highlight", start, end)
        self.text_widget.tag_config("search_highlight", foreground="blue", background="yellow")

        # Выделяем текущее совпадение другим цветом
        self.text_widget.tag_remove("current_match", "1.0", tk.END)
        if self.matches_positions:
            self.current_match_index = 0
            start, end = self.matches_positions[self.current_match_index]
            self.text_widget.tag_add("current_match", start, end)
            self.text_widget.tag_config("current_match", foreground="white", background="red")

            self.focus_match(self.current_match_index)



    # Перемещаем курсор к совпадению по индексу и выделяем его цветом
    def focus_match(self, index):
        if not self.matches_positions:
            return
        if index < 0 or index >= len(self.matches_positions):
            return
        start, end = self.matches_positions[index]
        # Убираем выделение текущего совпадения
        self.text_widget.tag_remove("current_match", "1.0", tk.END)
        self.text_widget.tag_remove(tk.SEL, "1.0", tk.END)
        self.text_widget.tag_add("current_match", start, end)
        self.text_widget.see(start)
        self.text_widget.mark_set(tk.INSERT, start)
        # Выделяем текущее совпадение
        self.text_widget.tag_add(tk.SEL, start, end)



    # Переходим к следующему совпадению
    def search_next(self):
        if not self.matches_positions:
            return
        self.current_match_index = (self.current_match_index + 1) % len(self.matches_positions)
        self.focus_match(self.current_match_index)



    # Переходим к предыдущему совпадению
    def search_prev(self):
        if not self.matches_positions:
            return
        self.current_match_index = (self.current_match_index - 1) % len(self.matches_positions)
        self.focus_match(self.current_match_index)



    # Удаляем выделение от поиска
    def clear_search_highlight(self):
        self.text_widget.tag_remove("search_highlight", "1.0", tk.END)



def FE(file_path=None, current_theme=False):
    try:
        if not current_theme:
            from config import THEME, DEFAULT_THEME
            current_theme = THEME[DEFAULT_THEME]
        FE_GUI = tk.Tk()
        apply_global_theme(FE_GUI, current_theme)
        editor = FileEditor(FE_GUI)
        if file_path:
            editor.load_file(file_path)
        FE_GUI.mainloop()
    except:
        logger.exception(l("fe_critical_error"))

if __name__ == "__main__":
    FE()
