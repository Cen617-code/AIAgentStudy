"""
日志处理工具模块 - Day 5 代码编写练习

提供日志格式化和过滤功能，用于处理日志文件或日志流。
"""


def format_log_level(level: str) -> str:
    """
    格式化日志级别为标准格式。

    Args:
        level: 用户输入的日志级别（不区分大小写）

    Returns:
        标准化的日志级别字符串

    Example:
        >>> format_log_level("warning")
        'WARN'
    """
    level_map = {
        "debug": "DEBUG",
        "info": "INFO",
        "warning": "WARN",
        "error": "ERROR",
        "critical": "CRITICAL",
    }
    return level_map.get(level.lower(), "INFO")


def parse_log_line(line: str) -> dict:
    """
    解析单行日志。

    日志格式应为: "timestamp - level - message"
    支持多级分隔符（如消息本身包含 " - "）

    Args:
        line: 日志行字符串

    Returns:
        包含 timestamp, level, message 的字典

    Example:
        >>> parse_log_line("2024-01-01 10:00:00 - INFO - Test message")
        {'timestamp': '2024-01-01 10:00:00', 'level': 'INFO', 'message': 'Test message'}
    """
    # 按 " - " 分隔符分割，限制分割次数为2，保留消息中的分隔符
    parts = line.strip().split(" - ", 2)
    if len(parts) >= 3:
        return {
            "timestamp": parts[0],
            "level": parts[1].upper(),
            "message": parts[2],
        }
    # 如果格式不标准，尝试简单解析 level
    upper_line = line.upper()
    for lvl in ["CRITICAL", "ERROR", "WARN", "WARNING", "INFO", "DEBUG"]:
        if lvl in upper_line:
            return {"timestamp": "", "level": lvl, "message": line}
    return {"timestamp": "", "level": "INFO", "message": line}


def filter_logs_by_level(logs: list[str], min_level: str) -> list[str]:
    """
    按最低级别过滤日志。

    Args:
        logs: 日志行列表
        min_level: 最低日志级别（包含此级别及更高级别）

    Returns:
        过滤后的日志列表

    Example:
        >>> logs = ["... - DEBUG - msg", "... - ERROR - msg"]
        >>> filter_logs_by_level(logs, "ERROR")
        ['... - ERROR - msg']
    """
    levels = ["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"]
    min_idx = levels.index(format_log_level(min_level))
    return [log for log in logs if levels.index(parse_log_line(log)["level"]) >= min_idx]


if __name__ == "__main__":
    # 测试
    test_logs = [
        "2024-01-01 10:00:00 - DEBUG - Debug message",
        "2024-01-01 10:01:00 - INFO - Info message",
        "2024-01-01 10:02:00 - ERROR - Error message",
    ]
    print("过滤前:", test_logs)
    print("WARN级别及以上:", filter_logs_by_level(test_logs, "WARN"))
