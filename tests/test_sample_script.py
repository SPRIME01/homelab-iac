import subprocess
import pytest

def test_sample_script():
    result = subprocess.run(['python', 'hello.py'], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello from homelab-iac!"
