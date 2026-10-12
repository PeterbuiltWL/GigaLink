"""
Simple Text Transmission Demo
Demonstrates how to encode text into acoustic frequencies using GigaLink.
"""

from gigalink.codec.encoder import GigaLinkEncoder
from gigalink.codec.decoder import GigaLinkDecoder

def main():
    message = "ThunderVault Open Acoustic Transport"
    print(f"Original Message: {message}")

    encoder = GigaLinkEncoder()
    decoder = GigaLinkDecoder()

    frequencies = encoder.encode_text(message)
    print(f"Generated Audio Frequencies (Hz): {frequencies[:5]}... ({len(frequencies)} total tones)")

    decoded_message = decoder.decode_frequencies(frequencies)
    print(f"Decoded Message: {decoded_message}")

    assert message == decoded_message, "Transmission error!"
    print("SUCCESS: Acoustic round-trip complete.")

if __name__ == "__main__":
    main()
