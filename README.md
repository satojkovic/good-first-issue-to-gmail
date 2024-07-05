# good-first-issue-to-gmail

### gh api

```shell
$ gh api -X GET search/issues -f 'q=label:"good first issue" lang:python is:open'
```

```shell
$ curl -H "Authorization: <PERSONAL ACCESS TOKEN>" \
    -H "Accept: application/vnd.github.v3+json \
    "https://api.github.com/search/issues?q=label:%22good%20first%20issue%22+lang:python+is:open"
```
