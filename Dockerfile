FROM mambaorg/micromamba:0.15.3
USER root
RUN mkdir /opt/me_kribaat
RUN chmod -R 777 /opt/me_kribaat
WORKDIR /opt/me_kribaat
USER micromamba
COPY environment.yml environment.yml
RUN micromamba install -y -n base -f environment.yml && \
   micromamba clean --all --yes
COPY run.sh run.sh
COPY project_contents project_contents
USER root
RUN chmod a+x run.sh
CMD ["./run.sh"]