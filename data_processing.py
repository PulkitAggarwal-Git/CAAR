import requests
import json
from collections import Counter
from database import db, User, SolvedProblems

def fetch_submissions_data(handle):
    url = f"https://codeforces.com/api/user.status?handle={handle}"
    try:
        response = requests.get(url)
        if response.status_code!=200:
            return None
        
        data = response.json()
        return data
    
    except requests.exceptions.RequestException:
        return None

def fetch_user_data(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    try:
        response = requests.get(url)
        if response.status_code!=200:
            return None
        
        data = response.json()
        return data
    
    except requests.exceptions.RequestException:
        return None

def get_tags_and_solved_problems(data):
    
    tag_counter = Counter()
    seen_problems = set()
    solved_problems = []

    if data.get("status") == "OK":
        for submission in data["result"]:
            
            problem_id = (submission["problem"]["contestId"], submission["problem"]["index"])
            if "verdict" in submission:
                if submission["verdict"] != "OK" and problem_id not in seen_problems:
                    tag_counter.update(submission["problem"]["tags"])
                    seen_problems.add(problem_id)  

                if submission["verdict"] == "OK":
                    solved_problems.append(problem_id)
    return tag_counter, solved_problems, len(data["result"]), len(solved_problems)

def analyze_user_problems(data):
    # tried_but_unsolved = []
    # solved_after_attempts = []
    unsolved_problems = []

    if data.get("status") == "OK":
        problem_stats = {}

        for entry in data["result"]:
            problem_id = (entry["problem"]["contestId"], entry["problem"]["index"])
            problem_name = entry["problem"]["name"]

            if problem_id not in problem_stats:
                problem_stats[problem_id] = {"attempts": 0, "solved": False, "name": ""}
                problem_stats[problem_id]["name"] = problem_name

            problem_stats[problem_id]["attempts"] += 1
            
            if "verdict" in entry:
                if entry["verdict"] == "OK":
                    problem_stats[problem_id]["solved"] = True

        for problem_id, stats in problem_stats.items():
            problem_name = stats["name"]
            
            if stats["attempts"] > 0 and not stats["solved"]:
                unsolved_problems.append((problem_name,f"https://codeforces.com/problemset/problem/{problem_id[0]}/{problem_id[1]}"))
            
            elif stats["solved"] and stats["attempts"] > 3:
                unsolved_problems.append((problem_name,f"https://codeforces.com/problemset/problem/{problem_id[0]}/{problem_id[1]}"))

    return unsolved_problems

def store_solved_problems(handle, solved_problems):
    user = User.query.filter_by(username=handle).first()

    if not user:
        user = User(username=handle)
        db.session.add(user)
        db.session.commit()

    for contest_id, index in solved_problems:
            problem_id = f"{contest_id}-{index}"
            existing = SolvedProblems.query.filter_by(user_id=user.id, problem_id=problem_id).first()
            
            if not existing:
                submission = SolvedProblems(user_id=user.id, problem_id=problem_id)
                db.session.add(submission)
    
    db.session.commit()

def get_solved_problems(handle):
    user = User.query.filter_by(username=handle).first()
    solved = SolvedProblems.query.filter_by(user_id=user.id).all()

    solved_problems = []

    for problem in solved:
        try:
            contestId, index = problem.problem_id.split("-")
            solved_problems.append((int(contestId), index))
        except ValueError:
            continue

    return solved_problems