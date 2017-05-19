import csv, os, sys
def parse_csv(filepath):
    resources = [['id', 'description']]
    with open(filepath, 'r') as csv_file:
        sheet = csv.DictReader(csv_file)
        for row in sheet:
            if _description_is_erroneous(row['description']):
                row['description'] = _casify_description(row['description'])
            resources.append([row['id'], row['description']])
    return resources

def create_new_csv(twod_list, path):
    with open(path, 'w') as f:
        sheet = csv.writer(f)
        for row in twod_list:
            sheet.writerow(row)


def _casify_description(description):
    sentences = description.split('.')
    cased_sentences=[]
    for sentence in sentences:
        if sentence:
            cased_sentences.append(_sentence_case(sentence))
    return ". ".join(cased_sentences) + "."


def _description_is_erroneous(description):
    words = description.split()
    return all(word[0].isupper() for word in words)

def _sentence_case(sentence):
    sentence = sentence.lower()
    words=sentence.split()
    words[0] = words[0].title()
    return " ".join(words)

def main(name, data_dir=".", data_input="test.csv", data_output="casified_data.csv"):
    filepath = os.path.join(data_dir, data_input)
    output = os.path.join(data_dir, data_output)
    resources = parse_csv(filepath)
    create_new_csv(resources, output)

if __name__ == '__main__':
    main(*sys.argv)


