FROM rackspacedot/python37
WORKDIR /usr/local/kmsBackend
COPY * /usr/local/kmsBackend/
CMD /bin/bash
RUN chmod +x ./install.sh \
	&& mkdir /mnt/uwsgi
RUN ./install.sh
EXPOSE 5000/tcp
CMD python app.py