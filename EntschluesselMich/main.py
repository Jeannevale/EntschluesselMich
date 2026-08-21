import threading
import subprocess
import sys

answer=input("Wie heißt du?")

def run_script(script_name):
    subprocess.run([sys.executable, script_name])

if __name__ == "__main__":
    script1_thread = threading.Thread(target=run_script, args=("schluessel1.py",))
    script2_thread = threading.Thread(target=run_script, args=("schluessel2.py",))

    script1_thread.start()
    script2_thread.start()

