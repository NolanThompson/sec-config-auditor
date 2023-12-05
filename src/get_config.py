import boto3
import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient


def get_org_config_summary(cloud_provider):
    try:
        if cloud_provider == "aws":
            # AWS config
            aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
            aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
            aws_region = os.getenv('AWS_DEFAULT_REGION')

            aws_config_client = boto3.client('config', aws_access_key_id=aws_access_key_id,
                                             aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

            # fetch response
            response = aws_config_client.describe_configuration_aggregators()

            # extract info
            config_aggregators = response.get('ConfigurationAggregators', [])

            org_summary = {
                'num_config_aggregators': len(config_aggregators),
                'config_aggregators': []
            }

            # collect aggregator info
            for aggregator in config_aggregators:
                aggregator_info = {
                    'name': aggregator.get('ConfigurationAggregatorName', 'N/A'),
                    'account_ids': aggregator.get('AccountAggregationSources', {}).get('AccountIds', []),
                    'regions': aggregator.get('AccountAggregationSources', {}).get('AllAwsRegions', False)
                }
                org_summary['config_aggregators'].append(aggregator_info)

        elif cloud_provider == 'azure':
            # Azure config
            credential = DefaultAzureCredential()
            subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
            resource_client = ResourceManagementClient(credential, subscription_id)

            resource_groups = resource_client.resource_groups.list()

            cloud_summary = {
                'num_resource_groups': len(list(resource_groups)),
                'resource_groups': [rg.name for rg in resource_groups]
            }

        else:
            print("Invalid cloud provider specified.")
            return None
        return org_summary

    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    cloud_provider = 'aws'
    org_config_summary = get_org_config_summary(cloud_provider)

    # can edit to make payload more meaningful if needed
    if org_config_summary:
        print(f"{cloud_provider.capitalize()} Configuration Summary:")

        if cloud_provider == 'aws':
            print(f"Number of Config Aggregators: {org_config_summary['num_config_aggregators']}")

        for i, aggregator_info in enumerate(org_config_summary['config_aggregators'], start=1):
            print(f"\nConfig Aggregator {i}:")
            print(f"Name: {aggregator_info['name']}")
            print(f"Account IDs: {aggregator_info['account_ids']}")
            print(f"All AWS Regions: {aggregator_info['regions']}")

    elif cloud_provider == 'azure':
        print(f"Number of Resource Groups: {org_config_summary['num_resource_groups']}")
        print(f"Resource Groups: {org_config_summary['resource_groups']}")

    else:
        print("Failed to retrieve organization configuration summary.")
