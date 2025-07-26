from flask import Flask, render_template, request, session, redirect, flash, url_for, Blueprint, jsonify
from data_processing import fetch_submissions_data, get_tags_and_solved_problems, analyze_user_problems, fetch_user_data, store_solved_problems, store_unsolved_problems, get_unsolved_problems
from fetch_problems import suggested_problems
from routes.problem_routes import problem_routes
from database import db, User, Favourites

app = Flask(__name__)
app.secret_key = "caar"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

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
            submissions_data = fetch_submissions_data(username) # fetch_submissions_data function is written in data_processing.py file

            unsolved_problems = analyze_user_problems(submissions_data)
            store_unsolved_problems(username, unsolved_problems)

            if submissions_data is None:
                flash("Codeforces is not responding. Please try again later.")
                return redirect('/')

            if submissions_data.get('status')=="FAILED":
                flash("Please enter a valid username")
                return redirect('/')
            
            user_data = fetch_user_data(username) # fetch_user_data function is written in data_processing.py file

            if user_data is None:
                flash("Codeforces is not responding. Please try again later.")
                return redirect('/')
        
            tags, solved_problems, total_submissions, problems_solved = get_tags_and_solved_problems(submissions_data) # get_tags function is written in data_processing file.py
            session['total_submissions'] = total_submissions
            session['problems_solved'] = problems_solved
            
            store_solved_problems(username, solved_problems)

            sorted_tags = sorted(tags.items(), key=lambda x: x[1], reverse=True)
            session['tags'] = sorted_tags
            
            if "rating" in user_data["result"][0]:
                session['user_rating'] = user_data["result"][0]["rating"]
            else:
                session['user_rating'] = 0

            if "rank" in user_data["result"][0]:
                session['user_rank'] = user_data["result"][0]["rank"]
            else:
                session['user_rank'] = "no_rank"

            flash("Data Fetched Successfully. You can select any of the above options.")

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
    problems = suggested_problems()   # suggested_problmes function is written in fetch_problems.py file
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
    username = session.get('codeforces_id')
    unsolved_problems = get_unsolved_problems(username)

    return render_template("unsolved_problems.html", problems = unsolved_problems)

@app.route('/practice_problems', methods = ['POST','GET'])
def practice_problems():
    username = session.get('codeforces_id')

    if username:
        return render_template("practice_problems.html")

    else:
        return redirect(url_for('main', show_alert='true'))
    
@app.route('/add_to_favourites', methods = ['POST','GET'])
def add_to_favourites():
    data = request.get_json()
    problem_name = data.get("name")
    problem_url = data.get("url")
    username = session.get('codeforces_id')
    user = User.query.filter_by(username=username).first()

    existing = Favourites.query.filter_by(user_id=user.id, problem_name=problem_name).first()
    if existing:
        return jsonify({'message':'Already in favourites!'})
    
    new_fav = Favourites(user_id=user.id, problem_name=problem_name, problem_url=problem_url)
    db.session.add(new_fav)
    db.session.commit()

    return jsonify({'message':'Added to favourites!'})

@app.route('/get_favourites', methods = ['POST','GET'])
def favourites():
    username = session.get('codeforces_id')
    
    if username:
        user = User.query.filter_by(username=username).first()

        favourites = Favourites.query.filter_by(user_id=user.id).all()
        fav_list = [
            {'name':fav.problem_name, 'url':fav.problem_url}
            for fav in favourites
        ]

        return render_template("favourites.html", favourites = fav_list)

    else:
        return redirect(url_for('main', show_alert='true'))
    
@app.route('/remove_from_favourites', methods = ['POST','GET'])
def remove_from_favourites():
    username = session.get('codeforces_id')
    data = request.get_json()
    problem_name = data.get("name")
    problem_url = data.get("url")

    user = User.query.filter_by(username=username).first()

    Favourites.query.filter_by(user_id=user.id, problem_name=problem_name, problem_url=problem_url).delete()
    db.session.commit()
    return jsonify({"success":True})


if __name__=="__main__":
    app.run(debug=True)