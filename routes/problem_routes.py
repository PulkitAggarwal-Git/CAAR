from flask import Flask, render_template, request, session, redirect, flash, url_for, Blueprint
from fetch_problems import fetch_data

problem_routes = Blueprint('problem_routes', __name__, url_prefix = '/practice_problems')

@problem_routes.route('/load_dp')
def load_dp():
    return render_template("loading.html", value = "dp")

@problem_routes.route('/dp', methods = ['POST'])
def dp():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("dp", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_greedy')
def load_greedy():
    return render_template("loading.html", value = "greedy")

@problem_routes.route('/greedy', methods = ['POST'])
def greedy():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("greedy", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_constructive')
def load_constructive():
    return render_template("loading.html", value = "greedy")

@problem_routes.route('/constructive', methods = ['POST'])
def constructive():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("constructive algorithms", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)


@problem_routes.route('/load_sortings')
def load_sortings():
    return render_template("loading.html", value = "sortings")

@problem_routes.route('/sortings', methods = ['POST'])
def sortings():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("sortings", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_implementation')
def load_implementation():
    return render_template("loading.html", value = "implementation")

@problem_routes.route('/implementation', methods = ['POST'])
def implementation():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("implementation", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_math')
def load_math():
    return render_template("loading.html", value = "math")

@problem_routes.route('/math', methods = ['POST'])
def math():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("math", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_data_structures')
def load_data_structures():
    return render_template("loading.html", value = "data_structures")

@problem_routes.route('/data_structures', methods = ['POST'])
def data_structures():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("data_structures", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_brute_force')
def load_brute_force():
    return render_template("loading.html", value = "brute_force")

@problem_routes.route('/brute_force', methods = ['POST'])
def brute_force():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("brute force", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_graphs')
def load_graphs():
    return render_template("loading.html", value = "graphs")

@problem_routes.route('/graphs', methods = ['POST'])
def graphs():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("graphs", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_binary_search')
def load_binary_search():
    return render_template("loading.html", value = "bs")

@problem_routes.route('/binary_search', methods = ['POST'])
def binary_search():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("binary search", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_dfs')
def load_dfs():
    return render_template("loading.html", value = "dfs")

@problem_routes.route('/dfs', methods = ['POST'])
def dfs():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("dfs and similar", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_trees')
def load_trees():
    return render_template("loading.html", value = "trees")

@problem_routes.route('/trees', methods = ['POST'])
def trees():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("trees", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_strings')
def load_strings():
    return render_template("loading.html", value = "strings")

@problem_routes.route('/strings', methods = ['POST'])
def strings():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("strings", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_divide_and_conquer')
def load_divide_and_conquer():
    return render_template("loading.html", value = "d&c")

@problem_routes.route('/divide_and_conquer', methods = ['POST'])
def divide_and_conquer():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("divide_and_conquer", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_dsu')
def load_dsu():
    return render_template("loading.html", value = "dsu")

@problem_routes.route('/dsu', methods = ['POST'])
def dsu():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("dsu", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_combinatorics')
def load_combinatorics():
    return render_template("loading.html", value = "combinatorics")

@problem_routes.route('/combinatorics', methods = ['POST'])
def combinatorics():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("combinatorics", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_bitmasks')
def load_bitmasks():
    return render_template("loading.html", value = "bitmasks")

@problem_routes.route('/bitmasks', methods = ['POST'])
def bitmasks():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("bitmasks", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)

@problem_routes.route('/load_two_pointers')
def load_two_pointers():
    return render_template("loading.html", value = "two_pointers")

@problem_routes.route('/two_pointers', methods = ['POST'])
def two_pointers():
    username = session.get('codeforces_id')
    rating = session.get('user_rating')
    solved_problems = set(session.get('solved_problems'))
    taken_problems = set()
    problems = fetch_data("two pointers", rating, taken_problems, solved_problems, 50)
    return render_template("display_practice_problems.html", problems = problems)