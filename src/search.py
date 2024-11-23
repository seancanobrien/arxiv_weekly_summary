import arxiv

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
    repository_query = []
    if repositories:
        repository_query = "(" + " OR ".join([f"cat:{repo}" for repo in repositories]) + ")"

    author_query = []
    if authors:
        # It is very unclear why we do not need to  encapsulate authors full names
        # (with spaces) with %22. It is necessary for other fields. But this works fine.
        author_query = "(" + " OR ".join([f"au:%22{author}%22" for author in authors]) + ")"

    title_query = []
    if keywords:
        title_query = "(" + " OR ".join([f"ti:%22{keyword}%22" for keyword in keywords]) + ")"

    abstract_query = []
    if keywords:
        abstract_query = "(" + " OR ".join([f"abs:%22{keyword}%22" for keyword in keywords]) + ")"

    # Combine queries with AND for the date range
    # Use submittedDate for new submissions
    query_str = (f"lastUpdatedDate:[{formatted_start_date} TO {formatted_end_date}] AND " +
                    repository_query + " AND (" +
                    author_query + " OR " +
                    title_query + " OR " +
                    abstract_query + ")"
                 )

    # Use arxiv.Client for querying
    client = arxiv.Client(page_size=100)  # Adjust page size as needed
    search = arxiv.Search(
        query=query_str,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    
    results = []
    # x = client.results(search)
    # pdb.set_trace()
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

