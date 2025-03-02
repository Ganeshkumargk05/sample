import subprocess
import time

# Define test cases (input, expected_output, time_limit in seconds)
test_cases = [
    ("input1.txt", "expected_output1.txt", 2),
]

def run_test_case(input_file, expected_output_file, time_limit):
    start_time = time.time()
    
    # Run the participant's script
    try:
        result = subprocess.run(
            ["python3", "solution.py"],  # Adjust command for other languages
            stdin=open(input_file, "r"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=time_limit,
            text=True
        )
    except subprocess.TimeoutExpired:
        print(f"❌ Time limit exceeded for {input_file}")
        return False

    end_time = time.time()
    execution_time = end_time - start_time
    
    # Check output correctness
    expected_output = open(expected_output_file).read().strip()
    actual_output = result.stdout.strip()

    if actual_output == expected_output:
        print(f"✅ Passed {input_file} in {execution_time:.2f} seconds")
        return True
    else:
        print(f"❌ Failed {input_file}. Expected {expected_output}, but got {actual_output}")
        return False

# Run all test cases
all_passed = all(run_test_case(tc[0], tc[1], tc[2]) for tc in test_cases)

if not all_passed:
    exit(1)  # GitHub Actions will mark the run as failed
