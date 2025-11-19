# Render Deployment Setup Guide

This guide explains how to configure automatic Render deployments via GitLab CI/CD using secure environment variables.

## Overview

The GitLab CI/CD pipeline is configured to automatically trigger a Render deployment when code is pushed to the `main` or `master` branch, after all tests pass successfully.

## Prerequisites

- A Render account with a deployed service
- Access to your GitLab project settings
- Your Render deploy hook URL

## Step 1: Get Your Render Deploy Hook Information

Your Render deploy hook URL looks like this:
```
https://api.render.com/deploy/srv-XXXXXXXXXXXXX?key=YYYYYYYYYYYY
```

From this URL, extract:
- **Service ID**: The part after `/deploy/` (e.g., `srv-d4epdr7gi27c73cre9ug`)
- **Deploy Key**: The part after `?key=` (e.g., `unoeEM6TPEQ`)

### How to Find Your Render Deploy Hook:

1. Go to your [Render Dashboard](https://dashboard.render.com/)
2. Select your service (e.g., "calculator-app")
3. Go to **Settings** tab
4. Scroll down to **Deploy Hook** section
5. Copy the deploy hook URL
6. Extract the Service ID and Deploy Key from the URL

## Step 2: Add Secrets to GitLab

### Option A: Using GitLab UI (Recommended)

1. Go to your GitLab project
2. Navigate to **Settings** → **CI/CD**
3. Expand the **Variables** section
4. Click **Add variable** and add the following:

#### Variable 1: RENDER_SERVICE_ID
- **Key**: `RENDER_SERVICE_ID`
- **Value**: `srv-d4epdr7gi27c73cre9ug` (your actual service ID)
- **Type**: Variable
- **Environment scope**: All (default)
- **Protect variable**: ✅ (recommended - only available to protected branches)
- **Mask variable**: ✅ (hides value in job logs)
- **Expand variable reference**: ❌

#### Variable 2: RENDER_DEPLOY_KEY
- **Key**: `RENDER_DEPLOY_KEY`
- **Value**: `unoeEM6TPEQ` (your actual deploy key)
- **Type**: Variable
- **Environment scope**: All (default)
- **Protect variable**: ✅ (recommended)
- **Mask variable**: ✅ (hides value in job logs)
- **Expand variable reference**: ❌

5. Click **Add variable** for each

### Option B: Using GitLab CLI

```bash
# Install glab CLI if not already installed
# macOS: brew install glab
# Linux: See https://gitlab.com/gitlab-org/cli

# Set variables
glab variable set RENDER_SERVICE_ID -v "srv-d4epdr7gi27c73cre9ug" --masked --protected
glab variable set RENDER_DEPLOY_KEY -v "unoeEM6TPEQ" --masked --protected
```

## Step 3: Verify Configuration

1. Push a commit to your `main` or `master` branch
2. Go to **CI/CD** → **Pipelines** in GitLab
3. Watch the pipeline run
4. The `deploy_render` job should trigger after tests pass
5. Check the job logs - you should see:
   ```
   Triggering Render deployment for service srv-XXXXX...
   ✅ Render deployment triggered successfully!
   ```

## Step 4: Verify Deployment on Render

1. Go to your [Render Dashboard](https://dashboard.render.com/)
2. Select your service
3. Check the **Events** tab - you should see a new deployment triggered by "Deploy Hook"

## Troubleshooting

### Error: "RENDER_SERVICE_ID and RENDER_DEPLOY_KEY must be set"

**Solution**: Make sure you've added both variables in GitLab CI/CD settings (see Step 2)

### Error: "Deployment failed with HTTP code: 401"

**Solution**: Your `RENDER_DEPLOY_KEY` is incorrect. Get the correct key from Render and update the GitLab variable.

### Error: "Deployment failed with HTTP code: 404"

**Solution**: Your `RENDER_SERVICE_ID` is incorrect. Verify the service ID from your Render deploy hook URL.

### Job doesn't run automatically

**Solution**: 
- Make sure you're pushing to `main` or `master` branch
- Check that tests are passing (deploy_render needs test and lint jobs to succeed)
- If using protected branches, ensure the variable has "Protect variable" enabled

## How It Works

```yaml
# Simplified workflow:
1. Code pushed to main/master
2. Test job runs ✓
3. Lint job runs ✓
4. Deploy job triggers:
   - Constructs URL: https://api.render.com/deploy/${RENDER_SERVICE_ID}?key=${RENDER_DEPLOY_KEY}
   - Makes GET request to Render API
   - Render pulls latest code and redeploys
   - Job reports success/failure
```

## Security Best Practices

✅ **DO:**
- Use masked variables for sensitive data
- Use protected variables for production deployments
- Regularly rotate your deploy keys
- Limit deploy hook to specific branches

❌ **DON'T:**
- Commit deploy hooks or keys to your repository
- Share deploy keys in plain text
- Use the same keys across multiple environments

## Manual Deployment Trigger

If you want to manually trigger a deployment without pushing code:

1. Go to **CI/CD** → **Pipelines**
2. Click **Run pipeline**
3. Select the branch (main/master)
4. Click **Run pipeline**

## Advanced Configuration

### Deploy to Different Render Services by Branch

You can set branch-specific variables:

1. Create multiple Render services (e.g., staging, production)
2. In GitLab, add variables with different environment scopes:
   - `RENDER_SERVICE_ID` with scope: `main` (production)
   - `RENDER_SERVICE_ID` with scope: `staging` (staging)

### Add Deployment Notifications

Update `.gitlab-ci.yml` to send notifications after deployment:

```yaml
after_script:
  - echo "Deployment completed. Check status at https://dashboard.render.com/"
  # Add Slack/Discord webhook notifications here
```

## Additional Resources

- [Render Deploy Hooks Documentation](https://render.com/docs/deploy-hooks)
- [GitLab CI/CD Variables Documentation](https://docs.gitlab.com/ee/ci/variables/)
- [GitLab Protected Branches](https://docs.gitlab.com/ee/user/project/protected_branches.html)

## Need Help?

If you encounter issues:
1. Check the GitLab pipeline logs
2. Check the Render deployment logs
3. Verify all variables are set correctly
4. Ensure the deploy hook is enabled in Render

---

**Last Updated**: November 2025

