from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def convert_kg_to_lb(kg):
    """Convert kilograms to pounds"""
    return kg * 2.20462

def convert_lb_to_kg(lb):
    """Convert pounds to kilograms"""
    return lb / 2.20462

@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.get_json()
        weight = float(data['weight'])
        
        if data['from_unit'] == 'kg':
            result = convert_kg_to_lb(weight)
            return jsonify({
                'converted_weight': round(result, 2),
                'to_unit': 'lb'
            })
        else:
            result = convert_lb_to_kg(weight)
            return jsonify({
                'converted_weight': round(result, 2),
                'to_unit': 'kg'
            })
    except (ValueError, KeyError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
