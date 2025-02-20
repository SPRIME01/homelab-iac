# homelab-IAC

Infrastructure as Code (IaC) for managing a homelab environment using Pulumi and Kubernetes.

## Overview

This repository contains the infrastructure configuration for a homelab environment following modern IaC practices with Pulumi and Kubernetes. The project uses Python and uv for dependency management.

## Prerequisites

- [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/)
- [Python 3.13 or later](https://www.python.org/downloads/)
- [uv](https://pypi.org/project/uv/) (for dependency management)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Git](https://git-scm.com/downloads)

## Project Structure

```
homelab-IAC/
├── pulumi/
│   ├── stacks/
│   │   ├── homelab-dev.ts    # Development environment stack
│   │   └── homelab-prod.ts   # Production environment stack
│   └── ...                 # Other Pulumi configuration files
├── kubernetes/              # Kubernetes manifests
│   ├── ...                # Kubernetes deployment files
├── docs/                    # Project documentation
├── hello.py                 # Sample Python script
└── pyproject.toml           # Project configuration and dependencies
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/SPRIME01/homelab-iac.git
   cd homelab-iac
   ```

2. Install Python dependencies using uv:
   ```bash
   uv install
   ```

3. Initialize Pulumi stack:
   ```bash
   cd pulumi
   pulumi stack init dev
   ```

4. Configure your environment:
   ```bash
   pulumi config set kubernetes:context your-context-name
   ```

5. Deploy the infrastructure:
   ```bash
   pulumi up
   ```

## Environment Management

- Development: `pulumi stack select dev`
- Production: `pulumi stack select prod`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - See [LICENSE](LICENSE) file for details

## Maintenance

- **Owner**: SPRIME01
- **Last Updated**: February 2025
