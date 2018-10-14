import nltk
from nltk import word_tokenize
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('What is URL? ')
    if len(url) < 1 : break

    # maybe put SSL thing back inside?

    #grab dat data
    print('Retrieving', url)
    urlhandle = urllib.request.urlopen(url, context=ctx)
    data = urlhandle.read().decode()
    print('Retrieved', len(data), 'characters')
    print('data type is', type(data))

    start = data.find('*** START OF THIS PROJECT GUTENBERG EBOOK')
    print("book starts at", start)
    end = data.find('*** END OF THIS PROJECT GUTENBERG EBOOK')
    print("book ends at", end)
    print("ok here we go!")
    print(data[:start])
    data = data[start:end]


    # print(data)

    #tokenizing
    tokens = nltk.word_tokenize(data)
    # print('the type of these tokens is ', type(tokens))

    # counting parts of speech
    speechParts = {}
    partList = nltk.pos_tag(tokens)
    # print(partList)
    for tuple in partList :
        speechParts[tuple[1]] = speechParts.get(tuple[1],0)+1


    #counting words
    lexicon = {}
    for token in tokens :
        token = token.lower()
        if ('project' or 'gutenberg') in token :
            continue
        lexicon[token] = lexicon.get(token,0)+1
        # itIs = nltk.pos_tag(token)
        # print(itIs)
        # print('pos_tag call produced a', type(itIs), 'of length', len(itIs))
        # print(itIs[0])
        # speechPart[itIs] = speechPart.get(itIs,0)+1
        # print('added', token, 'to the lexicon')
        # print('added', itIs, 'to the speech part count' )
        # print('count is', lexicon[token], 'for the word')

    print('(count, word) for this corpus:')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print (sorted( [ (v,k) for k,v in lexicon.items() ], reverse=True ) )
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('(count, part of speech) for this corpus:')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print (sorted( [ (v,k) for k,v in speechParts.items() ], reverse=True ) )

    # monkeying with some shit i found online
    tag_fd = nltk.FreqDist(tag for (word, tag) in partList)
    print('most common according to nltk.FreqDist are', tag_fd.most_common())
    tag_fd.plot(cumulative=True)


#
# scratch
    #
    # for line in handle:
    #     print('the line is', line)
    #     if 'Harvard' in line :
    #         print('harvard in line')
    #         continue
    #     if ('http' or 'https' or '.edu' or '.com' or '.org') in line :
    #         print('website in name')
    #         continue
    #     print('made it past the ins')
    #     sp_line = line.split()
    #     for word in sp_line:
    #         if '.' in word:
    #             cut = len(word) - 1
    #             word = word[:cut]
    #         words[word]=words.get(word,0)+1
    #
    # print (sorted( [ (v,k) for k,v in words.items() ], reverse=True ) )
