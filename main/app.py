

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return "OK", 200

@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()
    return jsonify({"received": data}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# --- 1. Homepage Route ---
# This is the main landing page for the application.
# Member 2 (Frontend) will likely update this route to render an HTML template.
@app.route('/')
def home():
    """
    Serves the homepage.
    """
    return "Welcome to the Collaborative Flask Lab Project!", 200

# --- 2. Health Check Route ---
# This route is used by monitoring services (and our unit tests)
# to verify that the application is running and healthy.
# The lab's unit test specifically checks for the string "OK".
@app.route('/health')
def health_check():
    """
    Provides a simple health check endpoint.
    Returns "OK" with a 200 status code if the app is running.
    """
    return "OK", 200

# --- 3. POST Endpoint ---
# This route demonstrates how to handle incoming data,
# specifically in JSON format.
@app.route('/data', methods=['POST'])
def handle_data():
    """
    Handles POST requests containing JSON data.
    Validates that the request is JSON and returns a confirmation.
    """
    # Check if the incoming request has the JSON MIME type
    if request.is_json:
        # Parse the JSON data from the request
        data = request.get_json()
        
        # You could add logic here to process the data (e.g., save to a database)
        
        # Send a success response back to the client
        return jsonify({
            "message": "Data received successfully!",
            "your_data": data
        }), 201 # 201 Created is a standard HTTP status for a successful POST
    else:
        # If the request is not JSON, return a 400 Bad Request error
        return jsonify({
            "error": "Invalid request: Content-Type must be 'application/json'"
        }), 400

# --- Main execution block ---
# This allows you to run the app directly using "python main/app.py"
# The 'host="0.0.0.0"' part is crucial for Docker,
# as it makes the app accessible from outside the container.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

