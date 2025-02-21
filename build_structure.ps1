# Set the root folder (assumes the script is executed from the root folder)
$root = Get-Location

# Function to create a file if it doesn't exist
function Ensure-File {
    param([string]$path)
    if (-not (Test-Path $path)) {
        New-Item -Path $path -ItemType File | Out-Null
        Write-Host "Created file: $path"
    } else {
        Write-Host "File exists, skipping: $path"
    }
}

# Function to create a folder if it doesn't exist
function Ensure-Folder {
    param([string]$path)
    if (-not (Test-Path $path)) {
        New-Item -Path $path -ItemType Directory | Out-Null
        Write-Host "Created folder: $path"
    } else {
        Write-Host "Folder exists, skipping: $path"
    }
}

# Create files at the root level
Ensure-File "$root\README.md"
Ensure-File "$root\.gitignore"
Ensure-File "$root\.env"
Ensure-File "$root\PROJECT_STRUCTURE.md"

# Create Pulumi directory structure
Ensure-Folder "$root\pulumi"
Ensure-File "$root\pulumi\Pulumi.yaml"
Ensure-File "$root\pulumi\Pulumi.dev.yaml"
Ensure-File "$root\pulumi\index.ts"
Ensure-Folder "$root\pulumi\stacks"
Ensure-File "$root\pulumi\stacks\homelab-dev.ts"
Ensure-File "$root\pulumi\stacks\homelab-prod.ts"

# Create Kubernetes directory structure
Ensure-Folder "$root\kubernetes"
Ensure-Folder "$root\kubernetes\deployments"
Ensure-File "$root\kubernetes\deployments\authelia.yaml"
Ensure-File "$root\kubernetes\deployments\traefik.yaml"
Ensure-Folder "$root\kubernetes\services"
Ensure-File "$root\kubernetes\services\rabbitmq.yaml"
Ensure-File "$root\kubernetes\services\heimdall.yaml"
Ensure-Folder "$root\kubernetes\ingress"
Ensure-File "$root\kubernetes\ingress\traefik-ingress.yaml"

# Create Helm directory structure
Ensure-Folder "$root\helm"
# Helm for Traefik
Ensure-Folder "$root\helm\traefik"
Ensure-File "$root\helm\traefik\Chart.yaml"
Ensure-File "$root\helm\traefik\values.yaml"
Ensure-Folder "$root\helm\traefik\templates"
Ensure-File "$root\helm\traefik\templates\deployment.yaml"
# Helm for Authelia
Ensure-Folder "$root\helm\authelia"
Ensure-File "$root\helm\authelia\Chart.yaml"
Ensure-File "$root\helm\authelia\values.yaml"
Ensure-Folder "$root\helm\authelia\templates"
Ensure-File "$root\helm\authelia\templates\deployment.yaml"

Write-Host "Structure build complete."
