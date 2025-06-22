GitHub API Postman Test Assignment

Overview
Goal: Test GitHub's API endpoints (`/search/repositories`, `/commits`, `/contents`) using Postman.
Tools Used: Postman, GitHub API.

Endpoints Tested
1. Search Repositories: `GET /search/repositories?q=python`
2. List Commits: `GET /repos/torvalds/linux/commits`
3. Get Contents: `GET /repos/torvalds/linux/contents`

Key Features
Authentication: Used GitHub Personal Access Token (PAT).
Pagination: Added `?page=1&per_page=5` to test multi-page results.
Error Handling: Validated status codes (200, 403, 404).

Files
- `Postman_Collection/GitHub_API_Test.postman_collection.json`: Exported Postman tests.

How to Run
1. Import the `.json` file into Postman.
2. Set environment variables:
   - `base_url`: `https://api.github.com`
   - `token`: Your GitHub PAT.

Links
- [GitHub API Docs](https://docs.github.com/en/rest)
