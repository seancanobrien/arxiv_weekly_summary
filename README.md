# Arχiv Weekly Summaries
This creates a weekly summary of filtered content on the arxiv using the excellent [arxiv api](https://info.arxiv.org/help/api/index.html) and [this Python wrapper](https://github.com/titipata/arxivpy).
The summary is in the form of a markdown document compiled to html.

## Usage
As input, the script takes:
- A start date in `yyyy-mm-dd` format, or `t` for today.
- An end date in `yyyy-mm-dd` format, or `t` for today.
- A filter file location.
- A directory location in which to save the summary.

### Example
`python3 main.py t t location/of/filter.txt my/arxiv/summaries/`

## Virtual Environments
This script requires packages. I don't want to learn how to package these requirements in a distributable way. Instead, here are instructions for how to install these packages, which requires the use a virtual enviromnent these days.
1) Downlaod this repository.
2) Create a Python virtual environment in this directory and install the dependencies.
  - `cd location/of/this/repository/`
  - `python3 -m venv env`
  - `source env/bin/activate`
  - `pip install -r requirements.txt`
  - `deactivate`
3) Edit the filter file to your requirements. Format described below.
5) Using your virtual environment, run `main.py`.
  - `location/of/this/repository/env/bin/python3 main.py t t filter.txt my/summaries/`

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

---

# Arχiv Weekly Update
#### Mon 2024-10-07 to Sun 2024-10-13

### Search Criteria
 - **Subject categories**: math.gr, math.at, math.gt
 - **Match authors**: Jon McCammond, Ruth Charney
 - **Match abstract**: artin, coxeter, braid, maths is cool



---
### [Braid group actions on grassmannians and extended crystals of type $A$](http://arxiv.org/abs/2410.09458v1)

**Authors:** Jian-Rong Li, Euiyong Park

**Published:** 2024-10-12 09:40:57

**Last Updated:** 2024-10-12 09:40:57

**Categories:** <u>math.RT</u>, math.AG, math.GR

**Abstract:**

Let $\sigma_i$ be the braid actions on infinite Grassmannian cluster algebras
induced from Fraser's braid group actions. Let $\mathsf{T}_i$ be the braid
group actions on (quantum) Grothendieck rings of Hernandez-Leclerc category
${\mathscr C}_\mathfrak{g}^0$ of affine type $A_n^{(1)}$, and $\mathsf{R}_i$
the braid group actions on the corresponding extended crystals. In the paper,
we prove that the actions $\sigma_i$ coincide with the braid group actions
$\mathsf{T}_i$ and $\mathsf{R}_i$.


---
### [Spaces Related to Virtual Artin Groups](http://arxiv.org/abs/2410.08640v1)

**Authors:** Federica Gavazzi

**Published:** 2024-10-11 09:07:14

**Last Updated:** 2024-10-11 09:07:14

**Categories:** <u>math.GR</u>

**Abstract:**

This work explores the topological properties of virtual Artin groups, a
recent extension of the ``virtual" concept - initially developed for braids -
to all Artin groups, as introduced by Bellingeri, Paris, and Thiel. For any
given Coxeter graph $\Gamma$, we define a CW-complex $\Omega(\Gamma)$ whose
fundamental group is isomorphic to the pure virtual Artin group
$\mathrm{PVA}[\Gamma]$, which coincides with the pure virtual braid group when
$\Gamma$ is $A_{n-1}$. This construction generalizes the previously studied
BEER complex, originally defined for pure virtual braids, to all Coxeter
graphs. We investigate the asphericity of $\Omega(\Gamma)$ and demonstrate that
it holds when $\Gamma$ is of spherical type or of affine type, thereby
characterizing $\Omega(\Gamma)$ as a classifying space for
$\mathrm{PVA}[\Gamma]$. To achieve this, we establish a connection between
$\Omega(\Gamma)$ and the Salvetti complex associated with a specific Coxeter
graph $\widehat{\Gamma}$ related to $\Gamma$, showing that they share a common
covering space. This finding links the asphericity of $\Omega(\Gamma)$ to the
$K(\pi, 1)$-conjecture for Artin groups associated with $\widehat{\Gamma}$.
Additionally, the paper introduces and studies almost parabolic (AP) reflection
subgroups, which play a crucial role in constructing these complexes.


---
### [Subgroup separability of twisted right-angled Artin groups](http://arxiv.org/abs/2410.06914v1)

**Authors:** Islam Foniqi

**Published:** 2024-10-09 14:14:10

**Last Updated:** 2024-10-09 14:14:10

**Categories:** <u>math.GR</u>, math.CO

**Abstract:**

We characterise twisted right-angled Artin groups that are subgroup separable
using only their defining mixed graphs; we deduce that the group is subgroup
separable if and only if the underlying simplicial graph of the mixed graph
does not contain paths or squares in 4 vertices. Our work generalises the
results of Metaftsis - Raptis on classical right-angled Artin groups.


