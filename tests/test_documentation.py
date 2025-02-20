import os
import pytest

def test_documentation_accuracy():
    docs_path = "docs/"
    assert os.path.exists(docs_path), f"Documentation directory {docs_path} does not exist."

    required_files = [
        "configuration-mgmt-repo-structure.md",
        "container-diagram.md",
        "container-images-repo-structure.md.md",
        "homelab-iac-repo-structure.md",
        "repositories.md",
        "specification.md",
        "system-context-diagram.md"
    ]

    for file in required_files:
        file_path = os.path.join(docs_path, file)
        assert os.path.exists(file_path), f"Required documentation file {file_path} is missing."

def test_project_structure_description():
    readme_path = "README.md"
    assert os.path.exists(readme_path), f"README file {readme_path} does not exist."

    with open(readme_path, "r") as readme_file:
        readme_content = readme_file.read()

    expected_sections = [
        "Overview",
        "Prerequisites",
        "Project Structure",
        "Getting Started",
        "Environment Management",
        "Contributing",
        "License",
        "Maintenance"
    ]

    for section in expected_sections:
        assert section in readme_content, f"Section '{section}' is missing from README.md."
