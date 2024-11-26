# Arχiv Weekly Summaries
This creates a weekly summary of filtered content on the arxiv using the excellent [arxiv api](https://info.arxiv.org/help/api/index.html) and [this Python wrapper](https://github.com/titipata/arxivpy).
The summary is in the form of a markdown document compiled to html.

## Usage
As input, the script takes:
- A start date in `yyyy-mm-dd` format, or `t` for today.
- An end date in `yyyy-mm-dd` format, or `t` for today.
- A filter file location.
- A directory location in which to save the summary.

The script then:
 - Finds every week (set of 7 concurrent days starting on a Monday and ending on a Sunday) that intersects $[\text{start date}, \text{end date}]$. Denote this set of weeks $S$.
 - Produces a summary for every week preceeding a week in $S$.
In partiular, to produce a summary for last week, input `t` for the start and end date.

### Example

`python3 main.py t t location/of/filter.txt my/arxiv/summaries/`

`python3 main.py 2024-11-11 2024-11-20 location/of/filter.txt my/arxiv/summaries/`

The second example will produce two summaries. One for the week beginning Monday the 4th of November, and one for the week beginning Monday the 11th of November.

## Virtual Environments
This script requires packages. I don't want to learn how to package these requirements in a distributable way. Instead, here are instructions for how to install these packages, which requires the use a virtual enviromnent these days.
1) Downlaod this repository.
2) Create a Python virtual environment in this directory and install the dependencies.
  - `cd location/of/this/repository/`
  - `python3 -m venv env`
  - `source env/bin/activate`
  - `pip install -r requirements.txt`
  - `deactivate`
3) Using your virtual environment, run `main.py`.
  - `location/of/this/repository/env/bin/python3 main.py t t filter.txt my/arxiv/summaries/`

## Filter file format
The filter file has a simple format described below.
```
# Comment lines that are ignored
REPOSITORIES:
math.gr
math.at

AUTHORS:
Jon McCammond
Ruth Charney
# Hyphens and potentially other symbols should be substituted for underscores.
Rose Morris_Wright

KEYWORDS:
artin
coxter
braid
maths is cool
```
The filtering works as follows:
- Only papers submitted to (or cross posted to) at least one of the listed repositories will be included.
- If a paper is authored (or co-authored) by at least one of the listed authors, it will be included.
- If a paper contains at least one of the keywords (which can also be key phrases) in the title or abstract, it will be included.
- A paper does not need to match authors and keywords to be included. If it just matches an author, or just matches a keyword, it will be included.
- Capitalisation and diacritics are ignored (as far as I can tell).

# Example output

The output will not render tex as it does in github markdown.

# Arχiv Weekly Update
#### Mon 2024-10-07 to Sun 2024-10-13

### Search Criteria
 - **Subject categories**: math.gr, math.at, math.gt
 - **Match authors**: Jon McCammond, Ruth Charney, Rose Morris_Wright
 - **Match abstract**: artin, coxeter, braid, maths is cool

---
### [2-dimensional Shephard groups](http://arxiv.org/abs/2411.15434v1)

**Authors:** Katherine Goldman

**New article, published**: 2024-11-23 03:34:59

**Categories:** <u>math.GR</u>, math.AT, math.MG

**Abstract:**

The 2-dimensional Shephard groups are quotients of 2-dimensional Artin groups
by powers of standard generators. We show that such a quotient is not
$\mathrm{CAT}(0)$ if the powers taken are sufficiently large. However, for a
given 2-dimensional Shephard group, we construct a $\mathrm{CAT}(0)$ piecewise
Euclidean cell complex with a cocompact action (analogous to the Deligne
complex for an Artin group) that allows us to determine other non-positive
curvature properties. Namely, we show the 2-dimensional Shephard groups are
acylindrically hyperbolic (which was known for 2-dimensional Artin groups), and
relatively hyperbolic (which most Artin groups are known not to be). As an
application, we show that a broad class of 2-dimensional Artin groups are
residually finite.


---
### [On the twisted conjugacy problem for large-type Artin groups](http://arxiv.org/abs/2411.05493v2)

**Authors:** Martín Blufstein, Motiejus Valiunas

**Article updated (V2)**: 2024-11-18 20:49:50. **Originally published**: 2024-11-08 11:51:19

**Categories:** <u>math.GR</u>

**Abstract:**

We show that the twisted conjugacy problem is solvable for large-type Artin
groups whose outer automorphism group is finite, generated by graph
automorphisms and the global inversion. This includes XXXL Artin groups whose
defining graph is connected, twistless, and not an even edge; and large-type
Artin groups whose defining graph admits a twistless hierarchy terminating in
twistless stars.


---

 Thank you to arXiv for use of its open access interoperability.

 Link to its [API](https://info.arxiv.org/help/api/index.html), which this makes use of.


