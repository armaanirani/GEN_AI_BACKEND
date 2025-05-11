# LLM Backend Boilerplate

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A production-ready Python backend boilerplate for Large Language Model (LLM) integration, featuring clean architecture, modular design, and comprehensive API support.

## Features

- **Modular Architecture**: Clear separation of routes, services, and LLM implementations
- **LLM Factory Pattern**: Easily switch between different LLM providers
- **Production Ready**: Built-in logging, configuration management, and health checks
- **RESTful API**: Standardized endpoints for QA and model selection
- **Environment Configuration**: Dotenv support for secure credential management

## Project Structure

```
.
├── app/                  # Application core
│   ├── api/              # API routes
│   │   └── routes/       # Route implementations
│   ├── llm/              # LLM integrations
│   └── services/         # Business logic
├── logs/                 # Application logs
├── utils/                # Utility modules
├── config.json           # Main configuration
├── env_template.txt      # Environment template
├── main.py               # Application entry point
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.9+
- pip package manager
- LLM API keys (as needed for your providers)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/armaanirani/GEN_AI_BACKEND.git
   cd GEN_AI_BACKEND
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy the environment template:
   ```bash
   cp env_template.txt .env
   ```

5. Update `.env` with your configuration values

### Configuration

Edit `config.json` for application settings:

```json
{
  "app": {
    "host": "0.0.0.0",
    "port": 8000,
    "debug": false,
    "log_level": "INFO"
  },
  "llm": {
    "default_provider": "openai"
  }
}
```

## Environment Variables

The following environment variables are required (place in `.env` file):

```
# LLM Provider API Keys
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
COHERE_API_KEY=

# Application Settings
APP_ENV=development
SECRET_KEY=your-secret-key-here
```

## API Documentation

### Health Check
`GET /health`
- Returns application health status

### Question Answering
`POST /qa`
- Request body:
  ```json
  {
    "question": "Your question here",
    "context": "Optional context",
    "model": "Optional model override"
  }
  ```
- Returns:
  ```json
  {
    "answer": "Generated response",
    "model": "Model used",
    "timestamp": "ISO-8601 timestamp"
  }
  ```

### Model Selection
`POST /select-llm`
- Request body:
  ```json
  {
    "provider": "openai|anthropic|cohere",
    "model": "model-name"
  }
  ```
- Returns confirmation of active model

## Development

### Running Locally

```bash
python main.py
```

### Testing

```bash
pytest tests/
```

### Logging

Logs are written to `logs/app.log` with rotation. Configure level in `config.json`.

## Deployment

### Docker

```bash
docker build -t llm-backend .
docker run -p 8000:8000 llm-backend
```

### Kubernetes

Sample deployment manifest provided in `deploy/` directory.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Armaan Irani - armaanirani@gmail.com

Project Link: [https://github.com/armaanirani/GEN_AI_BACKEND](https://github.com/armaanirani/GEN_AI_BACKEND)
