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

def test_rate_limits():
    """Test GitHub rate limit awareness"""
    url = f"{BASE_URL}/rate_limit"
    response = requests.get(url, headers=HEADERS)
    
    assert response.status_code == 200
    limits = response.json()["resources"]["core"]
    print(f"Rate limits: {limits['remaining']}/{limits['limit']} remaining")
    assert limits['remaining'] > 0, "Rate limit exceeded"

def test_pagination():
    """Test pagination handling"""
    for page in range(1, 3):  # Test first 2 pages
        url = f"{BASE_URL}/search/repositories?q=python&page={page}&per_page=5"
        response = requests.get(url, headers=HEADERS)
        
        assert response.status_code == 200
        assert len(response.json()["items"]) > 0
        print(f"Page {page} pagination test passed")

def test_403_forbidden():
    """Test handling of rate limits/insufficient permissions"""
    try:
        # Try accessing a protected endpoint with insufficient scopes
        url = f"{BASE_URL}/user/emails"  # Requires user:email scope
        response = requests.get(url, headers=HEADERS)
        
        if response.status_code == 403:
            print("✓ Got expected 403 Forbidden (needs token with user:email scope)")
        else:
            print(f"Got {response.status_code} instead of 403")
            
    except Exception as e:
        print(f"403 test failed: {str(e)}")

def test_404_not_found():
    """Test handling of non-existent resources"""
    try:
        url = f"{BASE_URL}/repos/nonexistentowner/nonexistentrepo"
        response = requests.get(url, headers=HEADERS)
        
        assert response.status_code == 404
        assert "Not Found" in response.json()["message"]
        print("✓ 404 Not Found test passed")
        
    except Exception as e:
        print(f"404 test failed: {str(e)}")

def test_422_validation():
    """Test handling of invalid parameters"""
    try:
        url = f"{BASE_URL}/search/repositories?per_page=0"  # Invalid value
        response = requests.get(url, headers=HEADERS)
        
        assert response.status_code == 422
        print("✓ 422 Validation test passed")
        
    except Exception as e:
        print(f"422 test failed: {str(e)}")

if __name__ == "__main__":
    test_search_repos()
    test_list_commits()
    test_get_contents()
    test_rate_limits()   
    test_pagination() 
    test_403_forbidden()  
    test_404_not_found()  
    test_422_validation()  