import sqlite3
from flask import Flask, render_template, abort

app = Flask(__name__)

def get_machine(machine_id):
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name_en, video_url, target_muscle, description FROM machines WHERE id = ?', (machine_id,))
    machine = cursor.fetchone()
    conn.close()
    return machine

@app.route('/machine/<int:machine_id>')
def show_machine(machine_id):
    machine_data = get_machine(machine_id)
    if machine_data is None:
        abort(404)
        
    machine = {
        'name': machine_data[0],
        'video_url': machine_data[1],
        'muscle': machine_data[2],
        'desc': machine_data[3]
    }
    return render_template('machine.html', machine=machine)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)