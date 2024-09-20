import pprint
import json
import sys
from os import system
import time
from utils.PDF import PDF

class Utility:

    def __init__(self) -> None:
         self.pdf = PDF()
         pass

    def generate_pdf(self, title='', author='',output_file_name='', chapters=[]):
        chap_num = 0
        
        try:
            self.pdf.set_title(title)
            self.pdf.set_author(author)
            for chapter in chapters:
                chap_num+=1
                self.pdf.print_chapter(chap_num, chapter['name'], json.dumps(chapter))
            self.pdf.output(output_file_name)
        except Exception as e:
                print(e)
        else:
                print('PDF Report Creation Complete')