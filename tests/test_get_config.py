import os
from unittest.mock import patch, Mock
import pytest
from get_config import get_org_config_summary

def mock_boto3_client(*args, **kwargs):
    """
    Mock for boto3 client.
    """
    mock_client = Mock()
    mock_client.describe_configuration_aggregators.return_value = {
        'ConfigurationAggregators': [
            {
                'ConfigurationAggregatorName': 'Aggregator1',
                'AccountAggregationSources': {
                    'AccountIds': ['123456789012'],
                    'AllAwsRegions': True
                }
            }
        ]
    }
    return mock_client

@patch('boto3.client', new=mock_boto3_client)
@patch.dict(os.environ, {
    'AWS_ACCESS_KEY_ID': 'test_key_id',
    'AWS_SECRET_ACCESS_KEY': 'test_secret_access_key',
    'AWS_DEFAULT_REGION': 'us-east-1'
})
def test_get_org_config_summary_success():
    """
    Test to ensure get_org_config_summary fetches correct data from AWS.
    """
    result = get_org_config_summary()
    
    assert result is not None
    assert result['num_config_aggregators'] == 1
    assert result['config_aggregators'][0]['name'] == 'Aggregator1'
    assert result['config_aggregators'][0]['account_ids'] == ['123456789012']
    assert result['config_aggregators'][0]['regions'] is True

@patch('boto3.client', side_effect=Exception("Test Exception"))
@patch.dict(os.environ, {
    'AWS_ACCESS_KEY_ID': 'test_key_id',
    'AWS_SECRET_ACCESS_KEY': 'test_secret_access_key',
    'AWS_DEFAULT_REGION': 'us-east-1'
})
def test_get_org_config_summary_exception(mock_boto_client):
    """
    Test to handle exceptions in get_org_config_summary.
    """
    result = get_org_config_summary()
    assert result is None

def mock_azure_resource_management_client(*args, **kwargs):
    mock_client = Mock()
    mock_client.resource_groups.list.return_value = [
        Mock(name='ResourceGroup1'),
        Mock(name='ResourceGroup2')
    ]
    return mock_client


@patch('get_org_config_summary.DefaultAzureCredential')
@patch('get_org_config_summary.ResourceManagementClient', new=mock_azure_resource_management_client)
@patch.dict(os.environ, {
    'AZURE_SUBSCRIPTION_ID': 'test_subscription_id'
})
def test_get_org_config_summary_azure_success(mock_azure_credential):
    """
    Test to ensure get_org_config_summary fetches correct data from Azure.
    """
    result = get_org_config_summary('azure')

    assert result is not None
    assert result['num_resource_groups'] == 2
    assert result['resource_groups'] == ['ResourceGroup1', 'ResourceGroup2']


@patch('get_org_config_summary.DefaultAzureCredential')
@patch('get_org_config_summary.ResourceManagementClient', side_effect=Exception("Test Exception"))
@patch.dict(os.environ, {
    'AZURE_SUBSCRIPTION_ID': 'test_subscription_id'
})
def test_get_org_config_summary_azure_exception(mock_azure_credential):
    """
    Test to handle exceptions in get_org_config_summary for Azure.
    """
    result = get_org_config_summary('azure')
    assert result is None
