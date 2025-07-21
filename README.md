# GitHub Followers Grid

This repository automatically generates a beautiful grid display of your GitHub followers using GitHub Actions. The grid is updated daily and displays follower avatars in an organized table format.

## ✨ Features

- **Automatic Updates**: Daily updates via GitHub Actions
- **Beautiful Grid Layout**: Clean table format with follower avatars
- **README Integration**: Displays followers grid directly in README.md
- **Fast & Efficient**: Pagination support for users with many followers
- **Easy Setup**: Simple one-time configuration
- **Responsive Design**: Works on all devices

## Quick Setup

### 1. Fork this Repository
Click the "Fork" button at the top right of this page.

### 2. Enable GitHub Actions
1. Go to your forked repository
2. Click on the "Actions" tab
3. Click "I understand my workflows, go ahead and enable them"

### 3. Configure (Optional)
The workflow uses your repository owner's username by default. If you want to display a different user's followers, you can:

1. Go to your repository's **Settings** → **Secrets and variables** → **Actions**
2. Add a new repository secret:
   - Name: `TARGET_USERNAME`
   - Value: The GitHub username whose followers you want to display

### 4. Run the Workflow
1. Go to **Actions** tab
2. Click on "Update Followers Grid"
3. Click "Run workflow" → "Run workflow"

The followers grid will be generated and saved as `followers.html` in your repository, and the grid will also be automatically displayed in your README.md file.

## 📋 How It Works

1. **GitHub Actions Workflow**: Runs daily at 6 AM UTC (configurable)
2. **API Calls**: Fetches followers using GitHub API with pagination
3. **HTML Generation**: Creates a responsive grid layout
4. **README Update**: Automatically updates the README.md with the followers grid
5. **Auto-Commit**: Automatically commits and pushes the updated files

## 🔧 Configuration

### Workflow Schedule
To change the update frequency, edit `.github/workflows/update-followers.yml`:

```yaml
on:
  schedule:
    # Change this cron expression
    - cron: '0 6 * * *'  # Daily at 6 AM UTC
```

### Grid Columns
To change the number of columns in the grid, modify `scripts/generate_followers.py`:

```python
# Change the columns parameter (default is 6)
html = generate_html(followers, columns=8)
```

## 📁 Project Structure

```
github-followers-grid/
├── .github/
│   └── workflows/
│       └── update-followers.yml    # GitHub Actions workflow
├── scripts/
│   └── generate_followers.py       # Main Python script
├── followers.html                  # Generated followers grid
├── LICENSE
└── README.md
```

## 🔍 Generated Output

The script generates an HTML file with a responsive grid layout:

```html
<div align="center">
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/username" aria-label="username">
        <img src="avatar_url" width="50px" alt="username"/><br />
        <sub><b>username</b></sub>
      </a>
    </td>
    <!-- More followers... -->
  </tr>
</table>
</div>
```

## 🛠️ Local Development

### Prerequisites
- Python 3.7+
- `requests` library

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/github-followers-grid.git
   cd github-followers-grid
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

3. Set environment variables:
   ```bash
   export GITHUB_USERNAME="your-username"
   export GITHUB_TOKEN="your-github-token"
   ```

4. Run the script:
   ```bash
   python scripts/generate_followers.py
   ```

## 🔑 GitHub Token

The workflow uses the built-in `GITHUB_TOKEN` which has sufficient permissions for public repositories. For private repositories or higher rate limits, you can:

1. Create a Personal Access Token (PAT) with `read:user` scope
2. Add it as a repository secret named `GITHUB_TOKEN`

## 🚨 Troubleshooting

### Common Issues

**Script fails with "User not found"**
- Check if the username is correct
- Ensure the user's profile is public

**API rate limit exceeded**
- The script automatically handles rate limits
- For high-frequency updates, consider using a PAT

**Workflow not running**
- Ensure GitHub Actions are enabled
- Check if the repository is active (has recent commits)

**Empty followers.html**
- Check if the user has any followers
- Verify GitHub token permissions

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 My Followers

<!-- FOLLOWERS-GRID:START -->
<!-- This section will be automatically updated by GitHub Actions -->
<!-- FOLLOWERS-GRID:END -->

