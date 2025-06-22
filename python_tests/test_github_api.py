import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('GITHUB_TOKEN')  
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def test_search_repos():
    """Test GitHub's repository search endpoint"""
    url = "https://api.github.com/search/repositories?q=python&per_page=5"
    response = requests.get(url, headers=HEADERS)
    
    assert response.status_code == 200, f"Error: {response.status_code}"
    assert "items" in response.json(), "Response missing 'items' key"
    print("Search repositories test passed!")

def test_list_commits():
    """Test GitHub's commit listing endpoint"""
    url = "https://api.github.com/repos/torvalds/linux/commits?per_page=5"
    response = requests.get(url, headers=HEADERS)
    
    assert response.status_code == 200
    assert isinstance(response.json(), list), "Commits should be a list"
    print("List commits test passed!")

if __name__ == "__main__":
    test_search_repos()
    test_list_commits()
