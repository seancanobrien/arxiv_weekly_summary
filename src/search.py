import arxiv
import pdb

def search_arxiv(start_date, end_date, authors=None, keywords=None, repositories=None):
    """
    Search arXiv for papers within a date range, matching authors, abstract keywords, and repositories.

    - repositories (list of str): List of repositories to search (e.g., 'math.GR', 'cs.AI').
    - authors (list of str): List of authors to match (partial matches allowed).
    - keywords (list of str): List of keywords to match in abstracts (case insensitive).

    Returns:
    - results (list of dict): List of dictionaries containing title, abstract, and URL of matching papers.
    """
    
    formatted_start_date = start_date.strftime("%Y%m%d") + "0001"
    formatted_end_date = end_date.strftime("%Y%m%d") + "2359"

    # Construct search query
    repository_query = ""
    if repositories:
        repository_query = "(" + " OR ".join([f"cat:{repo}" for repo in repositories]) + ")"

    author_query = ""
    if authors:
        author_query = "(" + " OR ".join([f"au:\"{author}\"" for author in authors]) + ")"

    title_query = ""
    if keywords:
        title_query = "(" + " OR ".join([f"ti:\"{keyword}\"" for keyword in keywords]) + ")"

    abstract_query = ""
    if keywords:
        abstract_query = "(" + " OR ".join([f"abs:\"{keyword}\"" for keyword in keywords]) + ")"

    # Combine queries with AND for the date range
    # Use submittedDate for new submissions
    query_str = f"lastUpdatedDate:[{formatted_start_date} TO {formatted_end_date}]"
    if repository_query or author_query or title_query:
        query_str += " AND ("
        if repository_query:
            query_str += repository_query + " AND ("
        if author_query or title_query:
            # join OR with non-empty queries
            query_str += " OR ".join([x for x in [author_query, title_query, abstract_query] if x])
        if repository_query:
            query_str += ")"
        query_str += ")"
    else:
        exit("No filters specified, exiting")

    # Use arxiv.Client for querying
    client = arxiv.Client(page_size=100)  # Adjust page size as needed
    search = arxiv.Search(
        query=query_str,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    
    results = []
    for result in client.results(search):
        results.append({
            "title": result.title,
            "published": result.published,
            "updated": result.updated,
            "abstract": result.summary,
            "authors": result.authors,
            "primary_category": result.primary_category,
            "all_categories": result.categories,
            "url": result.entry_id
        })
    
    return results

