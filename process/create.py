import os
import shlex
import shutil
import subprocess
from pathlib import Path


class CreateProject:
    def __init__(self, project_name, app_list):
        self.project_name = project_name
        self.app_list = app_list
        self.base_path_server_1 = Path(__file__).parent
        if project_name:
            self.create_project()

    def get_base_path(self):
        return self.base_path_server_1.parent

    def create_project(self):
        base_path = self.base_path_server_1
        startproject_name = self.project_name.replace(' ', '_').replace('-', '_').replace('.', '_')
        startproject_cmd = f"django-admin startproject {startproject_name}"
        subprocess.Popen(shlex.split(startproject_cmd), shell=True).wait()

        if not self.app_list:
            self.app_list = ['User']

        for startapp_name in self.app_list:
            startapp_name = startapp_name.strip().replace(' ', '_').replace('-', '_').replace('.', '_')
            if len(self.app_list) == 1 and startapp_name == '':
                startapp_name = 'User'
            startapp_cmd = f"django-admin startapp {startapp_name}"
            subprocess.Popen(shlex.split(startapp_cmd), shell=True).wait()
            shutil.move(f'{base_path.parent}\\{startapp_name}', f'{base_path.parent}\\{startproject_name}')

        project_path = str(base_path.parent / Path("final_project/"))
        if not os.path.exists(project_path):
            os.makedirs(project_path)

        shutil.move(f'{base_path.parent}\\{startproject_name}', f'{project_path}')
