import pytest
import requests
from services.web_crawler.subdomains_finder import get_subdomains, crawl_real_subdomains

@pytest.fixture
def mock_crtsh_response(monkeypatch):
    def mock_get(url, timeout=10):
        class MockResponse:
            def __init__(self):
                self.status_code = 200
            def json(self):
                return [
                    {"name_value": "www.example.com"},
                    {"name_value": "mail.example.com\nftp.example.com"}
                ]
        return MockResponse()
    
    monkeypatch.setattr(requests, "get", mock_get)

def test_get_subdomains_success(mock_crtsh_response):
    domain = "example.com"
    expected = sorted(["www.example.com", "mail.example.com", "ftp.example.com"])
    result = sorted(get_subdomains(domain))
    assert result == expected

def test_get_subdomains_failure(monkeypatch):
    def mock_get(*args, **kwargs):
        raise Exception("Network down")
    
    monkeypatch.setattr(requests, "get", mock_get)
    result = get_subdomains("example.com")
    assert result[0].startswith("Error:")

def test_crawl_real_subdomains(mock_crtsh_response):
    domains = ["example.com"]
    result = crawl_real_subdomains(domains)
    
    assert result["stage"] == "domain_asset_discovery"
    assert result["inputs"]["domains"] == domains
    assert "example.com" in result["discovered"]["subdomains"]
    assert "www.example.com" in result["discovered"]["subdomains"]["example.com"]