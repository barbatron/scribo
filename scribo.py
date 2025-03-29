import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import argparse
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe audio files using Whisper model"
    )
    parser.add_argument(
        "audio_file", nargs="?", help="Path to the audio file to transcribe"
    )
    args = parser.parse_args()

    if args.audio_file is None:
        parser.print_help()
        sys.exit(1)

    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    model_id = "openai/whisper-large-v3"
    eprint("Loading model...")
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
    )
    model.to(device)
    eprint("Setting up pipeline...")
    processor = AutoProcessor.from_pretrained(model_id)

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        torch_dtype=torch_dtype,
        device=device,
    )

    eprint("Processing: " + args.audio_file)
    result = pipe(args.audio_file)
    print(result["text"])


if __name__ == "__main__":
    main()
