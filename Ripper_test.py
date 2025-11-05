import hashlib
import jane_ripper as jr
import pytest

def md5(s: str) -> str:
    return hashlib.md5(s.encode("utf-8")).hexdigest()

def write_file(path, lines):
    path.write_text("\n".join(lines) + ("\n" if lines else ""))

def test_crack_passwords(tmp_path):
    
    wfile = tmp_path / "wordlist1.txt"
    hfile = tmp_path / "hashes1.txt"
    words = ["password", "123456", "password", "notinthelist"]
    write_file(wfile, words)
    targets = [md5("123456"), md5("password"), md5("missing")]
    write_file(hfile, targets)
    result = jr.crack_passwords(str(hfile), str(wfile))
    assert list(result.keys()) == targets
    assert result[targets[0]] == "123456"
    assert result[targets[1]] == "password"
    assert result[targets[2]] is None

    
    wfile2 = tmp_path / "wordlist2.txt"
    hfile2 = tmp_path / "hashes2.txt"
    words2 = ["dup", "dup", "unique"]
    write_file(wfile2, words2)
    targets2 = [md5("dup"), md5("unique")]
    write_file(hfile2, targets2)
    res2 = jr.crack_passwords(str(hfile2), str(wfile2))
    assert res2[targets2[0]] == "dup"
    assert res2[targets2[1]] == "unique"

    
    wfile3 = tmp_path / "wordlist3.txt"
    hfile3 = tmp_path / "hashes3.txt"
    write_file(wfile3, [])
    targets3 = [md5("anything"), md5("nothing")]
    write_file(hfile3, targets3)
    res3 = jr.crack_passwords(str(hfile3), str(wfile3))
    assert all(v is None for v in res3.values())

    
    wfile4 = tmp_path / "wordlist4.txt"
    hfile4 = tmp_path / "hashes4.txt"
    write_file(wfile4, ["Password", "password"])
    targets4 = [md5("Password"), md5("password")]
    write_file(hfile4, targets4)
    res4 = jr.crack_passwords(str(hfile4), str(wfile4))
    assert res4[targets4[0]] == "Password"
    assert res4[targets4[1]] == "password"

    
    wfile5 = tmp_path / "wordlist5.txt"
    hfile5 = tmp_path / "hashes5.txt"
    write_file(wfile5, ["foo", "bar", "baz", "password"])
    targets5 = [md5("password")]
    write_file(hfile5, targets5)
    res5 = jr.crack_passwords(str(hfile5), str(wfile5))
    assert res5[targets5[0]] == "password"
