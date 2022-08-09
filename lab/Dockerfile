FROM python:alpine3.6

# Copy the *.py files from current folder to container's /app folder
COPY ./*.py /

# Copy the Pipfile from current folder to container's /app folder
COPY ./requirements.txt /

# Install flask
RUN pip install -r requirements.txt

# Expose port 8080
EXPOSE 8080

ENTRYPOINT [ "python3" ]

CMD [ "myapp.py" ]
