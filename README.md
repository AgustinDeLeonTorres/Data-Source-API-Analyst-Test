# GitHub API Testing Assignment
**Data Source API Analyst Evaluation**  

## Table of Contents
1. [Security Notice](#-security-notice)  
2. [Prerequisites](#-prerequisites)  
3. [Setup Instructions](#-setup-instructions)  
4. [API Endpoints Tested](#-api-endpoints-tested)  
5. [Error Handling](#-error-handling)  
6. [Troubleshooting Guide](#-troubleshooting-guide)  
7. [Repository Structure](#-repository-structure)  
8. [Project Reflection](#-project-reflection)  

---

1## 🔒 Security Notice
**Critical Requirements**:  
- All API requests require a valid GitHub Personal Access Token with `repo` scope  
- The `.gitignore` file excludes sensitive data - verify no tokens are committed  
- **If token exposure occurs**:  
  1. Immediately revoke at [GitHub Token Settings](https://github.com/settings/tokens)  
  2. Generate a new token with minimal required scopes  

**Best Practices**:  
✔️ Use Postman environment variables for token management  
✔️ Never hardcode credentials in test collections  

---

2## 📋 Prerequisites
- [Postman](https://www.postman.com/downloads/) installed
- [Python 3.8+](https://www.python.org/downloads/) (for Python tests)
- [VS Code](https://code.visualstudio.com/download) with Python extension (recommended)
- GitHub Personal Access Token with `repo` scope

**API Access**:  
- Create personal access token with `repo` scope:  
  ```plaintext
  Settings > Developer Settings > Personal Access Tokens
  
3🛠 Setup Instructions
Postman Configuration
Import Test Collection:

bash
git clone https://github.com/AgustinDeLeonTorres/Data-Source-API-Analyst-Test.git
Import Postman_Collection/GitHub_API_Test_v4.json

Configure Environment:
Variable	Sample Value	Description
base_url	https://api.github.com	API root endpoint
token	ghp_...	Your GitHub PAT
Execute Test Sequence:

Repository Search (/search/repositories)

Commit History (/repos/{owner}/{repo}/commits)

Content Listing (/repos/{owner}/{repo}/contents)

4🌐 API Endpoints Tested
Endpoint	Method	Test Parameters	Validation Criteria
/search/repositories	GET	q=language:python&sort=stars	Returns >=1 Python repo
/repos/{owner}/{repo}/commits	GET	per_page=30	Returns commit SHA list
/repos/{owner}/{repo}/contents	GET	path=/docs	Returns file metadata

5⚠️ Error Handling
Comprehensive error testing implemented:

HTTP Code	Test Scenario	Expected Result
400	Missing Auth Header	"message": "Bad credentials"
401	Invalid Token	401 Unauthorized
403	Rate Limit Exceeded	"message": "API rate limit exceeded"
404	Invalid Repository	"message": "Not Found"
422	Invalid Parameters	"message": "Validation Failed"

6🔧 Troubleshooting Guide

Authentication Issues
Symptom: 401 Unauthorized errors
✅ Resolution:
Verify token has repo scope
Check header format:
http
Authorization: Bearer {{token}}
Rate Limiting
Symptom: 403 Forbidden with rate limit message
✅ Resolution:
Check current limits:
bash
curl -H "Authorization: Bearer $TOKEN" https://api.github.com/rate_limit
Implement request throttling if needed
Data Validation
Symptom: 422 Unprocessable Entity
✅ Resolution:
Verify all parameters meet GitHub API requirements
Test with default values first

7 📁 Repository Structure
plaintext
Data-Source-API-Analyst-Test/
├── Postman_Collection/
│   └── GitHub_API_Test_v4.json    # Postman test suite
├── .gitignore                    # Excludes sensitive files
└── README.md                     # This documentation
📝 Project Reflection

8 Key Findings

GitHub's REST API requires precise header formatting
Pagination is mandatory for complete data retrieval
Rate limits vary by authentication status