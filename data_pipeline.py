import os
from typing import List

import html2text
from requests_html import HTMLSession


def download_and_save_in_markdown(url: str, dir_path: str) -> None:
    """Download the HTML content from the web page and save it as a markdown file."""
    # Extract a filename from the URL
    if url.endswith("/"):
        url = url[:-1]

    filename = url.split("/")[-1] + ".md"
    print(f"Downloading {url} into {filename}...")

    session = HTMLSession()
    response = session.get(url, timeout=30)

    # Render the page, which will execute JavaScript
    response.html.render()

    # Convert the rendered HTML content to markdown
    h = html2text.HTML2Text()
    markdown_content = h.handle(response.html.raw_html.decode("utf-8"))

    # Write the markdown content to a file
    filename = os.path.join(dir_path, filename)
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(markdown_content)


def download(pages: List[str]) -> str:
    """Download the HTML content from the pages and save them as markdown files."""
    # Create the content/notion directory if it doesn't exist
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(base_dir, ".content", "blogs")
    os.makedirs(dir_path, exist_ok=True)
    for page in pages:
        download_and_save_in_markdown(page, dir_path)
    return dir_path


PAGES = [
    "https://www.cokeconsolidated.com/2023/11/21/baltimore-ravens-and-coca-cola-consolidated-team-up-for-tree-planting-event/"
    ,"https://www.cokeconsolidated.com/2023/11/15/boy-scout-exemplifies-commitment-to-environment-on-america-recycles-day/"
    ,"https://www.cokeconsolidated.com/2023/04/10/rain-barrel-workshop-aims-to-increase-rainwater-collection-in-columbus/"
    ,"https://www.cokeconsolidated.com/2023/04/08/coca-cola-consolidated-and-kroger-to-close-the-loop-at-the-2023-kentucky-derby/"
    ,"https://www.cokeconsolidated.com/2023/03/31/cleaning-up-nashvilles-waterways/"
    ,"https://www.cokeconsolidated.com/2023/03/23/coca-cola-consolidated-and-the-washington-wizards-plant-25-trees/"
    ,"https://www.cokeconsolidated.com/2022/12/13/coca-cola-consolidated-teams-up-with-indiana-university-to-prevent-unrecycled-plastic-waste/"
    ,"https://www.cokeconsolidated.com/2022/11/21/closing-the-loop-at-nissan-stadium/"
    ,"https://www.cokeconsolidated.com/2022/10/18/coca-cola-consolidated-commits-to-better-buildings-better-plants-challenge/"
    ,"https://www.cokeconsolidated.com/2022/04/09/coca-cola-consolidated-and-giant-food-partner-with-local-organizations-to-cleanup-oxon-run/"
    ,"https://www.cokeconsolidated.com/2021/05/28/closing-the-loop-at-the-coca-cola-600-2/"
    ,"https://www.cokeconsolidated.com/2021/04/21/coca-cola-consolidated-implements-closed-loop-recycling-at-rbc-heritage/"
]

if __name__ == "__main__":
    download(PAGES)
