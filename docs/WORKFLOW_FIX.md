# GitHub Actions Workflow Fix

## Issue
The GitHub Actions workflows were not properly preserving historical paper data in the `results` branch. This caused users to receive repeated lists of papers in their daily emails instead of only new papers.

## Root Cause
The workflows used `git checkout -B results` which **resets** the branch to the current HEAD (main branch) each time, effectively discarding all previous results branch history. Combined with `force: true` on push, this completely overwrote the remote results branch on every run.

## Solution
All three workflow files have been updated with a proper branching strategy:

### Changes Made
1. **Fetch existing results branch**: Added step to fetch the results branch from remote
2. **Conditional checkout**: Check if results branch exists and checkout if it does
3. **Merge strategy**: Merge main into results to get code updates while preserving logs
4. **Non-destructive branch creation**: Changed `git checkout -B results` to `git checkout -b results`
5. **No force push**: Changed `force: true` to `force: false`

### Workflow Files Updated
- `.github/workflows/daily-arxiv.yml` - Main daily workflow
- `.github/workflows/archive-old-papers.yml` - Monthly archiving
- `.github/workflows/update_paper_links.yml` - Weekly updates (currently disabled)

### How It Works Now

#### First Run (No results branch exists)
1. Checkout main branch
2. Attempt to fetch results branch (fails, as expected)
3. Stay on main branch
4. Run the script to generate papers
5. Create new results branch from main
6. Commit and push to results branch

#### Subsequent Runs (Results branch exists)
1. Checkout main branch
2. Fetch results branch from remote
3. Checkout results branch (preserves existing logs)
4. Merge main into results (gets code updates)
5. Run the script to update papers (FileManager merges new papers with existing)
6. Commit changes to results branch
7. Push to results branch (no force, preserves history)

### FileManager Integration
The `FileManager` class already implements proper merging logic:
```python
# In _update_existing_json_file
for keyword, papers in data.items():
    if keyword in json_data:
        json_data[keyword].update(papers)  # Merges new with existing
    else:
        json_data[keyword] = papers
```

This ensures that new papers are added to existing categories without removing old papers.

## Benefits
- ✅ Historical paper data is preserved
- ✅ Users only receive new papers in daily emails
- ✅ Code updates from main are still merged into results
- ✅ Complete commit history is maintained
- ✅ All papers remain searchable in the results branch

## Testing
A comprehensive test script was created to validate the workflow logic:
- First run creates results branch correctly
- Subsequent runs preserve existing data
- Code updates from main are merged correctly
- All historical papers are retained

## Migration Notes
When this fix is deployed:
1. If a results branch already exists but has been reset previously, it will be preserved going forward
2. The first run after deploying this fix will establish the proper branching structure
3. All subsequent runs will build upon the preserved history
