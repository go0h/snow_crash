# Level00

```bash
getent passwd {1000..60000}
```

```bash
find / -user flag00 -perm -g=r -type f 2>/dev/null
```

```bash
ls -l /rofs/usr/sbin/john
----r--r-- 1 flag00 flag00 15 Mar  5  2016 /rofs/usr/sbin/john
```

<https://www.dcode.fr/cipher-identifier>

```bash
cat /rofs/usr/sbin/john | tr '[a-z]' '[l-za-k]'
```
