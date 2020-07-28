### ssl notebook
```
ssh -i  "demo.pem" ubuntu@ec2-52-87-193-165.compute-1.amazonaws.com
ssh -L localhost:8888:localhost:8888 -i "demo.pem" ubuntu@ec2-52-87-193-165.compute-1.amazonaws.com

ssh -i  "demo.pem" ubuntu@ec2-52-91-116-79.compute-1.amazonaws.com
ssh -L localhost:8888:localhost:8888 -i "demo.pem" ubuntu@ec2-52-91-116-79.compute-1.amazonaws.com
sudo kill -9 $(sudo lsof -t -i:8888)
```
### share valume
```
sshfs ubuntu@ec2-54-87-240-61.compute-1.amazonaws.com:/home/ubuntu/notebook kaden/aws-notebook/share -o IdentityFile=/kindom/demo.pem -o allow_other
```

https://howchoo.com/g/ymmxmzlmndb/how-to-install-sshfs


### install pip in ubuntu 18.5 wiht python 3.6

https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-18-04
```
python3.8 -m venv my_env
source my_env/bin/activate
sudo pip install pip --upgrade

```

### install spark in ubuntu

https://phoenixnap.com/kb/install-spark-on-ubuntu



### cuda
```
cat /usr/local/cuda/version.txt
gcc --version
nvcc --version
nvidia-smi
```
