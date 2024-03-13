import subprocess

def test(in_, exp):
    p = subprocess.run(
        ["./main"],
        input=f"{in_}\n".encode(),
        capture_output=True,
    )
    out = p.stdout.decode().strip()
    if exp != out:
        print(in_, "assertion error", "expected =", exp, "got =", out)

test("3 10 8 2", "3")
test("3 10 2 8", "3")
test("10 3 8 2", "3")
test("3 10 4 1", "7")
test("8 10 8 2", "2")
test("18 20 8 2", "2")
test("18 2 8 2", "10")
test("18 2 8 3", "11")
test("18 2 1 0", "16")
test("18 2 20 1", "3")
test("18 20 15 1", "2")
test("18 20 5 1", "2")
test("18 20 21 30", "2")
