from flask import Flask, render_template, request, jsonify
import replicate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    user_prompt = request.form.get('prompt')
    
    # Enhance the user prompt with a predetermined template
    enriched_prompt = f"Web app front end design: {user_prompt}"

    input_data = {
        "steps": 25,
        "prompt": enriched_prompt,
        "guidance": 3,
        "interval": 2,
        "aspect_ratio": "1:1",
        "safety_tolerance": 2
    }

    output = replicate.run(
        "black-forest-labs/flux-pro",
        input=input_data,
    )
    image_url = output[0] if isinstance(output, list) else output
    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
