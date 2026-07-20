from unittest.mock import Mock, patch
import pytest
from src.llm.openai_client import OpenAIClient

def test_detect_action_returns_valid_action():
    """
    Test that a valid OpenAI response is returned correctly.
    """

    client = OpenAIClient()

    mock_response = Mock()
    mock_response.output_text = "top_products"

    with patch.object(client.client.responses, "create", return_value=mock_response,):
        result = client.detect_action("What are the top products?")

    assert result == "top_products"

def test_detect_action_returns_unknown_for_invalid_action():
    """
    Test that invalid OpenAI responses are converted to unknown.
    """

    client = OpenAIClient()

    mock_response = Mock()
    mock_response.output_text = "invalid_action"

    with patch.object(client.client.responses, "create", return_value=mock_response):
        result = client.detect_action("Do something random")

    assert result == "unknown"

def test_detect_action_handles_openai_failure():
    """
    Test OpenAI API failure handling.
    """

    client = OpenAIClient()

    with patch.object(client.client.responses, "create", side_effect=Exception("API error")):
        with pytest.raises(RuntimeError):
            client.detect_action("Show monthly revenue")