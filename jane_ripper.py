import hashlib

def crack_passwords(hash_file, wordlist):
    with open(hash_file, "r", encoding="utf-8") as f:
        targets = [l.strip().lower() for l in f if l.strip()]
    targ_set, found, seen = set(targets), {}, set()
    print("\nStart cracking")
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            w = line.strip()
            if not w or w in seen: continue
            seen.add(w)
            h = hashlib.md5(w.encode()).hexdigest()
            if h in targ_set and h not in found:
                found[h] = w
                print(f"[+] Cracked: {h}  -->  {w}")
                if len(found) == len(targ_set): break
    failed = [h for h in targets if h not in found]
    for h in failed: print(f"[-] FAILED: {h}")
    print("-Cracking complete\n")
    print("[!] All hashes cracked" if not failed else f"[!] Cracked with {len(failed)} failure(s).")
    return {h: found.get(h) for h in targets}

def main():
    h = input("Enter path to your hash file: ").strip() or "hashes.txt"
    w = input("Enter path to your wordlist file: ").strip() or "wordlist.txt"
    try:
        crack_passwords(h, w)
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")

if __name__ == "__main__":
    main()