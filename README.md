### Network Security Project for Phising Data

Setup GitHub actions :
AWS_ACCESS_KEY_ID = 

AWS_SECRET_ACCESS_KEY = 

AWS_REGION = us-west-2

AWS_ECR_LOGIN_URI = 

ECR_REPOSITORY_NAME = 


### commands to setup the EC2 Instance :
sudo apt-get update -y
sudo apt-get upgrade

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
