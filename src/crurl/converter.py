import subprocess

import regex


def paste_xsel():
    p = subprocess.Popen(['xsel', '-b', '-o'],
                         stdout=subprocess.PIPE, close_fds=True)
    stdout, stderr = p.communicate()
    return stdout.decode('utf-8')


def remove_punctuation(s):
    """ Strip all punctuation. """

    regularExpression = r'[\p{C} \p{M} \p{P} \p{S} \p{Z}]+'

    remove = regex.compile(regularExpression)

    return remove.sub(" ", s).strip()


def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """

    result = " ".join(s.split())  # firsly remove any multiple spaces " ".
    return new.join(result.split(old))


#  def build_file(url, urlfile):
    #  """
    #  """
    #  myfile = open(urlfile, "w", encoding='utf-8')
    #  myfile.write("[InternetShortcut]\n")
    #  myfile.write('''URL="{0}"'''.format(url))
    #  myfile.close()

def build_file(url, urlfile):
    """
    """
    with open(urlfile, mode='w', encoding='utf-8') as myfile:
        myfile.write("[InternetShortcut]\n")
        myfile.write('''URL="{0}"'''.format(url))


def build_file2(url,urlfile):
    """
    """
    with open(urlfile, mode='w', encoding='utf-8') as myfile:
        myfile.write("<html>\n")
        myfile.write("<body>\n")
        myfile.write('''<script type="text/javascript">\n''')
        myfile.write('''    window.location.href = "{0}";\n'''.format(url))
        myfile.write("</script>\n")
        myfile.write("<body>\n")
        myfile.write("<html>")


def convmv(i):
    """
    Function to produce a utf8 string.
    """
    # encode url title chars like ö converts a string to bytes
    encoded = i.encode("utf8", "ignore")
    # Decode to utf-8, convert bytes to string
    utf8str = encoded.decode("iso-8859-1")
    return utf8str
