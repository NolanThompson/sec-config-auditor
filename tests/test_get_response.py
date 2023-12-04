import os
from unittest.mock import patch, MagicMock
import pytest
from io import StringIO
from get_response import chat_completion, get_analysis

@pytest.fixture
def mock_openai_response():
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "Test response"
    return mock_response

@patch.dict('os.environ', {'CHATGPT_KEY': 'your_mocked_api_key'})
@patch('openai.ChatCompletion.create')
def test_chat_completion(mock_chat_create, mock_openai_response):
    """
    Test to ensure chat_completion returns a response.
    """
    mock_chat_create.return_value = mock_openai_response

    prompt = "Test prompt"
    response = chat_completion(prompt)

    mock_chat_create.assert_called_with(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    assert response == "Test response"

@patch('get_response.chat_completion')
@patch('get_response.get_org_config_summary')
def test_get_analysis(mock_get_config_summary, mock_chat_completion):
    """
    Test to ensure get_analysis correctly fetches and processes the config.
    """
    mock_get_config_summary.return_value = "Test config summary"
    mock_chat_completion.return_value = "Analysis response"

    with patch('sys.stdout', new_callable=StringIO) as fake_output:
        get_analysis()
        assert "Analysis response" in fake_output.getvalue()

    mock_chat_completion.assert_called_once()
    mock_get_config_summary.assert_called_once()
