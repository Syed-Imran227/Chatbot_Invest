# 🔒 Security Setup Guide

## Setting Up Environment Variables

### Step 1: Create a `.env` file

In the `finance_advisor` directory, create a file named `.env` (copy from `env.example`):

```bash
# On Windows PowerShell
Copy-Item env.example .env

# On Linux/Mac
cp env.example .env
```

### Step 2: Add Your API Key

Open the `.env` file and add your actual API key:

```env
GEMINI_API_KEY=
```

### Step 3: Verify `.env` is Ignored

The `.env` file is already in `.gitignore`, so it won't be committed to Git. Verify this:

```bash
git status
```

You should NOT see `.env` in the list of files to be committed.

## For Local Development

1. **Create `.env` file** in `finance_advisor/` directory
2. **Add your variables** (see `env.example` for template)
3. **Run the server** - Django will automatically load the `.env` file

## For Render Deployment

1. Go to your Render dashboard
2. Select your web service
3. Go to **Environment** tab
4. Add environment variables:
   - `GEMINI_API_KEY` = `your-actual-api-key`
   - `GEMINI_MODEL` = `models/gemini-1.5-flash` (optional)
   - `DJANGO_SECRET_KEY` = `generate-a-secure-key`
   - `DJANGO_DEBUG` = `False`
   - `DJANGO_ALLOWED_HOSTS` = `your-app.onrender.com`

## Security Best Practices

✅ **DO:**
- Store API keys in environment variables
- Use `.env` files for local development
- Add `.env` to `.gitignore` (already done)
- Use different keys for development and production
- Rotate keys if they're ever exposed

❌ **DON'T:**
- Commit API keys to Git
- Hardcode keys in source code
- Share `.env` files
- Use production keys in development

## If Your Key Was Exposed

1. **Immediately regenerate** your Gemini API key in Google Cloud Console
2. **Check Git history** - if committed, remove it from history (use `git filter-branch` or BFG Repo-Cleaner)
3. **Update all environments** with the new key
4. **Monitor usage** for any unauthorized access

## Testing Your Setup

After setting up `.env`, test that it works:

```bash
python manage.py shell
>>> from django.conf import settings
>>> print(settings.GEMINI_API_KEY[:10])  # Should show first 10 chars, not empty
```

