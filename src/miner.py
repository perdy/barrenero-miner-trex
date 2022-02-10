import shlex
import subprocess


class Miner:
    def __init__(self, miner_bin: str, config: str):
        self.miner_bin = miner_bin
        self.config = config

    def run(self):
        cmd = shlex.split(self.miner_bin)
        if self.config:
            cmd += ["-c", self.config]

        subprocess.run(cmd)
