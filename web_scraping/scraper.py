import requests
import pprint
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Crime_and_Punishment"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')


def get_citations_needed_count():
    find_all_cit = soup.find_all(string = 'citation needed')
    return(len(find_all_cit))
 

def get_citations_needed_report():
    first_citation = soup.find('sup', class_="noprint Inline-Template Template-Fact")
    result_first = first_citation.parent.text
    second_citation = soup.find('a', title="Cesare Beccaria")
    result_second = second_citation.parent.text
    print('ALL PARTS THAT NEED CITATION:\n' )
    print('1.',result_first )
    print('2.',result_second)


if __name__ == '__main__':
    get_citations_needed_report()
    count = get_citations_needed_count()
    print('NUMBER OF CITATIONS NEEDED:', count)
    
    