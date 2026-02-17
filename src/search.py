import arxiv
import datetime
from arxivql import Query as Q
from dateutil.relativedelta import relativedelta

def search_arxiv(start_date, end_date, authors=None, keywords=None, repositories=None):
    """
    Search arXiv for papers within a date range, matching authors,
    abstract/title keywords, and repositories.
    """

    if not any([authors, keywords, repositories]):
        raise ValueError("No filters specified, exiting")

    # consider all articles submitted up to 10 years ago
    formatted_search_start_date = (start_date - relativedelta(years=10)).strftime("%Y%m%d") + "0001"
    formatted_end_date = end_date.strftime("%Y%m%d") + "2359"

    # arXiv API does NOT support lastUpdatedDate filtering.
    # Use submittedDate instead, then filter by submittedDate later
    date_query = f"submittedDate:[{formatted_search_start_date} TO {formatted_end_date}]"
    query = date_query

    # Repository filter
    repo_query = None
    if repositories:
        for repo in repositories:
            q = Q.category(repo)
            repo_query = q if repo_query is None else (repo_query | q)
        query &= repo_query

    # Author filter
    author_query = None
    if authors:
        for author in authors:
            q = Q.author(author)
            author_query = q if author_query is None else (author_query | q)

    # Keyword filter (title OR abstract)
    keyword_query = None
    if keywords:
        for keyword in keywords:
            q = Q.title(keyword) | Q.abstract(keyword)
            keyword_query = q if keyword_query is None else (keyword_query | q)

    if not (author_query is None or keyword_query is None):
        query &= (author_query | keyword_query)
    elif not author_query is None:
        query &= author_query
    elif not keyword_query is None:
        query &= keyword_query

    print(query)

    # Use arxiv.Client for querying
    client = arxiv.Client(page_size=100)  # Adjust page size as needed
    search = arxiv.Search(
        query=query,
        max_results = 200,
        sort_by=arxiv.SortCriterion.LastUpdatedDate
    )

    results = []
    for result in client.results(search):
        if start_date <= result.updated.replace(tzinfo=None):
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
