import codecs
import os
import re

#换取当前文件所在目录
project_dir = os.path.dirname(os.path.abspath(__file__))
input_file=os.path.join("%s" % project_dir, "train1.txt")
output_file = os.path.join("%s" % project_dir, "train1_new.txt")

def character_tagging(input_file,output_file):
    input_data=codecs.open(input_file,'r','utf-8')
    output_data=codecs.open(output_file,'w','utf-8')
    for line in input_data.readlines():
        ner_list=line.strip().split()
        for ner in ner_list:
            word_tag=ner.split('/')
            if len(word_tag)==2:
                tag=word_tag[-1]
                word=word_tag[0]
                if tag=='o':
                    for w in word:
                        output_data.write(w+"\to\n")
                else:
                    output_data.write(word[0]+"\t"+tag+"_B\n")
                    for w in word[1:len(word)]:
                        output_data.write(w+"\t"+tag+"_I\n")
        output_data.write("\n")
    input_data.close()
    output_data.close()
character_tagging(input_file,output_file)