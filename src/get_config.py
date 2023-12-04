import boto3
import os

def get_org_config_summary():

    try:
        #fetch creds
        aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
        aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        aws_region = os.getenv('AWS_DEFAULT_REGION')

        aws_config_client = boto3.client('config', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

        #fetch response
        response = aws_config_client.describe_configuration_aggregators()

        #extract info
        config_aggregators = response.get('ConfigurationAggregators', [])

        org_summary = {
            'num_config_aggregators': len(config_aggregators),
            'config_aggregators': []
        }

        #collect aggregator info
        for aggregator in config_aggregators:
            aggregator_info = {
                'name': aggregator.get('ConfigurationAggregatorName', 'N/A'),
                'account_ids': aggregator.get('AccountAggregationSources', {}).get('AccountIds', []),
                'regions': aggregator.get('AccountAggregationSources', {}).get('AllAwsRegions', False)
            }
            org_summary['config_aggregators'].append(aggregator_info)

        return org_summary

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    org_config_summary = get_org_config_summary()

    #can edit to make payload more meaningful if needed
    if org_config_summary:
        print("Organization Configuration Summary:")
        print(f"Number of Config Aggregators: {org_config_summary['num_config_aggregators']}")
        
        for i, aggregator_info in enumerate(org_config_summary['config_aggregators'], start=1):
            print(f"\nConfig Aggregator {i}:")
            print(f"Name: {aggregator_info['name']}")
            print(f"Account IDs: {aggregator_info['account_ids']}")
            print(f"All AWS Regions: {aggregator_info['regions']}")
    else:
        print("Failed to retrieve organization configuration summary.")
