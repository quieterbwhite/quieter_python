FROM centos:7
MAINTAINER blog.51cto.com/ganbing
ENV TIME_ZOME Asia/Shanghai

RUN yum -y install gcc gcc-c++ make openssl-devel pcre-devel
ADD nginx-1.17.9.tar.gz /tmp

RUN cd /tmp/nginx-1.12.1 && \
        ./configure --prefix=/usr/local/nginx && \
        make -j 2 && \
        make install

RUN rm -rf /tmp/nginx* && yum clean all && \
        echo "${TIME_ZOME}" > /etc/timezone && \
        ln -sf /usr/share/zoneinfo/${TIME_ZOME} /etc/localtime

COPY nginx.conf /usr/local/nginx/conf/
WORKDIR /usr/local/nginx/
EXPOSE 80
CMD ["./sbin/nginx","-g","daemon off;"]
