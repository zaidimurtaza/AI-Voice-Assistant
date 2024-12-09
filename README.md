# AI Assistant using Ollama Llama

## Overview
This project is an AI-powered assistant built using the Ollama Llama 3.2 model. It is designed to take voice input, process the data, and respond with audio output. The assistant is capable of understanding natural language queries and providing insightful, conversational responses.

## Features
- **Voice Input:** Accepts input via microphone and processes natural language queries.
- **Audio Output:** Responds to queries with synthesized voice output.
- **Conversational AI:** Powered by the Ollama Llama model for contextual and accurate responses.
- **User-Friendly Interface:** Simple and intuitive for seamless interactions.

## Tech Stack
- **Backend:** Python
- **AI Model:** Ollama Llama 3.2
- **Libraries:**
  - SpeechRecognition
  - pyttsx3
  - OpenAI's Ollama SDK

## Installation

### Prerequisites
- Python 3.8 or later
- An active API key for Ollama Llama
- Microphone and speaker setup for voice input and output

### Steps
1. **Clone the repository**
   ```bash
   git clone [https://github.com/yourusername/ai-assistant-ollama-llama.git](https://github.com/zaidimurtaza/AI-Voice-Assistant.git)
   cd ai-assistant-ollama-llama
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   Replace `your_api_key` with your actual Ollama Llama API key:
   ```bash
   export OLLAMA_API_KEY=your_api_key  # On Windows, use `set OLLAMA_API_KEY=your_api_key`
   ```

5. **Run the assistant**
   ```bash
   python main.py
   ```

## Usage
1. Start the application.
2. Speak your query into the microphone when prompted.
3. The assistant processes the query and responds via audio output.

## Example Queries
- "What's the weather today?"
- "Tell me a joke."
- "Set a reminder for 6 PM."
- "How does machine learning work?"

## File Structure
```
.
├── main.py               # All assistant logic
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation

```

## Future Improvements
- Enhance natural language understanding for more complex queries.
- Add support for multi-lingual queries and responses.
- Integrate with external APIs (e.g., weather, reminders, news).

## Contributions
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Special thanks to Ollama for providing the Llama 3.2 model.
- OpenAI and the developer community for the supporting libraries.
