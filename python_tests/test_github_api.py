import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")  
BASE_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",  
    "Accept": "application/vnd.github.v3+json" 
}

def test_search_repos():
    """Test GitHub's repository search endpoint"""
    try:
        url = f"{BASE_URL}/search/repositories?q=python&per_page=5"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  
        
        assert "items" in response.json(), "Missing 'items' key"
        print("Search repositories test passed!")
        
    except Exception as e:
        print(f"Search failed: {str(e)}")

def test_list_commits():  
    """Test GitHub's commit listing endpoint"""
    try:
        url = f"{BASE_URL}/repos/torvalds/linux/commits?per_page=5" 
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        
        assert isinstance(response.json(), list)
        print("List commits test passed!")
        
    except Exception as e:
        print(f"Commits failed: {str(e)}")

def test_get_contents():
    """Test GitHub's repo contents endpoint"""
    try:
        url = f"{BASE_URL}/repos/torvalds/linux/contents"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        
        assert isinstance(response.json(), list)
        print("Get contents test passed!")
        
    except Exception as e:
        print(f"Contents failed: {str(e)}")

if __name__ == "__main__":
    test_search_repos()
    test_list_commits()
    test_get_contents()