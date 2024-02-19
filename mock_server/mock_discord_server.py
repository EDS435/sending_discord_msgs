from flask import Flask, request, jsonify
app = Flask(__name__)
# Mock storage for messages
mock_messages = {}

# Mock endpoint for sending messages
@app.route('/api/v1/channels/<channel_id>/messages', methods=['POST'])
def send_message(channel_id):
    data = request.json
    if channel_id not in mock_messages:
        mock_messages[channel_id] = []
    # Simulate sending message by storing it
    mock_messages[channel_id].append(data['content'])
    return jsonify({'message': 'Message sent to channel {}'.format(channel_id)})

# Endpoint to retrieve stored messages (for testing purposes)
@app.route('/api/v1/messages', methods=['GET'])
def get_messages():
    return jsonify(mock_messages)

if __name__ == '__main__':
    app.run(debug=True)
