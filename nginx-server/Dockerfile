# Dockerfile-nginx
FROM nginx:latest
# Nginx will listen on this port
EXPOSE 80
# Remove the default config file that
# /etc/nginx/nginx.conf includes
RUN rm /etc/nginx/conf.d/default.conf
# Add conf file
COPY nginx.conf /etc/nginx/conf.d/
COPY index.html /etc/nginx/html/