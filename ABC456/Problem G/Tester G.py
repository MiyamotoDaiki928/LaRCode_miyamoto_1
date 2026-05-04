import subprocess
import sys
import os

SAMPLES = [{'input': '5\n.x...', 'output': '9\n4\n2\n0\n0'}, {'input': '7\n.......', 'output': '33\n47\n27\n12\n5\n2\n1'}, {'input': '20\n.....x...x..........', 'output': '9359\n75312\n94664\n46840\n23680\n7168\n3072\n1280\n512\n256\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0'}]

print("=== TEST START ===")

for i, sample in enumerate(SAMPLES):
    print(f"[TEST {i+1}]")
    
    solution_path = os.path.join(os.path.dirname(__file__), "Solution G.py")
    
    result = subprocess.run(
        [sys.executable, solution_path],
        input=sample["input"].replace("\r\n", "\n") + "\n",
        text=True,
        capture_output=True
    )

    output = result.stdout.strip()
    expected = sample["output"].strip()

    print("Input:")
    print(sample["input"])
    print("Output:", output)
    print("Expected:", expected)

    print("OK" if output == expected else "NG")
    print("-" * 20)
