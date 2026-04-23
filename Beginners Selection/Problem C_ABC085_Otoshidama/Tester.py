import subprocess
import sys
import os

SAMPLES = [{'input': '9 45000', 'output': '4 0 5'}, {'input': '20 196000', 'output': '-1 -1 -1'}, {'input': '1000 1234000', 'output': '14 27 959'}, {'input': '2000 20000000', 'output': '2000 0 0'}]

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
