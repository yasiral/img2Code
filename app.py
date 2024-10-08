from flask import Flask, request, render_template
import replicate
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    image_url = None
    prompt = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        input_data = {
            "steps": 25,
            "prompt": f"A sleek and modern landing page web design with white background and rousing fonts: {prompt}",
            "guidance": 3,
            "interval": 2,
            "aspect_ratio": "1:1",
            "safety_tolerance": 2
        }
        output = replicate.run("black-forest-labs/flux-pro", input=input_data)
        image_url = output[0] if isinstance(output, list) else output

    return render_template('index.html', image_url=image_url, prompt=prompt)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
