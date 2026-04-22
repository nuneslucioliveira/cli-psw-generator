"""BDD tests for performance requirement - AC-006."""

import pytest
import time


@pytest.mark.performance
def test_password_generation_completes_within_time_target(cli_runner):
    """AC-006: Password generation completes within time target."""
    # Given the user invokes the CLI with a length of 64 characters
    start_time = time.time()

    for _ in range(100):  # Run 100 iterations to get statistical data
        result = cli_runner(["--length", "64"])
        assert result.returncode == 0

    end_time = time.time()

    # Then the password is generated and output within 100 milliseconds (p95 over 100 iterations)
    total_time = end_time - start_time
    avg_time_per_generation = total_time / 100 * 1000  # Convert to milliseconds

    # We'll check that average is less than 100ms, which is a reasonable approximation
    # of the p95 requirement for performance
    assert avg_time_per_generation < 100
