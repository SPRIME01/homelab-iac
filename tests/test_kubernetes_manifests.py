import os
import pytest
import yaml
from unittest.mock import patch
from kubernetes.client import ApiClient, V1Deployment
from kubernetes.client.rest import ApiException
from kubernetes.config import load_kube_config

@pytest.fixture
def authelia_manifest():
    with open("kubernetes/deployments/authelia.yaml", "r") as file:
        return yaml.safe_load(file)

def test_authelia_manifest_validity(authelia_manifest):
    assert authelia_manifest["apiVersion"] == "apps/v1"
    assert authelia_manifest["kind"] == "Deployment"
    assert authelia_manifest["metadata"]["name"] == "authelia"
    assert authelia_manifest["spec"]["replicas"] == 1
    assert authelia_manifest["spec"]["selector"]["matchLabels"]["app"] == "authelia"
    assert authelia_manifest["spec"]["template"]["metadata"]["labels"]["app"] == "authelia"
    assert authelia_manifest["spec"]["template"]["spec"]["containers"][0]["name"] == "authelia"
    assert authelia_manifest["spec"]["template"]["spec"]["containers"][0]["image"] == "authelia:latest"
    assert authelia_manifest["spec"]["template"]["spec"]["containers"][0]["ports"][0]["containerPort"] == 80

@patch("kubernetes.client.AppsV1Api.create_namespaced_deployment")
def test_authelia_resource_creation(mock_create_deployment, authelia_manifest):
    load_kube_config()
    api_client = ApiClient()
    apps_v1_api = kubernetes.client.AppsV1Api(api_client)

    mock_create_deployment.return_value = V1Deployment(metadata={"name": "authelia"})

    try:
        apps_v1_api.create_namespaced_deployment(
            body=authelia_manifest,
            namespace="default"
        )
    except ApiException as e:
        pytest.fail(f"APIException when creating deployment: {e}")

    mock_create_deployment.assert_called_once()
    assert mock_create_deployment.call_args[1]["body"]["metadata"]["name"] == "authelia"
