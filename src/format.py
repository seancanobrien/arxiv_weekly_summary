import markdown
import re

def save_as_update_html(results, start_date, end_date, authors=None, keywords=None, repositories=None, output_file="results.html"):
    """
    Save search results to an HTML file formatted with Markdown.

    Parameters:
    - results (list of dict): Search results with title, abstract, and URL.
    - output_file (str): Name of the output HTML file.
    """
    # Generate Markdown content
    md_content = "# Arχiv Weekly Update\n"
    md_content += f"#### {start_date.strftime('%a')} {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%a')} {end_date.strftime('%Y-%m-%d')}\n\n"
    md_content += "### Search Criteria\n"
    md_content += " - **Subject categories**: " + ", ".join(repositories)
    md_content += "\n - **Match authors**: " + ", ".join(authors)
    md_content += "\n - **Match abstract**: " + ", ".join(keywords)
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

    md_content += "---\n\n Thank you to arXiv for use of its open access interoperability.\n\n Link to its [API](https://info.arxiv.org/help/api/index.html), which this makes use of."
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['extra', 'pymdownx.arithmatex'])

    # MathJax 3 script
    mathjax_script = """
    <script>
    window.MathJax = {
      options: {
        ignoreHtmlClass: 'tex2jax_ignore',
        processHtmlClass: 'tex2jax_process',
        renderActions: {
          find: [10, function (doc) {
            for (const node of document.querySelectorAll('script[type^="math/tex"]')) {
              const display = !!node.type.match(/; *mode=display/);
              const math = new doc.options.MathItem(node.textContent, doc.inputJax[0], display);
              const text = document.createTextNode('');
              const sibling = node.previousElementSibling;
              node.parentNode.replaceChild(text, node);
              math.start = {node: text, delim: '', n: 0};
              math.end = {node: text, delim: '', n: 0};
              doc.math.push(math);
              if (sibling && sibling.matches('.MathJax_Preview')) {
                sibling.parentNode.removeChild(sibling);
              }
            }
          }, '']
        }
      }
    };
    </script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
    """

    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {mathjax_script}
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Save to an HTML file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(output_file)
