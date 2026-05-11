import subprocess
import sys
import os

SAMPLES = [{'input': '3\n1 1', 'output': '4'}, {'input': '5\n1 2 2 1', 'output': '0'}, {'input': '15\n4 4 4 4 4 4 3 2 2 2 2 2 1 1', 'output': '70270200'}]

print("=== TEST START ===")

for i, sample in enumerate(SAMPLES):
    print(f"[TEST {i+1}]")
    
    solution_path = os.path.join(os.path.dirname(__file__), "Solution F.py")
    
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
