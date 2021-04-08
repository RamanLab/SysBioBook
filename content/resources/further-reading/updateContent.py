#!/usr/bin/python3

CHAPTER_NAMES = {
"1": "Introduction to modelling",
"2": "Introduction to graph theory",
"3": "Structure of networks",
"4": "Applications of network biology",
"5": "Introduction to dynamic modelling",
"6": "Parameter estimation",
"7": "Discrete dynamic models: Boolean networks",
"8": "Introduction to constraint-based modelling",
"9": "Extending constraint-based approaches",
"10": "Perturbations to metabolic networks",
"11": "Modelling cellular interactions",
"12": "Designing biological circuits",
"13": "Robustness and evolvability of biological systems",
"14": "Epilogue: The road ahead",
"A": "Introduction to key biological concepts",
"B": "Reconstruction of biological networks",
"C": "Databases for systems biology",
"D": "Software tools compendium",
"E": "MATLAB for systems biology"
}

for chapter in CHAPTER_NAMES:
    if chapter in ["A", "B", "C", "D", "E"]:
        folder_name = "appendix-%s" % chapter
    else:
        folder_name = "chapter-%02d" % int(chapter)
    with open('%s/_index.md' % folder_name, 'w') as outfile:
        print('---', file=outfile)

        if chapter in ["A", "B", "C", "D", "E"]:
            print('weight: %d' % ord(chapter), file=outfile)
            print('bookFlatSection: false', file=outfile)
            print('title: "Appendix %s"'  % chapter, file=outfile)
        else:
            print('weight: %d' % int(chapter), file=outfile)
            print('bookFlatSection: false', file=outfile)
            print('title: "Chapter %d"'  % int(chapter), file=outfile)
        print('description: "%s"' % CHAPTER_NAMES[chapter], file=outfile)
        print('---', file=outfile)
        print('', file=outfile)
        print('# Chapter %s: %s' % (chapter, CHAPTER_NAMES[chapter]), file=outfile)
        print('', file=outfile)

with open('further-reading.tsv', 'r', errors='replace') as infile:
    lines = infile.readlines()
    for line in lines[1:]:
        print(line)
        chapter, author, year, title, journal, url, blurb = line.strip('\n').split('\t')
        author = author.strip('*')
        title = title.strip('"*')
        if chapter in ["A", "B", "C", "D", "E"]:
            folder_name = "appendix-%s" % chapter
        else:
            folder_name = "chapter-%02d" % int(chapter)
        with open('%s/_index.md' % folder_name, 'a') as outfile:
            if 'http' in url:
                if 'youtube' in url:
                    print('{{< hint danger >}}', file=outfile)
                    print('**%s**   ' % title, file=outfile)
                    print('{{< youtube %s >}}' % url.replace('http://www.youtube.com/watch?v=',''), file=outfile)
                else:
                    print('{{< hint danger >}}', file=outfile)
                    if year == '':
                        # print('**%s**   ' % title, file=outfile)
                        print('[**%s**](%s)' % (title, url), file=outfile)
                    else:
                        # print('**%s**   ' % title, file=outfile)
                        print('[**%s** (%s)](%s)' % (title, year, url), file=outfile)
                        # print('[%s (%s)](%s)' % (url, year, url), file=outfile)
            else:
                print('{{< hint info >}}', file=outfile)
                print('**%s**   ' % title, file=outfile)
                if journal == '':
                    print('[%s (%s)](http://doi.org/%s)' % (author, year, url), file=outfile)
                else:
                    print('[%s (%s) _%s_](http://doi.org/%s)' % (author, year, journal, url), file=outfile)

            print('', file=outfile)
            print(blurb.strip('"'), file=outfile)
            print('{{< /hint >}}', file=outfile)

