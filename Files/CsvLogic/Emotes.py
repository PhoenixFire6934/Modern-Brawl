import csv


class Emotes:
    def get_emotes_id():
        emotesID = []
        with open('GameAssets/csv_logic/emotes.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[1].lower() != 'true' and row[6].lower != 'true':
                        emotesID.append(line_count - 2)
                    line_count += 1

            return emotesID
