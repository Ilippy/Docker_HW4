FROM python:3.9
ADD main.py .
RUN pip install requests BeautifulSoup4
CMD ["python", "./main.py"]
