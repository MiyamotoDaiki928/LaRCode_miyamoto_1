import subprocess
import sys
import os

SAMPLES = [{'input': '3\n3 10 20 30\n1 7\n4 5 6 7 8\n3 4', 'output': '8'}, {'input': '4\n2 9 1\n3 8 2 6\n1 5\n2 4 3\n2 2', 'output': '2'}, {'input': '1\n5 100 200 300 400 500\n1 5', 'output': '500'}]

print("=== TEST START ===")

for i, sample in enumerate(SAMPLES):
    print(f"[TEST {i+1}]")
    
    solution_path = os.path.join(os.path.dirname(__file__), "Solution B.py")
    
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
