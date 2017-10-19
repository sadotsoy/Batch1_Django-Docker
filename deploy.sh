echo "Mandado a heroku"
sudo heroku container:login
sudo heroku container:push web --app $HEROKU_APP_NAME
echo "Se mando a heroku"
