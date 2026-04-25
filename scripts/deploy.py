import os
import yaml
import subprocess

def deploy_to_environment(env):
    with open('configs/config.yaml') as f:
        config = yaml.safe_load(f)

    env_config = config['environments'][env]
    os.environ['DATABRICKS_HOST'] = env_config['databricks_host']
    os.environ['DATABRICKS_TOKEN'] = env_config['databricks_token']

    # Deploy using Databricks CLI
    subprocess.run(['databricks', 'workspace', 'import-dir', 'notebooks', f'/Shared/Banking-Platform-{env}', '--overwrite'])
    subprocess.run(['databricks', 'jobs', 'create', '--json-file', 'databricks-job.json'])

if __name__ == "__main__":
    import sys
    env = sys.argv[1] if len(sys.argv) > 1 else 'dev'
    deploy_to_environment(env)