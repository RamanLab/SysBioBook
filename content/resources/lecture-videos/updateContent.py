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

with open('lecture-videos.tsv', 'r', errors='replace') as infile:
    lines = infile.readlines()
    for line in lines[1:]:
        chapter, week, vidnum, title, topic1, topic2, topic3, topic4, duration, url = line.strip('\n').split('\t')
        title = title.strip('"*')
        if chapter in ["A", "B", "C", "D", "E"]:
            folder_name = "appendix-%s" % chapter
        else:
            folder_name = "chapter-%02d" % int(chapter)
        with open('%s/_index.md' % folder_name, 'a') as outfile:
            print('{{< hint info >}}', file=outfile)
            print('**%s** (%s)  ' % (title, duration[:-3]), file=outfile)
            print(title)
            for topic in [topic1, topic2, topic3, topic4]:
                print(topic)
                if topic != "":
                    print(" - %s" % topic, file=outfile)
            print('{{< youtube %s >}}' % url.replace('https://youtu.be/',''), file=outfile)
            print('{{< /hint >}}', file=outfile)

