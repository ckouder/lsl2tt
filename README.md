# Logical Sentential Language to Truth Table

A really simple convertor that converts LSL to truth table, help you reduce laborious work.

## Dependency

```bash
pip install regex
```

## how to use

```bash
python3 lsl2tt.py
```
## Grammar of LSL

- and => `&`
- or  => `|`
- not => `~`
- if  => `->`
- iff => `<->`

Only single English character is considered as a legal sentential variable.
Please use () to separate ambiguous LSL expressions. e.g
A & B & C will throw en error, while (A & B) & C is all fine.

Have fun and enjoy!
