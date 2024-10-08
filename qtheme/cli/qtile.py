from os import path, listdir
from qtheme.utils.colors import green, red, blue, magenta
import subprocess
import json


class Qtile:
    def __init__(self, user_path) -> None:
        self.user_path = user_path

    def menu_themes(self):
        full_path = path.join(self.user_path, '.config', 'qtile', 'themes', 'theme_selector.json')
        qtile_themes_path = path.join(self.user_path, '.config', 'qtile', 'themes')
        kitty_themes_path = path.join(self.user_path, '.config', 'kitty', 'themes')

        qtile_index = 0
        kitty_index = 0

        with open(full_path, 'r') as file:
            cur_theme = json.load(file)

        magenta('Available Qtile themes: ')
        for theme in listdir(qtile_themes_path):
            if theme == 'theme_selector.json':
                continue
            qtile_index += 1
            theme_name = theme.split('.')[0]
            maker = lambda text : f'\033[34m{text}*\033[0m' if theme_name == cur_theme.get('theme') else text
            blue(f'[{qtile_index}] -> {maker(theme_name)}')
        print('')

        magenta('Available Kitty themes: ')
        for theme in listdir(kitty_themes_path):
            kitty_index += 1
            theme_name = theme.split('.')[0]
            blue(f'[{kitty_index}] -> {theme_name}')

    def set_bar_position(self, position: str = None):
        try:
            full_path = path.join(self.user_path, '.config', 'qtile', 'themes', 'theme_selector.json')

            if position is None:
                return

            if position not in {'top', 't', 'bottom', 'b'}:
                raise ValueError('The position is not correct')

            with open(full_path, 'r+') as file:
                data = json.load(file)
                data['position'] = 'bottom' if position in {'b', 'bottom'} else 'top' 
                file.seek(0)
                json.dump(data, file, indent=2, sort_keys=True)
                file.truncate()

            subprocess.run(['qtile', 'cmd-obj', '-o', 'cmd', '-f', 'reload_config'], check=True)
            green(f'Bar position changed correctly to {"bottom" if position in {"b", "bottom"} else "top" }')

        except ValueError as e:
            red(f'Error: {e}')
        except subprocess.CalledProcessError as e:
            red(f'Failed to reload Qtile configuration: {e}')
        except Exception as e:
            red(f'Unexpected error: {e}')

    def set_qtile_theme(self, theme: str = None):
        try:
            full_path = path.join(self.user_path, '.config', 'qtile', 'themes', 'theme_selector.json')
            qtile_theme_path = path.join(self.user_path, '.config', 'qtile', 'themes')

            if theme is None:
                return

            if not path.exists(path.join(qtile_theme_path, theme + '.json')):
                raise FileNotFoundError(f'The file "{theme}.json" does not exist')

            with open(full_path, 'r+') as file:
                data = json.load(file)
                data['theme'] = theme
                file.seek(0)
                json.dump(data, file, indent=2, sort_keys=True)
                file.truncate()

            subprocess.run(['qtile', 'cmd-obj', '-o', 'cmd', '-f', 'reload_config'], check=True)
            green(f'Theme changed correctly to "{theme}"')

        except (ValueError, FileNotFoundError) as e:
            red(f'Error: {e}')
        except subprocess.CalledProcessError as e:
            red(f'Failed to reload Qtile configuration: {e}')
        except Exception as e:
            red(f'Unexpected error: {e}')
