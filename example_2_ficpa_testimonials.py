import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.ficpa.org/Content/Members/Member-Testimonials.aspx')
soup = BeautifulSoup(r.text, 'lxml')


testimonials = soup.find_all('div', class_='testimonial-wrapper')

for testimonial in testimonials[:3]:
    author = testimonial.find(class_='testimonial-author').get_text()
    excerpt = testimonial.get_text().lstrip()
    print('Author: {}'.format(author))
    print('Excerpt: {}'.format(excerpt[:60]))
    print('-------------------------------------------------------------------')
