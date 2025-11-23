# single_byte_xor_bruteforce.py
from string import printable

ct_hex = "3a2f2f27296a3a24372b25372b"
ct = bytes.fromhex(ct_hex)

def is_printable(bs):
    return all(chr(b) in printable for b in bs)

candidates = []
for k in range(256):
    pt_bytes = bytes([b ^ k for b in ct])
    if is_printable(pt_bytes):
        pt = pt_bytes.decode('ascii', errors='replace')
        # simple English-ish scoring: count spaces + letters
        score = sum(1 for ch in pt if ch.isalpha() or ch.isspace())
        candidates.append((score, k, pt))

# sort by score (descending) and show top results
candidates.sort(reverse=True)
print("Top candidates (score, key (dec), key (hex), plaintext):")
for score, k, pt in candidates[:20]:
    print(f"{score:3d}   {k:3d}   0x{k:02x}   {pt}")
