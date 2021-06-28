FROM osgeo/gdal:ubuntu-full-3.2.2 AS builder-image
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt-get install --no-install-recommends -y \
    python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential && \
	apt-get clean && rm -rf /var/lib/apt/lists/*
RUN python3.9 -m venv /home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt
WORKDIR /home/myuser/app

FROM osgeo/gdal:ubuntu-full-3.2.2 AS runner-image
RUN apt update && apt-get install --no-install-recommends -y \
    python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential && \
	apt-get clean && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"
RUN useradd --create-home myuser
COPY --from=builder-image /home/myuser/venv /home/myuser/venv
COPY --from=builder-image /home/myuser/app  /home/myuser/app
RUN chmod +x $VIRTUAL_ENV/bin/activate
USER myuser
WORKDIR /home/myuser/app
COPY alembic alembic/
COPY alembic.ini alembic.ini