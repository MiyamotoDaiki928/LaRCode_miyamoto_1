import subprocess
import sys
import os

SAMPLES = [{'input': '3 3\r\n1 2 3', 'output': '3'}, {'input': '4 5\r\n10 1 10 1', 'output': '7'}, {'input': '20 457\r\n8 9 10 9 8 8 4 6 8 1 5 10 2 8 2 6 8 1 6 6', 'output': '132'}]

print("=== TEST START ===")

for i, sample in enumerate(SAMPLES):
    print(f"[TEST {i+1}]")
    
    solution_path = os.path.join(os.path.dirname(__file__), "Solution D.py")
    
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
