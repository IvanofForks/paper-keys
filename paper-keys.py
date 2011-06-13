from __future__ import with_statement
import datetime, os, subprocess, optparse
import simplejson as json
from PyQRNative import QRCode, QRErrorCorrectLevel

def main():
  
  parser = optparse.OptionParser()
  parser.add_option('-d', '--denomination', dest='denomination', default="")
  parser.add_option('-n', '--num-pages', dest='n', default=1)
  options, args = parser.parse_args()
  n = int(options.n)
  assert n >= 1
  denomination = options.denomination
  
  if len(args) == 1:
    print run_keytool('--address-of-priv58', args[0])
  else:
    keys = gen_keys(3 * n)
    addr_lines = []
    key_lines = []
    
    dirPath = 'keys-' + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    subprocess.check_call(['mkdir', '-p', dirPath])
    for i in range(n):
      pageKeys = keys[3 * i : 3 * i + 3]
      pageNum = i + 1
      savePage(pageKeys, denomination, "%s/page%d" % (dirPath, pageNum))
      addr_lines.append("\nPage %d:\n" % pageNum)
      key_lines.append("\nPage %d:\n" % pageNum)
      for key in pageKeys:
        addr_lines.append("    %s\n" % key['address'])
        
        key_lines.append("\n    %s\n" % key['address'])
        key_lines.append("    %s\n" % key['priv58'])
    
    with open("%s/addresses.txt" % dirPath, "wb") as f:
      f.write(''.join(addr_lines).encode('utf-8'))
    
    with open("%s/keys.txt" % dirPath, "wb") as f:
      f.write(''.join(key_lines).encode('utf-8'))


def findInkscape():
  macPath = "/Applications/Inkscape.app/Contents/Resources/bin/inkscape"
  if os.path.isfile(macPath):
    return macPath
  else:
    return "inkscape"


def savePage(keys, denomination, pathPrefix):
  svg = draw_3up(keys, denomination)
  with open("%s.svg" % pathPrefix, "wb") as f:
    f.write(svg.encode('utf-8'))
  subprocess.check_call([findInkscape(), '--export-pdf=%s.pdf' % pathPrefix, '%s.svg' % pathPrefix])


def compile_keytool():
  subprocess.check_call(['javac', 'KeyTool.java', '-cp', 'bitcoinj.jar'])


def run_keytool(*args):
  out, err = (subprocess
                .Popen(['java', '-classpath', './bitcoinj.jar:./', 'KeyTool'] + list(args),
                    stdout=subprocess.PIPE)
                .communicate())
  return out


def gen_keys(n):
  j = run_keytool('--gen-keys', str(n))
  return json.loads(j)['keys']


def f2s(x):
  return "%.17f" % x


def draw_3up(keys, denomination):
  
  assert len(keys) == 3
  
  layout = 'portrait'
  padding = 25
  
  if layout == 'portrait':
    w = 210 - (2 * padding)
    h = 279 - (2 * padding)
  elif s.layout == 'landscape':
    w = 279 - (2 * padding)
    h = 210 - (2 * padding)
  
  ones = []
  for i in range(len(keys)):
    key = keys[i]
    x = 31.428572
    y = 29.988726 + 280 * i
    ones.append(drawOne(key, x, y, denomination))
  
  return '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
  <svg
      width="''' + f2s(w) + '''mm"
      height="''' + f2s(h) + '''mm"
      
      xmlns:dc="http://purl.org/dc/elements/1.1/"
      xmlns:cc="http://creativecommons.org/ns#"
      xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
      xmlns:svg="http://www.w3.org/2000/svg"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
      xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
      
      version="1.1">
    
    ''' + ''.join(ones) + '''
    
  </svg>
  '''


def drawOne(key, x, y, denomination):
  
  address_qr_text = "http://blockexplorer.com/address/%s" % key['address']
  priv_qr_text =  "bitcoin-keys:%s" % key['priv58']
  #bitcoin-keys:4fkXomSL5mW7grJxKVCDGdXGTvR8MEBBuBhUekNaZp2D
  #http://blockexplorer.com/address/1AeBTeqmogerKsroxDQKmwar8PfukY6LG8
  
  return '''
      <rect
       style="fill:none;stroke:#000000;stroke-width:3.2615025;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none"
       id="rect2984"
       width="514.28571"
       height="191.53462"
       x="''' + f2s(x) + '''"
       y="''' + f2s(y) + '''"
       ry="32.524746" />
  
  ''' + text_to_qrSvg(address_qr_text, x + 18.6, y + 25, 147) + '''
  
  ''' + text_to_qrSvg(priv_qr_text, x + 345.6, y + 25, 147) + '''
  
  <text
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
       x="''' + f2s(x + 254 - 31.4) + '''"
       y="''' + f2s(y + 124.80526 - 29.9) + '''"
       id="text3795"
       sodipodi:linespacing="125%"><tspan
         sodipodi:role="line"
         id="tspan3797"
         x="''' + f2s(x + 254 - 31.4) + '''"
         y="''' + f2s(y + 124.80526 - 29.9) + '''"
         style="font-size:56px;font-style:normal;font-variant:normal;font-weight:500;font-stretch:normal;text-align:start;line-height:221.00000381%;writing-mode:lr-tb;text-anchor:start;font-family:Ubuntu;-inkscape-font-specification:Ubuntu Medium">''' + denomination + '''</tspan></text>
    
    
    <text
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
       x="''' + f2s(x + 224.85713 - 31.4) + '''"
       y="''' + f2s(y + 184.88649 - 29.9) + '''"
       id="text3834"
       sodipodi:linespacing="125%"><tspan
         sodipodi:role="line"
         id="tspan3836"
         x="''' + f2s(x + 224.85713 - 31.4) + '''"
         y="''' + f2s(y + 184.88649 - 29.9) + '''"
         style="font-size:40px;font-style:italic;font-variant:normal;font-weight:500;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Ubuntu;-inkscape-font-specification:Ubuntu Medium Italic">Bitcoin</tspan></text>
  '''


def qr_version_for_h(text):
  n = len(text)
  if n > 119:   raise Exception("Too much text")
  if n > 98:    return 10
  if n > 84:    return 9
  if n > 64:    return 8
  if n > 58:    return 7
  if n > 44:    return 6
  if n > 34:    return 5
  if n > 24:    return 4
  if n > 14:    return 3
  if n > 7:     return 2


def text_to_qrSvg(text, left = 0, top = 0, width = 100):
  
  qr = QRCode(qr_version_for_h(text), QRErrorCorrectLevel.H)
  qr.addData(text)
  qr.make()
  
  size = float(width) / qr.getModuleCount()
  antigapFactor = 1.05
  
  arr = []
  for y in range(qr.getModuleCount()):
    for x in range(qr.getModuleCount()):
      if qr.isDark(y, x):
        arr.append(
            '<rect x="' + f2s(left + x * size) +
            '" y="' + f2s(top + y * size) +
            '" width="' + f2s(size * antigapFactor) +
            '" height="' + f2s(size * antigapFactor) +
            '" fill="#000000" />\n')
  
  return ''.join(arr)


if __name__ == '__main__':
  main()

