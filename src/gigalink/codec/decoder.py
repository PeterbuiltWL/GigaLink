"""
GigaLink Public Acoustic Decoder (Open Source)
Converts received audio tone frequencies back into raw bytes and text strings.
Strictly safe for open-source release. Excludes all proprietary sharding or identity logic.
"""

class GigaLinkDecoder:
    def __init__(self, base_freq=1000, freq_step=100):
        self.base_freq = base_freq
        self.freq_step = freq_step

    def frequency_to_byte(self, freq: float) -> int:
        """Maps an audible frequency back to a single byte (0-255)."""
        byte_val = int(round((freq - self.base_freq) * 10.0 / self.freq_step))
        return max(0, min(255, byte_val))

    def decode_frequencies(self, frequencies: list) -> str:
        """Decodes a list of audio frequencies back into a text string."""
        byte_array = bytearray()
        for freq in frequencies:
            b = self.frequency_to_byte(freq)
            byte_array.append(b)
        return byte_array.decode('utf-8', errors='ignore')

    def verify_checksum(self, data_bytes: bytes, received_checksum: int) -> bool:
        """Verifies standard data integrity using a basic checksum."""
        calculated = sum(data_bytes) % 256
        return calculated == received_checksum
