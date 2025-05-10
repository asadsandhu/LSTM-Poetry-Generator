import torch
import torch.nn as nn
import numpy as np
import gradio as gr

# Config
MODEL_PATH = "poetry_model.pth"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Model Definition
class LSTMModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim=128, hidden_dim=256, num_layers=2):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, num_layers, batch_first=True, dropout=0.2)
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x, hidden=None):
        x = self.embedding(x)
        lstm_out, hidden = self.lstm(x, hidden)
        return self.fc(lstm_out[:, -1, :]), hidden

# Load Trained Model
checkpoint = torch.load(MODEL_PATH, map_location=DEVICE)
word_to_index = checkpoint['word_to_index']
index_to_word = {i: w for w, i in word_to_index.items()}

model = LSTMModel(
    len(word_to_index),
    checkpoint['config']['embed_dim'],
    checkpoint['config']['hidden_dim'],
    checkpoint['config']['n_layers']
).to(DEVICE)
model.load_state_dict(checkpoint['model_state'])
model.eval()

# Poetry Generation
def generate_poetry(start_phrase, gen_length=20, temp=1.0, user_words_per_line=4):
    input_words = start_phrase.strip().split()
    input_len = len(input_words)

    # Use max of input length and selected words per line
    words_per_line = max(input_len, user_words_per_line)

    # Initialize
    lines = []
    current_line = input_words.copy()

    # Convert last word in input to index (for input_seq)
    last_word = input_words[-1]
    start_idx = word_to_index.get(last_word, word_to_index['<UNK>'])
    input_seq = torch.full((1, 10), start_idx, dtype=torch.long, device=DEVICE)
    hidden = None

    for _ in range(gen_length):
        with torch.no_grad():
            output, hidden = model(input_seq, hidden)
            probs = torch.softmax(output / temp, dim=1).cpu().numpy().flatten()
            next_idx = np.random.choice(len(probs), p=probs)

        next_word = index_to_word.get(next_idx, '<UNK>')
        current_line.append(next_word)

        if len(current_line) >= words_per_line:
            lines.append(' '.join(current_line))
            current_line = []

        input_seq = torch.cat((input_seq[:, 1:], torch.tensor([[next_idx]], device=DEVICE)), dim=1)

    if current_line:
        lines.append(' '.join(current_line))

    return '\n'.join(lines)

# Gradio Interface
def generate_interface(start_word, length, temp, words_per_line):
    return generate_poetry(start_word, int(length), temp, int(words_per_line))

gr.Interface(
    fn=generate_interface,
    inputs=[
        gr.Textbox(label="Starting Word", value="aañkh"),
        gr.Slider(10, 100, value=20, label="Number of Words"),
        gr.Slider(0.1, 2.0, value=1.0, label="Creativity (Temperature)"),
        gr.Slider(2, 8, value=4, step=1, label="Words per Line")
    ],
    outputs=gr.Textbox(label="Generated Poetry", lines=6),
    title="Roman Urdu Poetry Generator 1",
    description="Generate poetic verses in Roman Urdu using a trained AI model"
).launch()
