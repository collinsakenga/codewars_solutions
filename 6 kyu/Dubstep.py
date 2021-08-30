def song_decoder(txt):
    x = txt.replace("WUB", " ")
    x=x.strip()
    x=' '.join(x.split())
    return x