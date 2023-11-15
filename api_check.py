import requests
from pprint import pprint


endpoint_projects = "https://api.weeek.net/public/v1/tm/projects"
endpoint_boards = "https://api.weeek.net/public/v1/tm/boards"
endpoint_tasks = "https://api.weeek.net/public/v1/tm/tasks"


def get_tasks():
    headers = {"Authorization": "Bearer 8c49ff6d-a1c7-4935-9d66-9f3b6a178aaa"}
    params = {
        "projectId": 6,
        "boardId": 27,
        "isCompleted": False,
    }

    task_num = "/660"
    tasks = requests.get(endpoint_tasks, headers=headers,
                         params=params).json().get('tasks')
    tasks_info = requests.get(endpoint_tasks + task_num, headers=headers,
                              params=params).json()
    pprint(tasks)
    pprint(len(tasks))
    return tasks


if __name__ == "__main__":

    get_tasks()
