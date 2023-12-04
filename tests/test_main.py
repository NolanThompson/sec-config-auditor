import threading
import time
import sys
from io import StringIO
from unittest.mock import patch
import main
from main import loading_spinner

def test_loading_spinner_output():
    """
    Test to ensure the loading spinner prints the correct characters.
    """
    stop_flag = threading.Event()
    output = StringIO()
    
    with patch('sys.stdout', new=output):
        spinner_thread = threading.Thread(target=loading_spinner, args=(stop_flag,))
        spinner_thread.start()
        time.sleep(0.5)  # Allow some time for the spinner to run
        stop_flag.set()
        spinner_thread.join()

    output_value = output.getvalue()
    assert '-' in output_value
    assert '\\' in output_value
    assert '|' in output_value
    assert '/' in output_value

@patch('main.get_analysis')
def test_get_analysis_called(mock_get_analysis):
    """
    Test to ensure get_analysis function is called within main's execution.
    """
    with patch('threading.Thread') as mock_thread:
        # Mocking threading.Thread to prevent actual thread creation
        main.main()  # Call the main function directly
        mock_get_analysis.assert_called_once()
        mock_thread.assert_called_once()  # Assert that a thread was initiated
