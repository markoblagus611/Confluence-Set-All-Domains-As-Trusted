# Confluence Data Center Migration - Bulk Set All Domains as Trusted

This script is designed to bulk set all domains as trusted while reviewing them in the context of a Confluence Data Center migration.

## How It Works

1. **Entering Your Confluence URL**: First, you need to enter the URL of your Confluence instance.

2. **Retrieving All Domains**: The script retrieves a list of all available domains for your Confluence site.

3. **Updating Domains**: It updates the decision for each domain, marking them as 'Trusted Domains.'

### Prerequisites

Before running this script, make sure you have the following:

- A compatible version of Confluence Data Center.
- Proper authentication credentials, including an access token.
