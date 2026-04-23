import subprocess
import sys
import os

SAMPLES = [{'input': '3 4', 'output': 'Even'}, {'input': '1 21', 'output': 'Odd'}]

print("=== TEST START ===")

for i, sample in enumerate(SAMPLES):
    print(f"[TEST {i+1}]")
    
    solution_path = os.path.join(os.path.dirname(__file__), "Solution.py")
    
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
