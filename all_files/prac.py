# single_byte_xor_breaker.py
from collections import Counter
import string
import math

# English letter frequency (A-Z) — relative frequencies
ENGLISH_FREQ = {
    'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702,
    'F': 0.02228, 'G': 0.02015, 'H': 0.06094, 'I': 0.06966, 'J': 0.00153,
    'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749, 'O': 0.07507,
    'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
    'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974,
    'Z': 0.00074
}

def single_byte_xor(data: bytes, key: int) -> bytes:
    return bytes([b ^ key for b in data])

def score_chi_squared(text: str) -> float:
    """
    Lower chi-squared = closer to English. We return negative chi so that higher is better.
    """
    text = text.upper()
    letters = [c for c in text if 'A' <= c <= 'Z']
    N = max(1, len(letters))
    counts = Counter(letters)
    chi2 = 0.0
    for ch, expected_freq in ENGLISH_FREQ.items():
        observed = counts.get(ch, 0)
        expected = expected_freq * N
        chi2 += ((observed - expected) ** 2) / (expected + 1e-9)
    # return negative to make higher scores better
    return -chi2

def printable_ratio(b: bytes) -> float:
    printable = set(bytes(string.printable, 'ascii'))
    return sum(1 for x in b if x in printable) / max(1, len(b))

COMMON_WORDS = [" the ", " and ", " to ", " of ", " is ", " in ", " that ", " it "]

def word_score(text: str) -> int:
    t = text.lower()
    return sum(t.count(w) for w in COMMON_WORDS)

def score_candidate(candidate_bytes: bytes) -> float:
    # Try decode; if fails, use latin-1 fallback for frequency calculation
    try:
        text = candidate_bytes.decode('utf-8')
    except UnicodeDecodeError:
        text = candidate_bytes.decode('latin-1', errors='ignore')

    # combine heuristics
    s1 = score_chi_squared(text)            # English frequency
    s2 = printable_ratio(candidate_bytes)   # printable ratio 0..1
    s3 = word_score(text)                   # count of common words

    # Weighted sum — tune weights if needed
    final_score = (s1 * 1.0) + (s2 * 50.0) + (s3 * 20.0)
    return final_score

def break_single_byte_xor(ciphertext: bytes, top_n: int = 5):
    results = []
    for k in range(256):
        cand = single_byte_xor(ciphertext, k)
        sc = score_candidate(cand)
        try:
            text = cand.decode('utf-8')
        except UnicodeDecodeError:
            text = cand.decode('latin-1', errors='ignore')
        results.append((sc, k, text))
    results.sort(reverse=True, key=lambda x: x[0])
    return results[:top_n]

# ----- Example usage -----
if __name__ == "_main_":
    # Example ciphertext (hex). Replace with your ciphertext.
    hexcipher = "3a2f2f27296a3a24372b25372b"  # example from many CTF guides
    ciphertext = bytes.fromhex(hexcipher)
    top = break_single_byte_xor(ciphertext, top_n=5)
    for score, key, plaintext in top:
        print(f"Key: {key} (0x{key:02x}) | Score: {score:.2f}")
        print("Plaintext preview:", plaintext[:200])
        print("-" * 60)