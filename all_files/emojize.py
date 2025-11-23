from collections import Counter

def english_score(text: str) -> float:
    freq = {
        'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
        ' ': 13.0, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03,
        'U': 2.76, 'W': 2.36, 'M': 2.41, 'F': 2.23, 'C': 2.78, 'G': 2.02,
        'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'X': 0.15,
        'J': 0.15, 'Q': 0.10, 'Z': 0.07
    }
    return sum(freq.get(c, 0) for c in text.upper())

def break_single_byte_xor(ciphertext: bytes, top_n=10):
    scored_candidates = []
    for key in range(256):
        plaintext_bytes = bytes([b ^ key for b in ciphertext])
        try:
            plaintext = plaintext_bytes.decode('utf-8')
            score = english_score(plaintext)
            scored_candidates.append((score, key, plaintext))
        except UnicodeDecodeError:
            continue
    scored_candidates.sort(reverse=True)
    return scored_candidates[:top_n]  # Return top N

# Example usage:
ciphertext = bytes.fromhex("3a2f2f27296a3a24372b25372b")
top_results = break_single_byte_xor(ciphertext, top_n=95)
for score, key, plaintext in top_results:
    print(f"cwa25{{{plaintext}}}")
