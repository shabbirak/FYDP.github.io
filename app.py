from flask import Flask, render_template, request
import matlab.engine  # Import MATLAB engine API for Python

app = Flask(__name__)

# Start MATLAB engine
eng = matlab.engine.start_matlab()

@app.route('/')
def index():
    return render_template('index.html')  # Load the HTML form

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get the form data (mass and acceleration) from the HTML form
        mass = float(request.form['mass'])
        acceleration = float(request.form['acceleration'])

        # Call the MATLAB function to calculate the force
        force = eng.calculateForce(mass, acceleration)

        # Return the result to the HTML page
        return render_template('index.html', result=f"The force is {force} N")
    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
