import json
import xml.etree.ElementTree as ET

def read_xml_list(filename):
    news_list = []
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(filename, parser)
    root = tree.getroot()
    xml_items = root.findall('channel/item')
    for item in xml_items:
        all_news = (item.find('description').text).split()
        news_list.append(all_news)
    return news_list

def read_json_list(filename):
    news_list = []
    with open(filename, 'r', encoding='utf8') as file:
        news_file = json.load(file)
    news_temp = [news_file['rss']['channel']['items']]
    for news_name in news_temp:
        for name in news_name:
            all_news = name['description'].split()
            news_list.append(all_news)
    return news_list

def get_worlds_list(raw_words_list):
    clear_words_list = []
    news_list = read_json_list('newsafr.json') # Менять xml и json
    for list_word in news_list:
        for word in list_word:
            if len(word) > 6:
                clear_words_list.append((word.capitalize().strip()))
    return clear_words_list

def calculate_words():
    words_dict = {}
    result_list = []
    raw_words_list = get_worlds_list(read_json_list('newsafr.json')) # Менять xml и json
    for word in raw_words_list:
        words_dict.setdefault((word), [])
        words_dict[word].append(1)
    for words in words_dict.items():
        words_dict[words[0]] = [sum(words[1])]
    sort_words = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
    for words in sort_words[0:9]:
        result_list.append(words[0])
    return f'ТОП 10, самых часто встречающихся слов, больше 6 символов:{result_list}'

def start():# Менять xml и json
    result_from_json = calculate_words()
    print(result_from_json)

if __name__ == '__main__':
    start()