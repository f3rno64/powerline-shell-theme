from powerline_shell.themes.washed import DefaultColor


class Color(DefaultColor):
    HOME_SPECIAL_DISPLAY = True

    USERNAME_FG = 34
    USERNAME_BG = 17
    USERNAME_ROOT_BG = 124

    HOSTNAME_FG = 255
    HOSTNAME_BG = 89

    PATH_BG = 53
    PATH_FG = 255
    CWD_FG = 255
    SEPARATOR_FG = 232

    READONLY_BG = 209
    READONLY_FG = 15

    REPO_CLEAN_BG = 22
    REPO_CLEAN_FG = 235
    REPO_DIRTY_BG = 52
    REPO_DIRTY_FG = 231

    JOBS_FG = 255
    JOBS_BG = 8

    CMD_PASSED_BG = 64
    CMD_PASSED_FG = 255
    CMD_FAILED_BG = 52
    CMD_FAILED_FG = 255

    TIME_FG = 34
    TIME_BG = 16

    BATTERY_LOW_BG = 124
    BATTERY_LOW_FG = 231

    BATTERY_NORMAL_BG = 238
    BATTERY_NORMAL_FG = 255
