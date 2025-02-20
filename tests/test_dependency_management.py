import subprocess
import pytest

def test_dependencies_installed():
    result = subprocess.run(['uv', 'list'], capture_output=True, text=True)
    assert result.returncode == 0
    output = result.stdout.strip()
    assert "pulumi" in output
    assert "pulumi-kubernetes" in output
    assert "kubernetes" in output
    assert "ansible" in output
    assert "ray" in output

def test_uv_configuration():
    result = subprocess.run(['uv', 'install'], capture_output=True, text=True)
    assert result.returncode == 0
    assert "All dependencies are installed and up-to-date" in result.stdout
