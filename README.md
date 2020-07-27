### acesss
ssh -i  "demo.pem" ubuntu@ec2-54-87-240-61.compute-1.amazonaws.com

ssh -L localhost:8888:localhost:8888 -i "demo.pem" ubuntu@ec2-54-87-240-61.compute-1.amazonaws.com

### share valume
sshfs ubuntu@ec2-54-87-240-61.compute-1.amazonaws.com:/home/ubuntu/transcription-api /transcribe-server/local_share -o IdentityFile=/transcribe-server/demo.pem -o allow_other


https://howchoo.com/g/ymmxmzlmndb/how-to-install-sshfs



