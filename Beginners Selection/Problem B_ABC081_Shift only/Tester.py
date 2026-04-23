import subprocess
import sys
import os

SAMPLES = [{'input': '3\r\n8 12 40', 'output': '2'}, {'input': '4\r\n5 6 8 10', 'output': '0'}, {'input': '6\r\n382253568 723152896 37802240 379425024 404894720 471526144', 'output': '8'}]

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
