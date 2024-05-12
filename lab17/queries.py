# Получаем все проекты и выводим их названия и описания.
# Получаем всех менеджеров и выводим их имена и электронные адреса.
# Получаем всех разработчиков и выводим их имена, электронные адреса и команды, в которых они работают.
# Получаем все команды и выводим их названия, а также имена разработчиков, работающих в этих командах.
# Получаем проекты вместе с их менеджерами и выводим названия проектов и имена менеджеров.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Base, Project, Manager, Developer, Team

engine = create_engine('sqlite:///sqlalchemy_example.db')
Session = sessionmaker(bind=engine)
session = Session()

# Получить все проекты
def project_id():
    projects = session.query(Project).all()
    for project in projects:
        print(f"Project: {project.name} - {project.description}")

# Получить всех менеджеров
def managers_id():
    managers = session.query(Manager).all()
    for manager in managers:
        print(f"Manager: {manager.name} - {manager.email}")

# Получить всех разработчиков
def developers_id():
    developers = session.query(Developer).all()
    for developer in developers:
        print(f"Developer: {developer.name} - {developer.email} - Team: {developer.team.name}")

# Получить все команды
def teams_id():
    teams = session.query(Team).all()
    for team in teams:
        print(f"Team: {team.name}")
        for developer in team.developers:
            print(f"  Developer: {developer.name}")

# Получить проекты с менеджерами
def projects_managers():
    projects_with_managers = session.query(Project, Manager).join(Manager).all()
    for project, manager in projects_with_managers:
        print(f"Project: {project.name} - Manager: {manager.name}")


print("Введите цифру:")
print("1. Получить все проекты")
print("2. Получить всех менеджеров")
print("3. Получить всех разработчиков")
print("4. Получить все команды")
print("5. Получить проекты с менеджерами")
while True:
    try:
        button_user = int(input("Введите значение кнопки (1, 2, 3, 4, 5): "))
        if button_user == 1:
            project_id()
        elif button_user == 2:
            managers_id()
        elif button_user == 3:
            developers_id()
        elif button_user == 4:
            teams_id()
        elif button_user == 5:
            projects_managers()
        else:
            print("Некорректное значение, введите 1, 2, 3, 4, 5")
    except ValueError:
        print("Ожидается число. Попробуйте еще раз.")