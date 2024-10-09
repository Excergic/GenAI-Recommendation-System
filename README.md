# GenAI Recommendation System  
An open-source AI-powered recommendation system that generates personalized suggestions for study desk setups, interior design, and fashion based on image input.

## Features  
🖼️ Object detection in uploaded images  
💡 AI-powered recommendations using open-source LLMs  
🎨 AI-generated visualization of suggestions  
📊 Interactive Streamlit interface  

## Tech Stack  
Python 3.9+  
Streamlit  
YOLOv8 for object detection  
Ollama for text generation  
Stable Diffusion for image generation  

## Installation  

1.Clone the repository:
```bash
git clone https://github.com/Excergic/GenAI-Recommendation-System.git
cd GenAI-Recommendation-System
```

2.Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3.Install dependencies:
```bash
pip install -r requirements.txt
```

4.Install Ollama:  
👉Visit https://ollama.ai  
👉Follow installation instructions for your OS  

5.Pull required models:  
```bash
ollama pull gemma2:2b
```

## Usage  
1.Start Ollama:  
```bash
ollama run gemma2:2b
```

2.Run the Streamlit app:  
```bash
streamlit run src/streamlit_app.py
```

3.Open your browser and navigate to http://localhost:8501  

## Contributing  

1.Fork the repository  
2.Create your feature branch (git checkout -b feature/amazing-feature)  
3.Commit your changes (git commit -m 'Add amazing feature')  
4.Push to the branch (git push origin feature/amazing-feature)  
5.Open a Pull Request  

## License  
This project is licensed under the MIT License - see the LICENSE file for details.  

## Acknowledgments  
👉YOLOv8 by Ultralytics  
👉Ollama for providing open-source LLM infrastructure  
👉Stable Diffusion by Stability AI    




