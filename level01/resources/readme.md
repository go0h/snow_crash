# Level01

```bash
getent passwd
```

<https://ru.wikipedia.org/wiki/John_the_Ripper>

```bash
level01@SnowCrash:~$ ls -la
total 12
dr-x------ 1 level01 level01  100 Mar  5  2016 .
```

```bash
cd /tmp
wget https://github.com/openwall/john/archive/refs/tags/1.9.0.tar.gz
tar xzvf 1.9.0.tar.gz
cd john-1.9.0/src
make generic
cd ../run
./john /etc/passwd --show
```
