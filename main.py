from flask import Flask, render_template, request, session, redirect, flash, url_for, Blueprint
from data_processing import fetch_submissions_data, get_tags_and_solved_problems, analyze_user_problems, fetch_user_data
from fetch_problems import suggested_problems
from routes.problem_routes import problem_routes

app = Flask(__name__)
app.secret_key = "caar"

app.register_blueprint(problem_routes)

@app.route('/')
def main():
    show_alert = request.args.get('show_alert')
    return render_template('index.html', show_alert = show_alert)


@app.route('/enter', methods=['POST','GET'])
def enter():
    if request.method=="POST":
        username = request.form.get('username')
        
        if not username:
            flash("Please enter your Codeforces username.")
            return redirect(url_for('main'))
        
        if username:
            session['codeforces_id'] = username
            submissions_data = fetch_submissions_data(username)     # fetch_submissions_data function is written in codeforces_data_processing.py file

            if submissions_data.get('status')=="FAILED":
                flash("Please enter a valid username")
                return redirect('/')
            
            user_data = fetch_user_data(username)                   # fetch_user_data function is written in codeforces_data_processing.py file
        
            tags, solved_problems, total_submissions, problems_solved = get_tags_and_solved_problems(submissions_data)            # get_tags function is written in codeforces_data_processing file.py
            session['solved_problems'] = solved_problems
            session['total_submissions'] = total_submissions
            session['problems_solved'] = problems_solved
            
            sorted_tags = sorted(tags.items(), key=lambda x: x[1], reverse=True)
            session['tags'] = sorted_tags
            
            tried_but_unsolved, solved_after_attempts = analyze_user_problems(submissions_data)
            session['tried_but_unsolved'] = tried_but_unsolved
            session['solved_after_attempts'] = solved_after_attempts
            
            if "rating" in user_data["result"][0]:
                session['user_rating'] = user_data["result"][0]["rating"]
            else:
                session['user_rating'] = 0

            if "rank" in user_data["result"][0]:
                session['user_rank'] = user_data["result"][0]["rank"]
            else:
                session['user_rank'] = "no_rank"

    return redirect('/')


@app.route('/profile_analysis', methods=['POST','GET'])
def profile_analysis():
    username = session.get('codeforces_id')
    
    if username:
        return render_template('profile_analysis.html', tags = session.get('tags'), rating = session.get('user_rating'), rank = session.get('user_rank'), problems_solved = session.get('problems_solved'), total_submissions = session.get('total_submissions'))
    else:
        return redirect(url_for('main', show_alert='true'))
    

@app.route('/load_suggested_problems', methods = ['POST','GET'])
def load_suggested_problems():
    username = session.get('codeforces_id')

    if username:
        return render_template('loading.html', value = "suggested")

    else:
        return redirect(url_for('main', show_alert='true'))
    
@app.route('/show_suggested_problems', methods = ['POST','GET'])
def show_suggested_problems():
    problems = suggested_problems()                               # suggested_problmes function is written in fetch_problems.py file
    return render_template("suggested_problems.html", problems = problems)


@app.route('/load_unsolved_problems', methods = ['POST','GET'])
def load_unsolved_problems():
    username = session.get('codeforces_id')

    if username:
        return render_template("loading.html", value = "unsolved")

    else:
        return redirect(url_for('main', show_alert='true'))
    
@app.route('/show_unsolved_problems', methods = ['POST', 'GET'])
def show_unsolved_problems():
    problems1 = session.get('tried_but_unsolved')
    problems2 = session.get('solved_after_attempts')
    problems = problems1 + problems2

    return render_template("unsolved_problems.html", problems = problems)

@app.route('/practice_problems', methods = ['POST','GET'])
def practice_problems():
    username = session.get('codeforces_id')

    if username:
        return render_template("practice_problems.html")

    else:
        return redirect(url_for('main', show_alert='true'))

if __name__=="__main__":
    app.run(debug=True)