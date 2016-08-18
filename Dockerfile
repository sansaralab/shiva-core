FROM postgres:9.5

ENV POSTGRES_USER shiva
ENV POSTGRES_PASSWORD 1
ENV POSTGRES_DB shiva

#RUN /bin/su - postgres -c "createdb shivadb"
#RUN /bin/su - postgres -c "psql -c \"CREATE USER shiva WITH LOGIN CREATEDB PASSWORD '1';\""