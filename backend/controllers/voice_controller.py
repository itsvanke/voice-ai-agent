
import time
from services.speech_to_text.whisper_stt import speech_to_text
from services.language_detection.detect import detect_language
from agent.reasoning.agent_engine import process_request
from services.text_to_speech.tts_engine import text_to_speech

async def handle_voice(audio):
    start = time.time()

    text = speech_to_text(audio)
    language = detect_language(text)

    print("User:", text)
    print("Language:", language)

    response = process_request(text)
    audio_response = text_to_speech(response)

    latency = time.time() - start
    print("Latency:", latency)

    return audio_response
