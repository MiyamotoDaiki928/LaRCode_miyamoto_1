import subprocess
import sys
import os

SAMPLES = [{'input': '3 9\r\n3 1 3 2\r\n1 3\r\n2 4 3\r\n1 3 2', 'output': '4'}, {'input': '3 1\r\n1 7\r\n1 111\r\n1 5\r\n1 100 10000', 'output': '7'}, {'input': '3 3163812\r\n5 1 2 3 4 5\r\n4 9 8 7 6\r\n2 10 11\r\n87043 908415 9814', 'output': '9'}]

print("=== TEST START ===")

for i, sample in enumerate(SAMPLES):
    print(f"[TEST {i+1}]")
    
    solution_path = os.path.join(os.path.dirname(__file__), "Solution C.py")
    
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
