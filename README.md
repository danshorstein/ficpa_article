# Programming for Efficiency
This repository includes example Python code from an article written for FICPA called Programming for Efficiency. 

The examples were written in Python 3.6, and require the following libraries to be installed:

<ul>
<li>requests</li>
<li>beautiful soup</li>
<li>openpyxl</li>
<li>pandas</li>
<li>pdfplumber</li>
</ul>

## Example 1: Using Excel to prep a PBC TB for import
There are several Python libraries designed to work with Excel data, including openpyxl  and pandas . While both are very powerful and useful, openpyxl is easier to perform simple Excel tasks such as reading in, editing, and saving back to Excel.  

This example shows the use of openpyxl to read in the PBC trial balance, clean it up to be import-ready in a new tab, and save as a new file.
### Take an example of a trial balance formatted like this:
![pbc tb](https://github.com/danshorstein/ficpa_article/blob/master/images/example_1/pbc_tb.png)

### After running example_1_tb.py, the output file includes a new tab with this data:<br>
![import tb](https://github.com/danshorstein/ficpa_article/blob/master/images/example_1/output.png)

## Example 2: Scraping the web

This simple code pulls down the authors and excerpt of their testimonial from the first three testimonials on FICPA's testimonials page.

This uses the requests  and beautifulsoup  Python libraries, which are two very powerful libraries for interacting with websites.

~~~~python
import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.ficpa.org/Content/Members/Member-Testimonials.aspx')

soup = BeautifulSoup(r.text, 'lxml')

testimonials = soup.find_all('div', class_='testimonial-wrapper')

for testimonial in testimonials[:3]:
    author = testimonial.find(class_='testimonial-author').get_text()
    excerpt = testimonial.get_text().lstrip()
    print('Author: {}'.format(author))
    print('Exerpt: {}'.format(excerpt[:60]))
    print('-------------------------------------------------------------------')
~~~~
An example of resulting output is:<br>
Author: John Smith, CPA — Smith & Smith, LLC <br>
Excerpt: Joining the FICPA and having the chance to participate in th<br>
-------------------------------------------------------------------<br>
Author: Jamie J. Johnson — J. J. Johnson & Associates, PA, CPA <br>
Excerpt: I will always feel honored to be able to contribute – and be<br>
-------------------------------------------------------------------<br>
Author: Bobby L. O’Charley — Longfellow Consulting Group<br>
Excerpt: I recently attended the 2014 University of South Florida Acc<br>
-------------------------------------------------------------------<br>

## Example 3: Extracting tables from PDFs
This is one of my new favorite tools. pdfplumber can extract text, and even identify tables, from PDF files. 
This example uses the PDF file from https://www.opm.gov/policy-data-oversight/data-analysis-documentation/federal-employment-reports/reports-publications/salary-information-for-the-executive-branch.pdf

### Let's say you wanted to extract the data from this table on pg 2:
![pdf table](https://github.com/danshorstein/ficpa_article/blob/master/images/example_3/pdf_table.png)

Using the Python code in example 3, the output looks like this:
![pdf table output](https://github.com/danshorstein/ficpa_article/blob/master/images/example_3/pdf_table_csv.png)
