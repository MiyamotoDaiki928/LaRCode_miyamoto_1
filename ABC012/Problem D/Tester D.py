import subprocess
import sys
import os

SAMPLES = [{'input': '3 2\r\n1 2 10\r\n2 3 10', 'output': '10'}, {'input': '5 5\r\n1 2 12\r\n2 3 14\r\n3 4 7\r\n4 5 9\r\n5 1 18', 'output': '26'}, {'input': '4 6\r\n1 2 1\r\n2 3 1\r\n3 4 1\r\n4 1 1\r\n1 3 1\r\n4 2 1', 'output': '1'}]

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
