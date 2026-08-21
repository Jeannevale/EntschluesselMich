import os


class Schluessel:
    def __init__(self):
        self.name = "me"
        self.note=os.getenv("NOTE","NOTE")
        self.schluessel="2"
        self.age=1

    def open(self):
        self.name=self.value
        return self.name

    def write(self,directory,content):

        import csv

        with open(directory, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(content)


class Antivirus(Exception):

    def __init__(self):
        super().__init__(
            "Threat detected\n"
            "Threat name: Trojan:Win32.Angriff\n"
            "Severity: High\n"
            "Action: Quarantined\n"
            "Status: Blocked"
        )
        self.text="Traceback (most recent call last):"
        self.line='  File "main.py", line 8, in <module> subprocess.run([sys.executable, script_name])'
