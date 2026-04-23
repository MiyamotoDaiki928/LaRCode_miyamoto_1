import subprocess
import sys
import os

SAMPLES = [{'input': '2\r\n2\r\n2\r\n100', 'output': '2'}, {'input': '5\r\n1\r\n0\r\n150', 'output': '0'}, {'input': '30\r\n40\r\n50\r\n6000', 'output': '213'}]

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
