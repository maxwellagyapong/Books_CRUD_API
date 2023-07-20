import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True)
        print("Command executed successfully with output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing the command: {e}")
