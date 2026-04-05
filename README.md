# cifi-demo

A demo repository for [CI Failure Intelligence (CIFI)](https://github.com/alihaidar2950/cifi).

This repo contains intentionally broken Python code. When the CI tests fail, CIFI automatically analyzes the failure using GitHub Models and posts a structured root cause analysis as a PR comment — no extra secrets required.

## What to expect

Open a pull request against `main` and watch the failing `test` job trigger CIFI, which will post a comment like:

> **🤖 CIFI — CI Failure Analysis**
> **Failure Type:** `test_failure` | **Confidence:** `high`
> ### Root Cause
> Off-by-one error in `add()` — the function returns `a + b + 1` instead of `a + b`...

## The intentional bug

```python
# math_utils.py
def add(a, b):
    return a + b + 1  # off-by-one bug
```

```python
# tests/test_math.py
def test_add_integers():
    assert add(2, 3) == 5  # returns 6 — FAIL
```

## CIFI setup used

```yaml
- name: Analyze failure with CIFI
  if: failure()
  uses: alihaidar2950/cifi@v1
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
```
# trigger fresh run
