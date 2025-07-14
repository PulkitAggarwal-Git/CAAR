import requests
import json
from collections import Counter

def fetch_submissions_data(handle):
    url = f"https://codeforces.com/api/user.status?handle={handle}"
    response = requests.get(url)
    data = response.json()
    return data

def fetch_user_data(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(url)
    data = response.json()
    return data

def get_tags_and_solved_problems(data):
    
    tag_counter = Counter()
    seen_problems = set()
    solved_problems = []

    if data.get("status") == "OK":
        for submission in data["result"]:
            
            problem_id = (submission["problem"]["contestId"], submission["problem"]["index"])

            if submission["verdict"] != "OK" and problem_id not in seen_problems:
                tag_counter.update(submission["problem"]["tags"])
                seen_problems.add(problem_id)  

            if submission["verdict"] == "OK":
                solved_problems.append(problem_id)
    return tag_counter, solved_problems, len(data["result"]), len(solved_problems)

def analyze_user_problems(data):
    tried_but_unsolved = []
    solved_after_attempts = []

    if data.get("status") == "OK":
        problem_stats = {}

        for entry in data["result"]:
            problem_id = (entry["problem"]["contestId"], entry["problem"]["index"])
            problem_name = entry["problem"]["name"]

            if problem_id not in problem_stats:
                problem_stats[problem_id] = {"attempts": 0, "solved": False, "name": ""}
                problem_stats[problem_id]["name"] = problem_name

            problem_stats[problem_id]["attempts"] += 1
            if entry["verdict"] == "OK":
                problem_stats[problem_id]["solved"] = True

        for problem_id, stats in problem_stats.items():
            problem_name = stats["name"]
            
            if stats["attempts"] > 0 and not stats["solved"]:
                tried_but_unsolved.append((problem_name,f"https://codeforces.com/problemset/problem/{problem_id[0]}/{problem_id[1]}"))
            
            elif stats["solved"] and stats["attempts"] > 3:
                solved_after_attempts.append((problem_name,f"https://codeforces.com/problemset/problem/{problem_id[0]}/{problem_id[1]}"))

    return tried_but_unsolved, solved_after_attempts