import csv
import requests
from bs4 import BeautifulSoup


def get_url(url):
    response = requests.get(url)
    #print(response.text)
    soup = BeautifulSoup(response.text,"lxml")
    table_of_contents = soup.find("div",id="toc")
    if table_of_contents is None:
        print("table of contents empty")
        return []
    headings = table_of_contents.find_all("li")
    data = []
    if not headings:
        print("No list items present")
        return []
    else:
        for heading in headings:
            heading_text = heading.find("span",class_="toc")
            heading_number = heading.find("span",class_="toc")
            if heading_text and heading_number:    
                data.append({
                    'heading_number':heading_number,
                    'heading_text':heading_text
                    })
            else:
                print("No heading data")
    return data
def export_data(data,filename):
    with open(filename,"w",newline="") as file:
        writer = csv.DictWriter(file,fieldnames=['heading_number','heading_text'])
        writer.writeheader()
        writer.writerows(data)
def main():
    parse_url= "https://en.wikipedia.org/wiki/Python_(programming_language)"
    file = "output.csv"
    data = get_url(parse_url)
    export_data(data,file)  
if __name__=='__main__':
    main()
