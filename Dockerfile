#FROM postgres:9.5
#
#ENV POSTGRES_USER shiva
#ENV POSTGRES_PASSWORD 1
#ENV POSTGRES_DB shiva
#
#COPY bootstrap.sql /docker-entrypoint-initdb.d/10-init.sql

FROM debian:jessie
