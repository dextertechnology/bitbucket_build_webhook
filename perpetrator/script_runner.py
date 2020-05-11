import subprocess


class RunScript:
    def __init__(self, script_file):
        self.script_file = script_file
    
    def execute(self):
        return subprocess.run(["/bin/bash", self.script_file])