events {}

http {
    server {
        server_name ;
            location /text_translation/bhashini/remote/ {
                proxy_pass http://localhost:8000;
            }
            location /text_lang_detection/bhashini/remote/ {
                proxy_pass http://localhost:8001;
            }
    }
}
