@startuml
' Include the C4-PlantUML Container definitions
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

' Define the boundary for the Homelab system
System_Boundary(homelab, "Homelab System") {
    ' --- Primary Control Node (Beelink SEi8) Containers ---
    Container(k3s, "K3s Control Plane", "Kubernetes",
        "Orchestrates container scheduling and cluster management. Deployed on Beelink SEi8 (WSL2 + Ubuntu with Flannel).")
    Container(traefik, "Traefik Ingress Controller", "Traefik",
        "Routes inbound traffic, handles TLS termination and ingress management. Deployed within the k3s cluster.")
    Container(authelia, "Authelia", "Authentication Service",
        "Provides multi-factor authentication and access control for external services.")
    Container(rabbit, "RabbitMQ", "Message Broker",
        "Enables asynchronous messaging and service integration.")
    Container(vault, "VaultWarden", "Secrets Manager",
        "Stores passwords, tokens, and other sensitive data securely.")
    Container(databases, "Database Services", "Various Database Engines",
        "Hosts multiple databases (DuckDB, MongoDB, Qdrant, etc.) for persistent storage.")
    Container(logs, "Loki Logging System", "Loki",
        "Aggregates and stores logs from all containerized services.")
    Container(promtail, "Promtail", "Log Collector",
        "Collects and forwards log data from nodes to the Loki logging system.")
    Container(automation, "Pulumi & Ansible", "Automation Tools",
        "Manages infrastructure-as-code deployments and configuration management across the homelab.")

    ' --- AI/ML Node (Jetson AGX Orin) Containers ---
    Container(triton, "NVIDIA Triton Inference Server", "Triton",
        "Delivers AI/ML inference services leveraging GPU acceleration. Deployed on Jetson AGX Orin.")
    Container(ray, "Ray Worker", "Ray",
        "Executes distributed machine learning workloads. Deployed on the Jetson AGX Orin as a K3s worker node.")

    ' --- Home Automation and Monitoring Containers ---
    Container(homeassistant, "Home Assistant", "Home Assistant",
        "Handles home automation tasks and integrates smart devices via MQTT. Deployed on the Home Assistant Yellow hub.")
    Container(grafana, "Grafana Monitoring", "Grafana",
        "Provides dashboards and displays metrics for system health. Deployed on the Surface Pro 6.")

    ' --- Networking & DNS ---
    Container(adguard, "AdGuard Home", "AdGuard Home",
        "Acts as the local DNS and ad blocking service that overrides client DNS settings. Deployed on the GL.i.Net AX1800 router.")
}

' --- Relationships between Containers ---
' Automation tools deploy and manage configurations across the cluster.
Rel(automation, k3s, "Deploys configuration to", "Pulumi/Ansible")
Rel(automation, traefik, "Updates via Helm charts", "Pulumi")

' Traefik routes external requests to backend services.
Rel(traefik, authelia, "Routes auth requests to", "HTTP/HTTPS")
Rel(traefik, rabbit, "Forwards API calls & service traffic", "HTTP/HTTPS")
Rel(traefik, grafana, "Routes traffic for monitoring", "HTTP/HTTPS")

' Authentication and messaging.
Rel(authelia, k3s, "Secures API access for services", "HTTP/S")
Rel(rabbit, homeassistant, "Exchanges MQTT messages with", "MQTT")
Rel(homeassistant, rabbit, "Publishes sensor data via", "MQTT")

' Scheduling workloads on the cluster.
Rel(k3s, triton, "Schedules AI workloads on", "Kubernetes scheduling")
Rel(k3s, ray, "Deploys distributed ML tasks on", "Kubernetes scheduling")

' Logging collection.
Rel(promtail, logs, "Forwards log streams to", "Log streaming")

' DNS resolution for internal services.
Rel(adguard, traefik, "Resolves domain names for", "DNS queries")
@enduml

This diagram represents the key containerized components of your homelab along with their
responsibilities and relationships: • Primary Control Node (Beelink SEi8):
– Hosts the K3s control plane and core services such as Traefik, Authelia, RabbitMQ,
VaultWarden, databases, and logging (Loki/Promtail).
– Automation via Pulumi and Ansible manages these deployments. • AI/ML Node (Jetson
AGX Orin):
– Runs GPU-intensive services like NVIDIA Triton Inference Server and distributed
computing via Ray workers. • Home Automation & Monitoring:
– Home Assistant handles smart home tasks and MQTT integration, while Grafana
provides dashboards for system health. • Networking & DNS:
– AdGuard Home on your router provides local DNS resolution and ad blocking, ensuring
internal traffic is properly routed (e.g., to Traefik). Feel free to adjust labels or add additional
details as your homelab evolve
