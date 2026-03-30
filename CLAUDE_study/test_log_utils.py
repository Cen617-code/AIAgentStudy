"""
日志工具测试 - Day 5 单元测试练习
"""
import pytest
from log_utils import format_log_level, parse_log_line, filter_logs_by_level


class TestFormatLogLevel:
    """日志级别格式化测试"""

    def test_lowercase(self):
        assert format_log_level("info") == "INFO"

    def test_uppercase(self):
        assert format_log_level("ERROR") == "ERROR"

    def test_mixed_case(self):
        assert format_log_level("Warning") == "WARN"

    def test_invalid_level(self):
        assert format_log_level("unknown") == "INFO"


class TestParseLogLine:
    """日志解析测试"""

    def test_valid_log_line(self):
        result = parse_log_line("2024-01-01 10:00:00 - INFO - Test message")
        assert result["timestamp"] == "2024-01-01 10:00:00"
        assert result["level"] == "INFO"
        assert result["message"] == "Test message"

    def test_empty_line(self):
        result = parse_log_line("")
        assert result["level"] == "INFO"


class TestFilterLogsByLevel:
    """日志过滤测试"""

    def test_filter_warning(self):
        logs = [
            "2024-01-01 - DEBUG - msg",
            "2024-01-01 - INFO - msg",
            "2024-01-01 - ERROR - msg",
        ]
        result = filter_logs_by_level(logs, "WARNING")
        assert len(result) == 1
        assert "ERROR" in result[0]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
