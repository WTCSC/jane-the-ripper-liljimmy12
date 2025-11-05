[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21491927)
# Jane the Ripper


## Security & ethics

Do not use this tool to attack systems, crack passwords you do not own or have explicit permission to test, or otherwise perform illegal activity. Only run this on data you are authorized to analyze, misuse is your responsibility.

### What this repo contains

A small MD5 hash wordlist cracker `jane_ripper.py` and tests `ripper_test.py`.                                                                
The cracker reads two files (hash list and wordlist), deduplicates candidates, and tries to match MD5 hashes to plaintext passwords. 

### What the file does
- Reads a file of MD5 hashes (one per line) and a wordlist (one candidate password per line) using with open() and .strip().

- Deduplicates the wordlist with an empty set() and streams candidates to avoid unnecessary work.

- Computes hashlib.md5(candidate.encode("utf-8")).hexdigest() for each candidate and checks if it matches any target hash.

- Prints progress lines for each cracked hash ([+] Cracked: <hash> --> <password>), reports failed hashes, and prints a final summary.

- Returns a mapping of each original hash (order preserved) to the recovered password or None if not found.

### Requirements

- Python 3.8+ (works with 3.8, 3.9, 3.10, 3.11)
- pytest

### Usage

- Run `python jane_ripper.py` to run the hash cracker
- Run `pytest` to run the tests

### flowchart
  A[Start / Run Jane_ripper.py] --> B{Prompt for file paths}                                                                                      
  B -->|User enters custom paths| C[Open hash file (with open)]                                                                                    
  B --> C                                                                                                            
  C --> D[Read hashes -> list + set (strip & lowercase)]                                                                                                                                                                                                                                    
  D --> E[Open wordlist]                                             
  E --> F{For each candidate line}                                                                                    
  F -->|blank or seen before| F                                                                                                          
  F -->|new candidate| G[compute md5(candidate)]                                    
  G --> H{md5 in target set?}                                                                                                                      
  H -->|yes & not found| I[record found; print [+] Cracked line]                                                        
  H -->|no| F                                                                          
  I --> J{All targets found?}                                                                                              
  J -->|yes| K[break loop]                                                              
  J -->|no| F                                                        
  F --> L[After loop -> print FAILED lines for remaining targets]                                                                    
  L --> M[Print final summary & return mapping]                                                                    
  M --> Z[End]                                                                                                        
