import subprocess
import sys
import os

SAMPLES = [{'input': '4\r\n10\r\n8\r\n8\r\n6', 'output': '3'}, {'input': '3\r\n15\r\n15\r\n15', 'output': '1'}, {'input': '7\r\n50\r\n30\r\n50\r\n100\r\n50\r\n80\r\n30', 'output': '4'}]

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
