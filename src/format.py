import markdown
import re

def save_as_update_html(results, start_date, end_date, authors=None, keywords=None, repositories=None, output_file="results.html"):
    """
    Save search results to an HTML file formatted with Markdown.

    Parameters:
    - results (list of dict): Search results with title, abstract, and URL.
    - output_file (str): Name of the output HTML file.
    """

    link_formatted_repositories = [f"[{rep_cap}](https://arxiv.org/list/{rep_cap}/recent)" for rep_cap in 
                                   [f"{rep_no_cap.split('.')[0]}.{rep_no_cap.split('.')[1].upper()}" for rep_no_cap in repositories]]

    # Generate Markdown content
    md_content = "# Arχiv Weekly Update\n"
    md_content += f"#### {start_date.strftime('%a')} {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%a')} {end_date.strftime('%Y-%m-%d')}\n\n"
    md_content += "### Search Criteria\n"
    md_content += " - **Subject categories**: " + ", ".join(link_formatted_repositories)
    md_content += "\n - **Match authors**: " + ", ".join(authors)
    md_content += "\n - **Match title or abstract**: " + ", ".join(keywords)
    md_content += "\n\n\n"

    for idx, paper in enumerate(results, start=1):
        other_categories = paper['all_categories']
        other_categories.remove(paper['primary_category'])
        # only filer for math.XX type categories.
        # some are numeric, and I don't know what they mean.
        other_categories = [item for item in other_categories if "." in item]

        version_match = re.search(r'v(\d+)$', paper['url'])
        version_correctly_formatted = False
        if version_match:
            version_correctly_formatted = True
            version = version_match.group(1)

        md_content += "\n---\n"
        md_content += f"### [{paper['title']}]({paper['url']})\n\n"
        md_content += f"**Authors:** {', '.join(map(str, paper['authors']))}\n\n"
        if version_correctly_formatted:
            if version == '1':
                md_content += f"**New article, published**: {paper['published'].strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            else:
                md_content += f"**Article updated (V{version})**: {paper['updated'].strftime('%Y-%m-%d %H:%M:%S')}. **Originally published**: {paper['published'].strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        else:
            md_content += f"**Published:** {paper['published'].strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            md_content += f"**Last updated:** {paper['updated'].strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        md_content += f"**Categories:** <u>{paper['primary_category']}</u>"
        if other_categories:
            md_content += ", " + ", ".join(other_categories)
        md_content += "\n\n"
        md_content += f"**Abstract:**\n\n{paper['abstract']}\n\n"

    # message if no results were found
    if not(results):
        md_content += "\n\n---\n\n No results matched matched your filter in this date range."

    md_content += "\n\n---\n\n Thank you to arXiv for use of its open access interoperability.\n\n Link to its [API](https://info.arxiv.org/help/api/index.html), which this makes use of."
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['extra'])
    
    # Save to an HTML file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(output_file)
