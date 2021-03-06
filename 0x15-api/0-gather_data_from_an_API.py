#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
   returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    """return name, tasks and name_tasks"""

    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    response1 = requests.get(url)

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
    response2 = requests.get(url)
    task = 0
    total_task = 0
    if response2.status_code == 200 & response1.status_code == 200:
        employee = response1.json()['name']
        for i in response2.json():
            if i['completed'] is True:
                task += 1
            total_task += 1
        print("Employee {} is done with tasks({}/{}):".format(
            employee, task, total_task))

        for i in response2.json():
            if i['completed'] is True:
                print("\t {}".format(i['title']))
