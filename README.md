GitHub API Postman Test Assignment

Overview
Tested 3 GitHub API endpoints using Postman for a job assignment.

Endpoints Tested
1. `GET /search/repositories` - Search public repos
2. `GET /repos/{owner}/{repo}/commits` - Get commit history
3. `GET /repos/{owner}/{repo}/contents` - List repo files

How to Run
1. Import the `.json` file into Postman
2. Set variables:
   - `base_url`: `https://api.github.com`
   - `token`: [Your GitHub PAT](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

Troubleshooting 
| Error | Solution |
|-------|----------|
| 401 Unauthorized | 1. Check token is valid<br> 2. Make sure token has `repo` permissions |
| 403 Rate Limit | Wait 1 hour or [check limits](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting) |
| 404 Not Found | Double-check repository name (e.g., `torvalds/linux`) |

Files
- `Postman_Collection/`: Contains all API tests
