# Project Structure for Infrastructure‑as‑Code Repository

c:\Users\sprim\Focus Areas\Projects\Dev\homelab-IAC
│
├── README.md              // General project documentation
├── .gitignore             // Git ignore rules
├── .env                   // Environment variable file
├── PROJECT_STRUCTURE.md   // This file describes the repository layout
│
├── pulumi/                // Pulumi code for defining Kubernetes resources
│   ├── Pulumi.yaml
│   ├── Pulumi.dev.yaml     // Example stack configuration
│   ├── index.ts            // Main Pulumi program
│   └── stacks/             // Stack-specific variants (e.g., dev, prod)
│       ├── homelab-dev.ts
│       └── homelab-prod.ts
│
├── kubernetes/            // Kubernetes manifests
│   ├── deployments/       // Deployments for core services (e.g., authelia, traefik)
│   │   ├── authelia.yaml
│   │   └── traefik.yaml
│   │
│   ├── services/          // Service definitions (e.g., RabbitMQ, Heimdall)
│   │   ├── rabbitmq.yaml
│   │   └── heimdall.yaml
│   │
│   └── ingress/           // Ingress configuration (e.g., entry points for Traefik)
│       └── traefik-ingress.yaml
│
└── helm/                  // Helm charts for deployments
    ├── traefik/
    │   ├── Chart.yaml
    │   ├── values.yaml
    │   └── templates/
    │       └── deployment.yaml
    │
    └── authelia/
        ├── Chart.yaml
        ├── values.yaml
        └── templates/
            └── deployment.yaml
