
If you have

  * <code>java</code>
  * <code>python</code>
  * <code>inkscape</code>

then running:
<pre>
python paper-keys.py --num-pages=3 --denomination=10
</pre>

...will create a folder (e.g. <code>keys-2011-05-28-13-28-49</code>) in your current directory with these files:
<pre>
addresses.txt
keys.txt
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
...
</pre>

### keys.txt
<pre>

Page 1:

    17NwoDvissrGDnKRoEtPwEPLpbcWs9NzLs
    4WAqdAN4kq8KaFnxYGEmisH84bFpVpowXJgMkDsKUSDE

    ...
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
