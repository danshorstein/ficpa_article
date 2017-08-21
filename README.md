# Programming for Efficiency
This repository includes example Python code from an article written for FICPA called Programming for Efficiency. 

The examples were written in Python 3.6, and require the following libraries to be installed:

<ul>
<li>requests</li>
<li>beautiful soup</li>
<li>openpyxl</li>
</ul>

## Example one: Using Excel to prep a PBC TB for import

Take an example of a trial balance formatted like this:
<br>
![Image of Yaktocat](\images\pbc.png)

After running tb.py, the output file includes a new tab with this data:
 
![Image of Yaktocat](\images\output.png)

## Example two: Scraping the web

This simple code pulls down the authors and excerpt of their testimonial from the first three testimonials on FICPA's testimonials page.


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
The resulting output is:<br>
Author: Christopher J. Baker, CPA  — Baker DMM, LLC <br>
Excerpt: Joining the FICPA and having the chance to participate in th
-------------------------------------------------------------------
Author: Yanick J. Michel  — Y. J. Michel & Associates, PA, CPA <br>
Excerpt: I will always feel honored to be able to contribute – and be
-------------------------------------------------------------------
Author: Karena S. Thomas  — PPI Technologies GROUP <br>
Excerpt: I recently attended the 2014 University of South Florida Acc
-------------------------------------------------------------------

