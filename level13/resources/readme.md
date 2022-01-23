
# Level13

```bash
gdb ./level13
```

```bash
disassemble main
```

0x0804859a <+14>: cmp    $0x1092,%eax
0x0804859f <+19>: je     0x80485cb <main+63>

```bash
disassemble main
break *main+14
run
info registers
set $eax = 4242
continue
```
