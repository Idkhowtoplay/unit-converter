from flask import Flask, render_template, request

app = Flask(__name__)

def convert(units, value, unit_from, unit_to):
    if unit_from == unit_to:
        return value
    
    unit_refer = float(value) * units[unit_from]
    return unit_refer / units[unit_to]

def temperature_convert(value, unit_from, unit_to):
    if value:
        values = int(value)
        if unit_from == unit_to:
            return value
        elif unit_from == "°C" and unit_to == "°F":
            return (9/5 * values) + 32
        elif unit_from == "°F" and unit_to == "°C":
            return 9/5 * (values - 32)
        elif unit_from == "°C" and unit_to == "k":
            return values + 273
        elif unit_from == "k" and unit_to == "°C":
            return values - 27

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/length', methods=['GET', 'POST'])
def length():
    results = None
    unit = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.344
    }
    if request.method == "POST":
        value = request.form.get("length")
        unit_from = request.form.get("unit_from")
        unit_to = request.form.get("unit_to")
        result = convert(unit, value, unit_from, unit_to)
        results = f"{value}{unit_from} = {result}{unit_to}"
    return render_template('length.html', result=results)

@app.route('/weight', methods=['GET', 'POST'])
def weight():
    results = None
    unit = {
        "mg": 0.001,
        "gram": 1,
        "kg": 1000,
        "ounce": 28.3495,
        "pound": 453.592
    }
    if request.method == "POST":
        value = request.form.get("weight")
        unit_from = request.form.get("unit_from")
        unit_to = request.form.get("unit_to")
        result = convert(unit, value, unit_from, unit_to)
        results = f"{value}{unit_from} = {result}{unit_to}"
    return render_template('weight.html', result=results)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    results = None
    if request.method == "POST":
        value = request.form.get("number")
        unit_from = request.form.get("unit_from")
        unit_to = request.form.get("unit_to")
        result = temperature_convert(value, unit_from, unit_to)
        results = f"{value}{unit_from} = {result}{unit_to}"
    return render_template('temperature.html', result=results)

if __name__ == '__main__':
    app.run(debug=True)