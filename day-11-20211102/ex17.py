import sys
script,endcoding,error = sys.argv

def main(language_file,encoding,errors):
  line = language_file.readline()
  if line:
    print_line(line,encoding,errors)
    return main(language_file,encoding,errors)

def print_line(line,encoding,errors):
  next_lang = line.strip()
  raw_bytes = next_lang()