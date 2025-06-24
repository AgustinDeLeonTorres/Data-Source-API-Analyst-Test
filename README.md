GitHub API Postman Test Assignment

Overview
Tested 3 GitHub API endpoints using Postman for a job assignment.

Prerequisites
Before running these tests, ensure you have:
- [Postman](https://www.postman.com/downloads/) installed
- [Python 3.8+](https://www.python.org/downloads/) (for Python tests)
- [VS Code](https://code.visualstudio.com/download) with Python extension (recommended)
- GitHub Personal Access Token with `repo` scope

Endpoints Tested
1. `GET /search/repositories` - Search public repos
2. `GET /repos/{owner}/{repo}/commits` - Get commit history  
3. `GET /repos/{owner}/{repo}/contents` - List repo files

How to Run

Postman Tests
1. **Install Postman** if not already installed
2. Import the collection:
   - Open Postman → Click "Import" → Select `GitHub_API_Test_v4.postman_collection.json`
3. Set environment variables:
   - `base_url`: `https://api.github.com`
    - `token`: Your [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) with `repo` scope

   *Note:* While this repo includes a `.env` file template and `.gitignore` for security,  
   **you must manually add your own token** in either:
   - Postman's environment variables, **OR**
   - A local `.env` file (not committed to Git)
4. Import the collection:
   ```bash
   git clone https://github.com/AgustinDeLeonTorres/Data-Source-API-Analyst-Test.git

Error Handling Tests (Recruiter Requirement)
All error tests are implemented in Postman:

| Error Code | Test Case | Validation |
|------------|----------|------------|
| 400 | Missing Authorization Header | Verify error message |
| 401 | Invalid Token | Check "Bad credentials" response |
| 403 | Rate Limit Exceeded | Monitor X-RateLimit headers |
| 404 | Non-existent Repository | Validate "Not Found" message |
| 422 | Invalid Parameters | Test pagination bounds |

Troubleshooting Guide
Common Issues (As Required by Recruiter)

401 Unauthorized Error
1. **Check Authentication**:
   - Verify your `AUTH_TOKEN` is active and valid
   - Ensure token has `repo` permissions in [GitHub Settings](https://github.com/settings/tokens)
   
2. **Environment Variables**:
   - Confirm `base_url` is set to `https://api.github.com`
   - Verify the token is correctly referenced as `{{token}}` in Postman

3. **Rate Limits**:
   - Check remaining requests: `GET /rate_limit`
   - Implement auto-retry in tests when `X-RateLimit-Remaining` is low

Other Errors
| Error | Solution | Postman Test Included |
|-------|----------|-----------------------|
| 403 Forbidden | Wait 1 hour or upgrade token scope |  Yes |
| 404 Not Found | Verify repository/endpoint exists |  Yes |
| 422 Validation | Check parameter requirements | Yes (tests `per_page=0`) |