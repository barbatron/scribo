# Scribo

Scribo is a simple audio transcription tool that uses OpenAI's Whisper model to
convert speech to text.

## Features

- Transcribe audio files using state-of-the-art speech recognition
- Support for GPU acceleration if available
- Easy command-line interface

## Requirements

- Python 3.12 or higher
- FFmpeg (for audio processing)

## Installation

### Using Poetry

```bash
git clone https://github.com/yourusername/scribo.git
cd scribo
poetry install
```

### Using Docker

```bash
docker build -t scribo .
```

## Usage

### Command Line

```bash
python scribo.py path/to/your/audio/file.mp3
```

### With Docker

```bash
docker run -v /path/to/your/audio:/app/data scribo data/your-audio-file.mp3
```

## Development

This project uses Poetry for dependency management:

```bash
# Install development dependencies
poetry install

# Run linting
poetry run ruff check .
poetry run ruff format .
```

## License

See [LICENSE](./LICENSE)
