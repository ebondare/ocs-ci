"""
Defaults module
"""
from getpass import getuser

INSTALLER_VERSION = '4.1.0-rc.3'
AWS_REGION = 'us-east-2'
ROOK_CLUSTER_NAMESPACE = 'openshift-storage'
KUBECONFIG_LOCATION = 'auth/kubeconfig'  # relative from cluster_dir
CLUSTER_NAME = f"ocs-ci-cluster-{getuser()}"
API_VERSION = "v1"
