# Release Reset Guide

## Commands to Reset Repository State

```bash
git tag -d v1.0.0
git push origin --delete v1.0.0
```

## Manual Reset Steps

1. Delete the existing tag locally: `git tag -d v1.0.0`
2. Delete the tag from remote: `git push origin --delete v1.0.0`
3. Proceed with implementing the corrected workflow