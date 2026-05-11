import subprocess
import sys
import os

SAMPLES = [{'input': '5\r\n1 2 3 4 5\r\n3', 'output': '3'}, {'input': '10\r\n6 6 9 6 10 5 7 2 8 2\r\n4', 'output': '6'}, {'input': '10\r\n4 4 4 3 4 2 1 1 2 1\r\n10', 'output': '1'}]

print("=== TEST START ===")

for i, sample in enumerate(SAMPLES):
    print(f"[TEST {i+1}]")
    
    solution_path = os.path.join(os.path.dirname(__file__), "Solution A.py")
    
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
