1. **Infrastructure-as-Code Repository**
    - Store all Pulumi scripts, Kubernetes manifests, and Helm-related configurations here.
    - Organize this repository with environment-specific directories if needed. For example, if the Windows host and the WSL2 environment on your Beelink have significantly different configurations, you could have subdirectories (or even separate projects within the repository) for each.
    - .env         : Environment variables for local configurations.

<!-- Infrastructure‑as‑Code Project Structure -->
The Infrastructure‑as‑Code repository has the following layout:
- /pulumi          : Contains Pulumi scripts, configuration files (Pulumi.yaml, stacks, etc.).
- /kubernetes      : Stores Kubernetes manifests (deployments, services, ingress resources).
- /helm            : Contains Helm charts for deployed applications.
- README.md        : Overall project documentation.
- .gitignore       : Files and directories excluded from version control.

2. **Configuration Management Repository**
    - Store all Ansible playbooks and roles.
    - Organize playbooks by device/role and keep common roles centralized.
    - .env         : Environment variables (e.g., target inventory, credentials).

3. **Container Images Repository (Optional)**
    - Keep Dockerfiles and related scripts for custom image builds.
    - Organize by application or service.
    - .env         : Environment variables for build configurations.

4. **Monorepo vs. Multirepo for Beelink**
    - For the Beelink, if the Windows host and the WSL2 environment have different responsibilities (e.g., Docker Desktop/Pulumi on Windows vs. k3s/Traefik/Ansible on WSL2), you have two options:
      - Create two separate repositories—one for host-specific configurations and one for the Linux/WSL2 environment.
      - Or maintain a single repository with clear subdirectories (e.g., `/windows` and `/wsl2`) to reduce overhead while still delineating the environments.
