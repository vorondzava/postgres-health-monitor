import pytest

from config import get_connection_usage_critical, get_connection_usage_thresholds, get_connection_usage_warning
from report import get_monitor_status


def test_monitor_status_ok():
    result = get_monitor_status([],50,80,90)
    assert result["status"] == "OK"

def test_monitor_status_warning_for_long_queries():
    result = get_monitor_status(["slow query"],50,80,90)
    assert result["status"] == "WARNING"
    assert result["reasons"] == ["Long-running queries detected"]

def test_monitor_status_critical_connections():
    result = get_monitor_status([],90,80,90)
    assert result["status"] == "CRITICAL"
    assert result["reasons"] == ["Connection usage is critically high"]

def test_monitor_status_warning_connections():
    result = get_monitor_status([],80,80,90)
    assert result["status"] == "WARNING"
    assert result["reasons"] == ["Connection usage is high"]

def test_monitor_status_critical_with_long_queries():
    result = get_monitor_status(["slow query"], 90, 80, 90)
    assert result["status"] == "CRITICAL"
    assert result["reasons"] == ["Long-running queries detected","Connection usage is critically high"]

def test_monitor_status_ok_below_warning_threshold(): 
    result = get_monitor_status([],79,80,90)
    assert result["status"] == "OK"
    assert result["reasons"] == []

def test_monitor_status_warning_below_critical_threshold():
    result = get_monitor_status([],89,80,90)
    assert result["status"] == "WARNING"
    assert result["reasons"] == ["Connection usage is high"]

def test_get_connection_usage_thresholds_valid_values():
    result = get_connection_usage_thresholds(80,90)
    assert result == (80,90)

def test_get_connection_usage_thresholds_warning_greater_than_critical():
    with pytest.raises(ValueError):
        get_connection_usage_thresholds(90,80)

def test_get_connection_usage_thresholds_equal_values():
    with pytest.raises(ValueError):
        get_connection_usage_thresholds(80,80)

def test_get_connection_usage_warning_default_value(monkeypatch):
    monkeypatch.delenv("CONNECTION_USAGE_WARNING", raising=False)
    result = get_connection_usage_warning()
    assert result == 80

def test_get_connection_usage_warning_custom_value(monkeypatch):
    monkeypatch.setenv("CONNECTION_USAGE_WARNING", "75")
    result = get_connection_usage_warning()
    assert result == 75

def test_get_connection_usage_critical_default_value(monkeypatch):
    monkeypatch.delenv("CONNECTION_USAGE_CRITICAL", raising=False)
    result = get_connection_usage_critical()
    assert result == 90

def test_get_connection_usage_critical_custom_value(monkeypatch):
    monkeypatch.setenv("CONNECTION_USAGE_CRITICAL", "95")
    result = get_connection_usage_critical()
    assert result == 95