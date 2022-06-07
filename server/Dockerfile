FROM python

WORKDIR /userAPI
COPY userAPI.py .

RUN pip install flask

EXPOSE 8081
CMD python userAPI.py