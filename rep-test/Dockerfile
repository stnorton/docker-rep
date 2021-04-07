FROM rocker/r-ver:4.0.3
WORKDIR /replication 
COPY . . 
RUN Rscript install_packages.R rpacks.txt
RUN Rscript runscript.R