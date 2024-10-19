FROM python:"3.12"

ENV PYTHONDONTWRITEBINARYCODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /books

COPY Pipfile Pipfile.lock /books/
RUN pip install pipenv && pipenv install --system

COPY . /books/