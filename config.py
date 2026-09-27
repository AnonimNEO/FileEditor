# Текущий язык (доступные языки: ru, en, ua)
CURRENT_LOCALIZATION = "ru"

# Контрастная тема
BLACK_THEME = {"bg": "black", "fg": "white", "bbg": "darkblue", "bfg": "white", "abg": "blue", "afg": "white", "lbg":  "black", "lfg": "white", "stb": "#090909", "tbg": "darkblue", "tfg": "white"}

# Тёмная тема
DARK_THEME = {"bg": "#1e1f22", "fg": "white", "bbg": "#243048", "bfg": "white", "abg": "#548af7", "afg": "white", "lbg":  "#1e1f22", "lfg": "white", "stb": "#1e1f22", "tbg": "#243048", "tfg": "white"}

# Светлая тема
WHITE_THEME = {"bg": "white", "fg": "black", "bbg": "white", "bfg": "black", "abg": "gray", "afg": "black", "lbg":  "white", "lfg": "black", "stb": "gray", "tbg": "white", "tfg": "black"}

# Красная тема
RED_THEME = {"bg": "black", "fg": "white", "bbg": "darkred", "bfg": "white", "abg": "red", "afg": "black", "lbg":  "black", "lfg": "white", "stb": "red", "tbg": "darkred", "tfg": "white"}

# Серая тема
GRAY_THEME =  {"bg": "gray", "fg": "white", "bbg": "gray", "bfg": "white", "abg": "white", "afg": "black", "lbg":  "gray", "lfg": "white", "stb": "gray", "tbg": "black", "tfg": "white"}

# Оранжевая тема
ORANGE_THEME =  {"bg": "gray", "fg": "white", "bbg": "darkorange", "bfg": "white", "abg": "orange", "afg": "black", "lbg":  "gray", "lfg": "darkorange", "stb": "gray", "tbg": "darkorange", "tfg": "black"}

# Зелёная тема
LIME_THEME =  {"bg": "green", "fg": "white", "bbg": "green", "bfg": "white", "abg": "lime", "afg": "black", "lbg":  "green", "lfg": "lime", "stb": "green", "tbg": "lime", "tfg": "black"}

# Кортеж тем
THEME = {
    "dark": {
        "bg": "#1e1e1e",
        "fg": "#ffffff",
        "bbg": "#0d47a1",  # button background
        "bfg": "#ffffff",  # button foreground
        "abg": "#0d47a1",  # active background
        "afg": "#ffffff",  # active foreground
    },
    "white": {
        "bg": "#ffffff",
        "fg": "#000000",
        "bbg": "#e0e0e0",
        "bfg": "#000000",
        "abg": "#d0d0d0",
        "afg": "#000000",
    },
    "red": {
        "bg": "#2b0000",
        "fg": "#ff4444",
        "bbg": "#b71c1c",
        "bfg": "#ffffff",
        "abg": "#c41c00",
        "afg": "#ffffff",
    },
    "lime": {
        "bg": "#001a00",
        "fg": "#00ff00",
        "bbg": "#2e7d32",
        "bfg": "#ffffff",
        "abg": "#388e3c",
        "afg": "#ffffff",
    },
    "black": {
        "bg": "#000000",
        "fg": "#ffffff",
        "bbg": "#333333",
        "bfg": "#ffffff",
        "abg": "#555555",
        "afg": "#ffffff",
    },
    "gray": {
        "bg": "#424242",
        "fg": "#e0e0e0",
        "bbg": "#616161",
        "bfg": "#ffffff",
        "abg": "#757575",
        "afg": "#ffffff",
    },
    "orange": {
        "bg": "#331a00",
        "fg": "#ffb366",
        "bbg": "#e65100",
        "bfg": "#ffffff",
        "abg": "#ff6d00",
        "afg": "#ffffff",
    },
}

# Тема по умолчанию
DEFAULT_THEME = "dark"