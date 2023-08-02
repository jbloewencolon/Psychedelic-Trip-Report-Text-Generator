from flask import Flask, request, jsonify
from waitress import serve
import torch # and any other required imports

# Your model loading code
model_checkpoint_path = "/content/drive/MyDrive/Colab Notebooks/Data/trip_reports_model_epoch1"
model.load_state_dict(torch.load(model_checkpoint_path))

def generate_text(drug, category, length=500):
    model.eval()
    input_str = f"The experience of using {drug}, which belongs to the {category} category, is like..."
    input_ids = tokenizer.encode(input_str, return_tensors='pt').to(device)
    attention_mask = (input_ids != tokenizer.pad_token_id).type(input_ids.dtype).to(device)  # Creating the attention mask
    outputs = model.model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,  # Passing the attention mask
        max_length=length,
        num_return_sequences=1,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id  # Setting the pad_token_id
    )
    return tokenizer.decode(outputs[0])

app = Flask(__name__, static_folder="static", template_folder="static")

@app.route('/generate', methods=['POST'])
def generate_text_endpoint():
    data = request.json
    drug = data['drug']
    category = data['category']
    generated_text = generate_text(drug, category)
    return jsonify({'generated_text': generated_text})

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)
