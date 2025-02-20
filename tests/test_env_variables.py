import os
import pytest

def test_env_variables_presence():
    required_vars = ["VAR1", "VAR2", "VAR3"]
    for var in required_vars:
        assert var in os.environ, f"Environment variable {var} is missing"

def test_env_variables_sensitivity():
    sensitive_vars = ["SECRET_KEY", "API_TOKEN"]
    for var in sensitive_vars:
        assert var not in os.environ, f"Sensitive environment variable {var} should not be exposed"
