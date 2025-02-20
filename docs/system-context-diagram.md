```markdown
@startuml HomelabContext
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

' Define Persons and External Actors
Person(admin, "Admin", "Home lab administrator", "Manages, monitors, and updates the homelab services")
Person(user, "Home User", "Local user", "Interacts with home automation and computing services")
Person(remoteUser, "Remote User", "Remote user", "Accesses homelab services via secure tunnels")

System_Ext(cloudflare, "Cloudflare", "External DNS and Tunneling Service", "Provides external DNS management and secure connectivity")

' Define the Homelab System Boundary and Inside Systems
System_Boundary(homelab, "Homelab Environment") {
    System(beelink, "Primary Control Node (Beelink SEi8)",
        "Hosts WSL2 with k3s control plane, Pulumi, Ansible, and core containerized services (Traefik, Authelia, RabbitMQ, Loki, VaultWarden, databases, etc.)")
    System(jetson, "AI/ML Node (Jetson AGX Orin)",
        "A dedicated GPU node running AI/ML workloads including NVIDIA Triton Inference Server and Ray workers")
    System(ha, "Home Automation Hub (Home Assistant Yellow)",
        "Manages home automation tasks, integrating via MQTT (and Zigbee2MQTT) to control smart devices")
    System(monitor, "Monitoring Device (Surface Pro 6)",
        "Provides dashboards and remote management (Grafana, remote desktop) for overall system health")
    System(router, "Local DNS Router (GL.i.Net AX1800 with AdGuard Home)",
        "Acts as the primary local DNS server to override client DNS settings, integrates Tailscale for remote connectivity and routes traffic internally")
    System(deepconnect, "Deep Connect DPN",
        "Sits between the modem and router, managing smart external routing and acting as an additional external security gateway")
}

' Relationships between People/External Systems and Homelab Components
Rel(admin, beelink, "Manages & updates services via Ansible/Pulumi", "SSH / HTTP API")
Rel(user, ha, "Interacts with home automation via web UI & MQTT", "Web / MQTT")
Rel(user, monitor, "Views dashboards & system health", "Remote Desktop / Web UI")
Rel(remoteUser, cloudflare, "Accesses homelab services securely", "VPN / Tunnel")
Rel(cloudflare, router, "Routes external requests into the homelab", "DNS over HTTPS, SSL/TLS")

' Relationships among Homelab Components
Rel(router, beelink, "Routes DNS and external traffic (via Traefik)", "DNS / HTTP")
Rel(router, jetson, "Directs requests for AI/ML services", "DNS")
Rel(router, ha, "Routes requests to home automation services", "DNS")
Rel(router, monitor, "Routes monitoring traffic", "HTTP/S")
Rel(deepconnect, router, "Provides smart external routing and failover", "Network routing")
Rel(beelink, jetson, "Coordinates task scheduling and internal APIs", "HTTP API / MQTT")
Rel(beelink, ha, "Integrates home automation data (via MQTT)", "MQTT")
Rel(beelink, monitor, "Forwards logs and metrics", "HTTP/S API")
@enduml
```
