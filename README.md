# get_vsix_download_url
Extracts the publisher name, extension name, and version from a Visual Studio Code Marketplace extension URL and constructs the direct download URL for the .vsix file

## How It Works

### Input: 
The script takes a Visual Studio Code Marketplace URL as input (e.g., https://marketplace.visualstudio.com/items?itemName=GitHub.copilot).
### Parsing:
Extracts the itemName (e.g., GitHub.copilot) from the URL query or path.
Splits itemName into publisher (e.g., GitHub) and extension_name (e.g., copilot).
### Version Extraction:
Fetches the extension’s Marketplace page.
Uses a regular expression to find the version number (e.g., 1.2.3) in the page’s HTML, typically in a JSON-LD or meta tag.
### Download:
paste the URL in your browser or wget it to download it
### Post-download:
You will need to rename the file download to have filename extension suffix '.vsix'. Then go to:
VScodium > Extensions > ... (settings) > Install from VSIX > [select downloaded file]