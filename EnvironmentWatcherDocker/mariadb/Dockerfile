FROM mariadb:latest

RUN touch /var/log/mysql/mysqld.log

COPY init.sql /docker-entrypoint-initdb.d/
COPY my.cnf /etc/mysql/conf.d/my.cnf
RUN chmod 644 /etc/mysql/my.cnf

#FROM mariadb:latest
#
#COPY ./init.sql /docker-entrypoint-initdb.d/
#
#VOLUME [ "/var/lib/mysql" ]
