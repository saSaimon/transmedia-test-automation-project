import subprocess
import os

# Paths
api_test_path = os.path.join("api", "tests", "test_api.py")
ui_test_path = os.path.join("tests", "test_board_list.py")

def run_pytest(test_path, label):
    print(f"\n🔹 Running {label} tests...\n{'-' * 40}")
    result = subprocess.run(["pytest", test_path], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"❌ {label} tests failed!")
    else:
        print(f"✅ {label} tests passed!")

if __name__ == "__main__":
    # Run API tests
    run_pytest(api_test_path, "API")

    # Run UI tests
    run_pytest(ui_test_path, "UI")