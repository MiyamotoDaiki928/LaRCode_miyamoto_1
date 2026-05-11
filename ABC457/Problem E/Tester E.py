import subprocess
import sys
import os

SAMPLES = [{'input': '4 3\r\n1 3\r\n1 1\r\n2 4\r\n4\r\n1 4\r\n2 4\r\n1 3\r\n1 1', 'output': 'Yes\r\nNo\r\nYes\r\nNo'}, {'input': '7 10\r\n2 6\r\n2 5\r\n3 6\r\n1 6\r\n1 2\r\n5 6\r\n2 3\r\n3 7\r\n2 3\r\n1 2\r\n10\r\n1 2\r\n3 5\r\n1 4\r\n1 5\r\n1 5\r\n5 7\r\n1 6\r\n2 3\r\n5 7\r\n2 4', 'output': 'Yes\r\nNo\r\nNo\r\nYes\r\nYes\r\nNo\r\nYes\r\nYes\r\nNo\r\nNo'}]

print("=== TEST START ===")

for i, sample in enumerate(SAMPLES):
    print(f"[TEST {i+1}]")
    
    solution_path = os.path.join(os.path.dirname(__file__), "Solution E.py")
    
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
