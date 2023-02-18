from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
  {
    'id': 1,
    'title': 'data analyst',
    'location': 'manila',
    'salary': '$5600'
  },
  {
    'id': 2,
    'title': 'engineer',
    'location': 'laguna',
    'salary': '$1400'
  },
{
    'id': 3,
    'title': 'staff',
    'location': 'remote',
    
  }
]


@app.route("/")
def hello():
  return render_template('home.html', jobs = JOBS, company_name = 'sherwin')


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)