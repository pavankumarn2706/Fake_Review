import requests
from bs4 import BeautifulSoup as bs
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def extract_review(request):
    if request.method == 'POST':
        url = request.POST['url']
        n = int(request.POST['n'])
        reviews=[]

# link='https://www.flipkart.com/redmi-10-power-sporty-orange-128-gb/product-reviews/itm97f5d2ec83588?pid=MOBGHDXFV9PCSYXV&lid=LSTMOBGHDXFV9PCSYXVWJIUDD&marketplace=FLIPKART'
        page = requests.get(url)
        soup = bs(page.content,'html.parser')

        # product Name
        product_name=soup.find('div',class_='_2s4DIt _1CDdy2').get_text().strip()

        # product image
        product_img=soup.find('img' ,class_="_396cs4")
        product_img=product_img.get('src')
        
        # product Price
        product_price=soup.find('div',class_='_30jeq3').get_text().strip()

        # review 
        for i in range(1, n + 1):
            page_url = url + f'&page={i}'
            page = requests.get(page_url)
            soup = bs(page.content, 'html.parser')
            review_containers = soup.find_all('div', class_='_27M-vq')
            for container in review_containers:
                title = container.find('p', class_='_2-N8zT').get_text().strip()
                content = container.find('div', class_='t-ZTKy').get_text().strip()
                content = content.replace('READ MORE', '.').strip()
                reviews.append({'title': title, 'content': content})

        context = {'reviews': reviews,'product_name':product_name,'product_img':product_img,'product_price':product_price,'url':url}
        return render(request, 'extract_review.html', context)
    else:
        return render(request, 'index.html')

