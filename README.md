
If you have

  * <code>java</code>
  * <code>python</code> (>= 2.6)
  * <code>inkscape</code>

then running:
<pre>
python paper-keys.py --num-pages=3 --denomination=10
</pre>

...will create a folder (e.g. <code>keys-2011-05-28-13-28-49</code>) in your current directory with these files:
<pre>
addresses.txt
page1.pdf
page2.pdf
page3.pdf
</pre>

## Example

### addresses.txt
<pre>

Page 1:
    17NwoDvissrGDnKRoEtPwEPLpbcWs9NzLs
    1EzmCsa9suh4eBvSafhQzgz68MywWoFso8
    1dzhwh7sVsKRCmgWmFrmUDNumjbiuJrbg

Page 2:
    1Jr8g46M8MBLiMHTKQSQFYPKpPUr3VcjEZ
    15r8qeAFYeWceyRuwmXr8VwudU9xnnQswh
    1BoBQNRhqwAtAw7CT9SvdjEHYo6BgQ1hDo

Page 3:
    1F6aeovfoqJJKBozSJ82dmCtcRXjYQkehL
    1EyvQcprkfNhoSgd8Bn36NWZFoHnVaCqPj
    1C3MsCKDcq8KPLZFEMnzWV9wrpXwx2UJwz

</pre>

### page1.pdf

![](//github.com/bitcoin-labs/paper-keys/raw/master/documentation/page1.png)


## Private &rarr; Address
<pre>
python paper-keys.py 4WAqdAN4kq8KaFnxYGEmisH84bFpVpowXJgMkDsKUSDE
</pre>
<pre>
17NwoDvissrGDnKRoEtPwEPLpbcWs9NzLs
</pre>
