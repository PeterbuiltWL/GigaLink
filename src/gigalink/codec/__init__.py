"""
GigaLink Acoustic Codec Module
Encoder and decoder for text-to-frequency and frequency-to-text conversion.
"""

from .encoder import GigaLinkEncoder
from .decoder import GigaLinkDecoder

__all__ = ["GigaLinkEncoder", "GigaLinkDecoder"]
