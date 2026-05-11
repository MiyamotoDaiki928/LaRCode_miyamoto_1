import subprocess
import sys
import os

SAMPLES = [{'input': '4\n0 2\n1 0\n2 1\n2 3', 'output': '2'}, {'input': '5\n0 1\n0 2\n0 3\n0 4\n0 5', 'output': '5'}, {'input': '8\n10 4\n4 2\n7 10\n5 3\n1 9\n0 6\n3 8\n0 9', 'output': '2'}]

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
