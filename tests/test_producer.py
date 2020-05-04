import os

from py import test

from producer import MessageProducer
from util import extract_bootstrap_servers


def test_extract_boostrap_servers_has_multiple_returns_list():
    os.environ["BOOTSTRAP_SERVERS"] ="192.168.1.10:90902,192.168.1.11:1234,192.168.1.12:8282"

    servers = extract_bootstrap_servers()

    assert servers
    assert len(servers) == 3
    assert "192.168.1.10:90902" in servers
    assert "192.168.1.11:1234" in servers
    assert "192.168.1.12:8282" in servers


def test_extract_boostrap_servers_has_single_returns_list_with_one_element():
    os.environ["BOOTSTRAP_SERVERS"] ="192.168.1.10:90902"

    servers = extract_bootstrap_servers()

    assert servers
    assert len(servers) == 1
    assert "192.168.1.10:90902" in servers


def test_extract_bootstrap_servers_has_no_env_returns_localhost():
    del os.environ["BOOTSTRAP_SERVERS"]

    servers = extract_bootstrap_servers()

    assert servers
    assert len(servers) == 1
    assert "127.0.0.1:9092" in servers
