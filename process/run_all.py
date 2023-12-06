from .all_functions.get_files import Functionality
from .create import CreateProject, Path


def call_process(data):
    path = call_runserver(data)
    call_file(data, path)

    print(f'File Location: {path}\\{Path("final_project/")}')
    print(f'Project Name: {data["project_name"]}')
    print('Successfully Generated')


def call_runserver(data):
    project_name = data['project_name']
    app_name = data['app_name']
    app_list = app_name.split(',')

    path = CreateProject(
        project_name=project_name,
        app_list=app_list
    ).get_base_path()

    return path


def call_file(data, path):
    project_name = data['project_name']
    app_name = data['app_name']
    login = data['login']
    register = data['register']
    logout = data['logout']
    profile = data['profile']
    client_ip = data['client_ip']
    last_name = data['last_name']

    function_names = [
        {'name': 'login', 'status': login},
        {'name': 'register', 'status': register},
        {'name': 'logout', 'status': logout},
        {'name': 'profile', 'status': profile},
        {'name': 'client_ip', 'status': client_ip},
        {'name': 'home', 'status': 'True'},
    ]

    app_list = app_name.split(',')
    if len(app_list) == 1 and app_list[0] == '':
        app_list = ['User']

    Functionality(
        projectname=project_name,
        app_lists=app_list,
        main_project_path=f'{path}\\final_project\\{project_name}\\{project_name}',
        main_app_path=f'{path}\\final_project\\{project_name}\\{last_name}',
        function_names=function_names,
        last_name=f'{path}\\final_project\\{project_name}\\{last_name}',
        main_base_path=f'{path}\\final_project\\{project_name}'
    )
