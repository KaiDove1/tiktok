from openai import OpenAI
import time

def main():
    client = OpenAI(api_key="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")

    with open("FILENAME.mp3", "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
        # Process the transcript here

        text = transcript['text']
    
        # Optionally, split the text into sentences or process as needed
        sentences = text.split('. ')

        # Print the transcribed text or do other processing as needed
        for sentence in sentences:
            print(sentence)

if __name__ == "__main__":
    main()
