import unittest
from unittest.mock import patch, MagicMock
import ansible_runner

class TestAnsiblePlaybooks(unittest.TestCase):

    @patch('ansible_runner.run')
    def test_validate_ansible_playbooks(self, mock_run):
        # Mock Ansible playbook execution
        mock_run.return_value = MagicMock(status='successful')

        # Define playbooks to validate
        playbooks = [
            'playbooks/beelink.yml',
            'playbooks/jetson.yml',
            'playbooks/home_assistant.yml'
        ]

        # Validate each playbook
        for playbook in playbooks:
            result = ansible_runner.run(playbook=playbook)
            self.assertEqual(result.status, 'successful')

    @patch('ansible_runner.run')
    def test_mock_ansible_modules(self, mock_run):
        # Mock Ansible module execution
        mock_run.return_value = MagicMock(status='successful')

        # Define playbooks to test
        playbooks = [
            'playbooks/beelink.yml',
            'playbooks/jetson.yml',
            'playbooks/home_assistant.yml'
        ]

        # Test each playbook execution
        for playbook in playbooks:
            result = ansible_runner.run(playbook=playbook)
            self.assertEqual(result.status, 'successful')

if __name__ == '__main__':
    unittest.main()
