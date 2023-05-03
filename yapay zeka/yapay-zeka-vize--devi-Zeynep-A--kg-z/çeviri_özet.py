from PyPDF2 import PdfReader

reader = PdfReader("computer_science_problem1.pdf")
number_of_pages = len(reader.pages)
pages_range = range(94,126)
for page_num in pages_range:
    page = reader.pages[page_num]
    text = page.extract_text()
    #print(f"Page {page_num}: {text}")
from googletrans import Translator
translated_text=text
translator=Translator()
translate_text =translator.translate(text, dest='tr'). text
#print(translate_text)
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.tokenizers import Tokenizer
ozet=translate_text
parser = PlaintextParser.from_string(translate_text, Tokenizer("turkish"))
summarizer = TextRankSummarizer()
summary = summarizer(parser.document, sentences_count=2)
for sentence in summary:
    print(sentence)

    

