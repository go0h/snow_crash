
# Level02

```bash
scp -P 4242 level02@192.168.1.77:/home/user/level02/level02.pcap .
```

```bash
chmod 700 level02.pcap
```

```bash
tcpdump -qA -r level02.pcap
```

```bash
tcpdump -qA -r level02.pcap 'src 59.233.235.218 and (tcp[13] & 8!=0)' -w filtered.pcap
```

```bash
tcpflow  -l filtered.pcap -C0 > data
```

```bash
tcpflow  -l filtered.pcap -CD0 > data
```
