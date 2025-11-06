<!--
README for Roman Urdu Poetry Generator
Crafted with ❤️ by Asad Sandhu
-->

<div align="center">

# 🕊️ **Roman Urdu Poetry Generator**  
### _AI-Powered Poetic Expression in Roman Urdu_  

🌸 *“Where code meets emotion, and verses are born from data.”* 🌸  

---

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-ee4c2c?logo=pytorch)](https://pytorch.org/)
[![Gradio](https://img.shields.io/badge/Gradio-Interface%20App-green?logo=gradio)](https://gradio.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 🌟 Overview  

**Roman Urdu Poetry Generator** is an AI-based text generator that creates poetic verses in **Roman Urdu**, inspired by the works of poets like *Ahmad Faraz* and *Mir Taqi Mir*.  

Built using **LSTM (Long Short-Term Memory)** networks in **PyTorch**, the model learns from a curated dataset of Urdu poetry transliterated into Roman script. It then composes new, coherent poetic lines — often surprisingly soulful. 💫  

You can interact with it through a **Gradio Web App**, adjusting:  
- 🎨 **Creativity** (`temperature`)  
- ✍️ **Poem length** (`number of words`)  
- 📏 **Structure** (`words per line`)  

---

## 🧠 How It Works  

1. The model reads your **starting phrase** (e.g., _“aañkh se”_).  
2. It predicts the **next most likely word**, one token at a time.  
3. Words are grouped into lines, forming rhythmic verses.  
4. You control how “creative” or “logical” the poem sounds with the **temperature** slider.

> 🪄 *A higher temperature = more creativity & randomness. A lower one = more structure & logic.*

---

## ⚙️ Tech Stack  

| Component | Technology |
|------------|-------------|
| 🧩 Model Type | LSTM (Long Short-Term Memory Network) |
| 🧠 Framework | PyTorch |
| 💬 Interface | Gradio |
| 📁 Dataset | *Roman Urdu Poetry.csv* |
| 🧾 Language | Python 3.9+ |

---

## 🧩 File Structure  

```

📂 Roman-Urdu-Poetry-Generator
│
├── 📄 app.py                 # Main app (model + Gradio UI)
├── 📄 poetry_model.pth       # Trained LSTM model checkpoint
├── 📄 Roman-Urdu-Poetry.csv  # Training dataset (poems in Roman Urdu)
└── 📄 README.md              # You're reading this :)

```

---

## 🚀 Getting Started  

### 🔧 1. Clone the Repository  
```bash
git clone https://github.com/your-username/Roman-Urdu-Poetry-Generator.git
cd Roman-Urdu-Poetry-Generator
````

### 📦 2. Install Dependencies

```bash
pip install torch gradio numpy
```

### 💡 3. Run the App

```bash
python app.py
```

This will automatically launch the **Gradio interface** in your browser. 🌐

---

## 💻 Gradio Interface Preview

<div align="center">

🎤 **Roman Urdu Poetry Generator**

> *Generate poetic verses in Roman Urdu using an AI trained on classic poetry.*

| Input                       | Control                      |
| --------------------------- | ---------------------------- |
| 🪶 Starting Word            | “aañkh”, “dil”, “ishq”, etc. |
| 🔢 Number of Words          | Choose total poem length     |
| 🔥 Creativity (Temperature) | Adjust imagination level     |
| 📏 Words per Line           | Control verse structure      |

</div>

---

## 🪶 Example Output

**Input:**

> Starting Word: `aañkh`
> Number of Words: `25`
> Temperature: `1.0`
> Words per Line: `4`

**Generated Poetry:**

```
aañkh se duur na ho dil se utar jaayega  
waqt ka kya hai guzarta hai guzar jaayega  
itna maanus na ho khalvat-e-gham se apni  
tu kabhi khud ko bhi dekhega to dar jaayega
```

> 💫 *Sometimes, even AI has feelings.*

---

## 🧩 Model Details

The model uses a **multi-layer LSTM** network to learn sequential word patterns from poetry.

**Model Configuration:**

* Embedding Dimension: `128`
* Hidden Dimension: `256`
* LSTM Layers: `2`
* Dropout: `0.2`
* Optimized for Roman Urdu poetic syntax

---

## 📚 Dataset

The dataset `Roman-Urdu-Poetry.csv` contains handpicked poems from various Urdu poets transliterated into **Roman Urdu**. Each record includes:

* Poet’s Name
* Original Roman Urdu Poem Text

> 🧾 Example entry:
>
> ```
> Poet: ahmad-faraz  
> Poetry: "aañkh se duur na ho dil se utar jaayega..."
> ```

---

## 🎨 Future Enhancements

✅ Add multilingual support (Urdu script + English translations)
✅ Train on larger poetry datasets (Mir, Faiz, Iqbal)
✅ Implement rhyme & rhythm detection
✅ Add voice output using TTS (Text-to-Speech)

---

## 🤝 Contributing

Contributions are always welcome! 💬
If you’d like to enhance the model, improve training data, or design a better interface, feel free to:

```bash
fork -> code -> commit -> pull request
```

---

## 🪙 License

This project is licensed under the **MIT License** — free to use, modify, and share.

> See the [LICENSE](LICENSE) file for details.

---

<div align="center">

✨ *“Poetry is not written by code — it’s awakened by it.”* ✨

Made with ❤️ using **Python, PyTorch & Gradio**

</div>

---
