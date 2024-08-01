import requests


def search_github_issues(label, state, language):
    url = "https://api.github.com/search/issues?"
    query = f'q=label:"{label}"+is:{state}+language:{language}'

    url = url + query

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None


if __name__ == "__main__":
    label = "good first issue"
    state = "open"
    language = "python"

    result = search_github_issues(label, state, language)

    if result:
        issues = result.get("items", [])
        for issue in issues:
            print(f"Title: {issue['title']}")
            print(f"URL: {issue['html_url']}")
            print(f"Repository: {issue['repository_url']}")
            print(f"Issue: {issue['body']}")
            print("-" * 80)
