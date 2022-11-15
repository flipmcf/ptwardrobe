ARG PLONE_VERSION=6.0.0b3
FROM plone/plone-backend:${PLONE_VERSION}

LABEL maintainer="flipmcf <flipmcf@gmail.com>" \
      org.label-schema.name="playtimewardrobe-backend" \
      org.label-schema.description="playtimewardrobe backend image." \
      org.label-schema.vendor="flipmcf"

# Add local code
COPY . .

# Install local requirements and fix permissions
RUN ./bin/pip install mxdev \
    && mv requirements-docker.txt requirements.txt \
    && ./bin/mxdev -c mx.ini \
    && ./bin/pip install -r requirements-mxdev.txt \
    && chown -R plone: /app
