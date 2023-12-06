import os
import shutil
from pathlib import Path


class Functionality:
    def __init__(self,
                 main_base_path, projectname, app_lists, main_project_path, function_names, main_app_path, last_name):
        base_path = Path(__file__).parent
        self.base_path = base_path
        self.main_base_path = main_base_path
        self.project_path = base_path / Path("project")
        self.app_path = base_path / Path("app")
        self.project_name = projectname
        self.app_list = app_lists
        self.main_project_path = main_project_path
        self.main_app_path = main_app_path
        self.function_names = function_names
        self.last_name = last_name

        self.get_project_views()
        self.get_project_urls()
        self.get_app_views()
        self.get_app_urls()
        self.get_models()
        self.get_templates()
        self.get_settings()

    def get_project_views(self):
        file_path = self.main_project_path / Path("views.py")
        if os.path.exists(file_path):
            os.remove(file_path)
        shutil.copy(f'{self.project_path / Path("views.py")}', f'{self.main_project_path}')

    def get_project_urls(self):
        data = open(self.project_path / Path("urls.txt"), "r").read()
        text = ''
        if len(self.app_list) == 0:
            self.app_list = ['User']
        for i in range(len(self.app_list)):
            if i == len(self.app_list) - 1:
                text += f'\tpath("{self.app_list[i].lower()}/", include("{self.app_list[i]}.urls")),'
            else:
                text += f'\tpath("{self.app_list[i].lower()}/", include("{self.app_list[i]}.urls")),\n'

        data = data.replace('replace_this_line', text)

        file_path = Path("urls.py")
        open(file_path, "w").write(data)

        if os.path.exists(self.main_project_path / Path("urls.py")):
            os.remove(self.main_project_path / Path("urls.py"))
        shutil.move(f'{file_path}', f'{self.main_project_path}')

    def get_app_views(self):
        data = open(self.app_path / Path("views.txt"), "r").read()
        function_names = self.function_names
        for i in function_names:
            text = ''
            if i['status'] == 'True':
                text = open(self.app_path / Path(f"{i['name']}.txt"), "r").read()

            data = data.replace(f"replace_{i['name']}", text)

        file_path = Path("views.py")
        open(file_path, "w").write(data)

        if os.path.exists(self.main_app_path / Path("views.py")):
            os.remove(self.main_app_path / Path("views.py"))
        shutil.move(f'{file_path}', f'{self.main_app_path}')

    def get_app_urls(self):
        data = open(self.app_path / Path("urls.txt"), "r").read()
        function_names = self.function_names
        text = ''
        for i in range(len(function_names)):
            if function_names[i]['status'] == 'True':
                if function_names[i]["name"].lower() == 'register':
                    text += f'\tpath("{function_names[i]["name"].lower()}/", ' \
                            f'{function_names[i]["name"].lower()}, name="{function_names[i]["name"].lower()}"),\n'
                    text += f'\tpath("token/", token_send, name="token"),\n'
                    text += f'\tpath("verify/<str:auth_token>/", verify, name="verify"),\n'
                    continue
                if function_names[i]["name"].lower() == 'home':
                    continue
                if i == len(function_names) - 1:
                    text += f'\tpath("{function_names[i]["name"].lower()}/", ' \
                            f'{function_names[i]["name"].lower()}, name="{function_names[i]["name"].lower()}"),'
                else:
                    text += f'\tpath("{function_names[i]["name"].lower()}/", ' \
                            f'{function_names[i]["name"].lower()}, name="{function_names[i]["name"].lower()}"),\n'

        data = data.replace('replace_path', text)

        file_path = Path("urls.py")
        open(file_path, "w").write(data)

        if os.path.exists(self.main_app_path / Path("urls.py")):
            os.remove(self.main_app_path / Path("urls.py"))
        shutil.move(f'{file_path}', f'{self.main_app_path}')

    def get_models(self):
        file_path = self.base_path / Path("models.py")

        if os.path.exists(self.last_name / Path("models.py")):
            os.remove(self.last_name / Path("models.py"))
        shutil.copy(f'{file_path}', f'{self.last_name}')

    def get_templates(self):
        file_path = self.base_path / Path("tem")
        folder_path = self.base_path / Path("templates")
        static_path = self.base_path / Path("static")
        function_names = self.function_names
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        shutil.copy(f'{file_path}' / Path("index.html"), f'{folder_path}')
        shutil.copy(f'{file_path}' / Path("404.html"), f'{folder_path}')

        for i in function_names:
            if i['status'] == 'True':
                if i['name'].lower() == 'register':
                    shutil.copy(f'{file_path}' / Path(f"{i['name'].lower()}.html"), f'{folder_path}')
                    shutil.copy(f'{file_path}' / Path(f"token.html"), f'{folder_path}')
                    continue

                if i['name'].lower() == 'logout':
                    continue

                shutil.copy(f'{file_path}' / Path(f"{i['name'].lower()}.html"), f'{folder_path}')

        if os.path.exists(self.main_base_path / Path("templates")):
            os.remove(self.main_base_path / Path("templates"))

        shutil.move(f'{folder_path}', f'{self.main_base_path}')

        if os.path.exists(self.main_base_path / Path("static")):
            os.remove(self.main_base_path / Path("static"))

        shutil.copytree(f'{static_path}', f'{self.main_base_path}\\static')

    def get_settings(self):
        project_names = self.project_name
        app_lists = self.app_list

        text = f"'{project_names}',\n"

        if len(app_lists) == 0:
            app_lists = ['User']
        for i in range(len(app_lists)):
            if i == len(app_lists) - 1:
                text += f"\t'{app_lists[i]}',"
            else:
                text += f"\t'{app_lists[i]}',\n"

        text = f"{text}\n\t'django.contrib.admin',"

        main_project_path = self.main_project_path / Path("settings.py")
        data = open(main_project_path, "r").read()

        static_text = 'STATIC_URL = "static/"\nSTATICFILES_DIRS = [\n\tBASE_DIR / "static",\n]'

        data = data \
            .replace("DIRS': []", f"DIRS': ['templates']") \
            .replace("'django.contrib.admin',", text) \
            .replace('ALLOWED_HOSTS = []', "ALLOWED_HOSTS = ['*']") \
            .replace("STATIC_URL = 'static/'", static_text)

        file_path = Path("settings.py")
        open(file_path, "w").write(data)

        if os.path.exists(main_project_path):
            os.remove(main_project_path)

        shutil.move(f'{file_path}', f'{self.main_project_path}')


if __name__ == '__main__':
    project_name = 'music_club'
    app_list = ['App1', 'App2', 'App3']
    Functionality(
        projectname=project_name,
        app_lists=app_list,
        main_project_path='C:\\prathmesh\\update_project\\git\\soniprathmesh-30-10\\'
                          'projects\\main\\final_project\\music_club\\music_club',
        main_app_path='C:\\prathmesh\\update_project\\git\\soniprathmesh-30-10\\'
                      'projects\\main\\final_project\\music_club\\User',
        function_names=[
            {'name': 'login', 'status': False},
            {'name': 'register', 'status': False},
            {'name': 'logout', 'status': False},
            {'name': 'profile', 'status': False},
            {'name': 'client_ip', 'status': False},
            {'name': 'home', 'status': True},
        ],
        last_name='C:\\prathmesh\\update_project\\git\\soniprathmesh-30-10\\'
                  'projects\\main\\final_project\\music_club\\User',
        main_base_path='C:\\prathmesh\\update_project\\git\\soniprathmesh-30-10\\'
                       'projects\\main\\final_project\\music_club'
    )
