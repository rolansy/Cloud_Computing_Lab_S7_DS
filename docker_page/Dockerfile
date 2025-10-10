# Use a lightweight web server image
FROM nginx:alpine

# Copy the HTML file to the default nginx public folder
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80

# No CMD needed, nginx runs by default