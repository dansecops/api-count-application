FROM python:3

# Create src directory
WORKDIR /usr/src/app/

#add requirements to the project
COPY requirements.txt ./

# Install src dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8080
RUN useradd -ms /bin/bash duckcounter
USER duckcounter
CMD [ "PYTHON", "APP.PY" ]
