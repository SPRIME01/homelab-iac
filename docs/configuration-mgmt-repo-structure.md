# Project Structure for Configuration Management Repository

c:\Users\sprim\Focus Areas\Projects\Dev\homelab-IAC\config-management
│
├── README.md              // General documentation for configuration management
├── .gitignore             // Git ignore rules
├── .env                   // Environment variables (e.g., inventories, secrets)
│
├── playbooks/             // Ansible playbooks per device or role
│   ├── beelink.yml
│   ├── jetson.yml
│   └── home_assistant.yml
│
└── roles/                 // Reusable Ansible roles
    ├── common/
    │   └── tasks/         // ...existing code...
    ├── beelink/
    │   └── tasks/         // ...existing code...
    └── jetson/
        └── tasks/         // ...existing code...
