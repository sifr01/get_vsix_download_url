import re
import requests
from urllib.parse import urlparse

def get_vsix_download_url(marketplace_url):
    """
    Generate the VSIX download URL for a VS Code extension given its Marketplace URL.
    
    Args:
        marketplace_url (str): The URL of the extension on the VS Code Marketplace.
        
    Returns:
        str: The direct download URL for the .vsix file, or None if extraction fails.
    """
    try:
        # Example URL: https://marketplace.visualstudio.com/items?itemName=GitHub.copilot
        # Parse the URL to extract the itemName parameter
        parsed_url = urlparse(marketplace_url)
        if parsed_url.netloc != 'marketplace.visualstudio.com':
            print("Error: URL must be from marketplace.visualstudio.com")
            return None

        # Extract itemName from query or path
        item_name = None
        if 'items' in parsed_url.path:
            item_name = parsed_url.query.split('itemName=')[-1] if 'itemName=' in parsed_url.query else parsed_url.path.split('/')[-1]
        
        if not item_name:
            print("Error: Could not extract itemName from URL")
            return None

        # itemName format: publisher.extensionName
        publisher, extension_name = item_name.split('.', 1)
        
        # Fetch the extension page to get the latest version
        response = requests.get(marketplace_url)
        if response.status_code != 200:
            print(f"Error: Failed to fetch page, status code {response.status_code}")
            return None

        # Look for version in the page content (meta tag or JSON-LD)
        version_pattern = r'"version"\s*:\s*"(\d+\.\d+\.\d+)"'
        match = re.search(version_pattern, response.text)
        if not match:
            print("Error: Could not find version in page")
            return None
        
        version = match.group(1)
        
        # Construct the VSIX download URL
        vsix_url = (
            f"https://{publisher}.gallery.vsassets.io/_apis/public/gallery/publisher/"
            f"{publisher}/extension/{extension_name}/{version}/assetbyname/"
            f"Microsoft.VisualStudio.Services.VSIXPackage"
        )
        
        return vsix_url
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def main():
    # Example usage
    marketplace_url = input("Enter the VS Code Marketplace extension URL (e.g., https://marketplace.visualstudio.com/items?itemName=GitHub.copilot): ")
    download_url = get_vsix_download_url(marketplace_url)
    
    if download_url:
        print(f"VSIX Download URL: {download_url}")
    else:
        print("Failed to generate VSIX download URL.")

if __name__ == "__main__":
    main()