from flask import session
import requests
import json
from data_processing import get_solved_problems

def fetch_data(tag, rating, taken_problems, solved_problems, max_len):
    url = f"https://codeforces.com/api/problemset.problems?tags={tag}"
    response = requests.get(url)
    data = response.json()

    problems = []

    if data["status"]  == "OK":
        for problem in data["result"]["problems"]:
            problem_name = problem["name"]
            problem_id = (problem["contestId"], problem["index"])

            if rating < 800:
                if "rating" in problem:
                    if problem["rating"] <= 900:
                        taken_problems.add(problem_id)
                        problems.append((problem_name, f"https://codeforces.com/problemset/problem/{problem_id[0]}/{problem_id[1]}"))

                        if len(problems)==max_len:
                            break

            elif rating <= 1600:
                if "rating" in problem:
                    if (rating - 100) <= problem["rating"] <= (rating + 200) and problem_id not in taken_problems and problem_id not in solved_problems:
                        taken_problems.add(problem_id)
                        problems.append((problem_name, f"https://codeforces.com/problemset/problem/{problem_id[0]}/{problem_id[1]}"))

                        if len(problems)==max_len:
                            break

            elif rating <= 2000:
                if "rating" in problem:
                    if (rating - 100) <= problem["rating"] <= (rating + 300) and problem_id not in taken_problems and problem_id not in solved_problems:
                        taken_problems.add(problem_id)
                        problems.append((problem_name, f"https://codeforces.com/problemset/problem/{problem_id[0]}/{problem_id[1]}"))

                        if len(problems)==max_len:
                            break

            elif rating <= 2500:
                if "rating" in problem:
                    if (rating - 100) <= problem["rating"] <= (rating + 400) and problem_id not in taken_problems and problem_id not in solved_problems:
                        taken_problems.add(problem_id)
                        problems.append((problem_name, f"https://codeforces.com/problemset/problem/{problem_id[0]}/{problem_id[1]}"))

                        if len(problems)==max_len:
                            break
            
            else:
                if "rating" in problem:
                    if (rating - 100) <= problem["rating"] <= (rating + 500) and problem_id not in taken_problems and problem_id not in solved_problems:
                        taken_problems.add(problem_id)
                        problems.append((problem_name, f"https://codeforces.com/problemset/problem/{problem_id[0]}/{problem_id[1]}"))

                        if len(problems)==max_len:
                            break

        return problems


def suggested_problems():
    try:
        problems = []
        username = session.get('codeforces_id')
        rating = session.get('user_rating')

        tags = session.get('tags')
        solved_problems = get_solved_problems(username)
        taken_problems = set()
        
        for i, (tag, count) in enumerate(tags):
            if i >= 10:
                break
            tag_problems = fetch_data(tag, rating, taken_problems, solved_problems, 10)
            problems.append(tag_problems)

        problems = sum(problems, [])
        return problems
    
    except:
        raise Exception("Failed to fetch data.")