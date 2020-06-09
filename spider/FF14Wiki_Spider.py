import requests
import re
import json
import os
# get every single quests search result info
def Spider_GetQuestInfo(category, type, genre, filepath):
    global num
    param_text = '{{QuestSearch|category=%s|type=%s|genre=%s}}' % (category, type, genre)
    json_url = 'https://cdn.huijiwiki.com/ff14/api.php'
    headers = {'Host': 'cdn.huijiwiki.com',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
                'Referer': 'https://ff14.huijiwiki.com/wiki/QuestSearch?category=2',
                'Origin': 'https://ff14.huijiwiki.com'}
    params = {'format': 'json',
              'action': 'parse',
              'disablelimitreport': 'true',
              'prop': 'text',
              'title': 'QuestSearch',
              'ver': '5.05.0',
              'smaxage': '86400',
              'maxage': '86400',
              'text': param_text}
    searchResult_response = requests.get(json_url, params=params, headers=headers)
    searchResult_data = searchResult_response.text
    hrefs_list = re.findall('quest-name.*?title', searchResult_data)


    urls_list = ['']
    for herf in hrefs_list:
        quest_url = ('https://ff14.huijiwiki.com/%s') % (herf.replace('quest-name\\\"><a href=\\\"', "").replace('\\\" title',""))
        if quest_url not in urls_list:
            urls_list.append(quest_url)
            print(quest_url)
            num += 1
        # get dialog info
        quest_response = requests.get(quest_url)
        questData = quest_response.text
        questName = re.findall('<title>任务:.*? ', questData)[0].replace("<title>任务:", "").replace(" ", "")
        # clean the data
        character_name = re.findall('class="quest-content-block--title qcb-icon qcb-icon-07">.*?</div>', questData)
        # only get chinese text, if jp or en needed, replace 'chs' with 'jp' or 'en'
        character_dialogue = re.findall('class="quest-content-block--text talk-content jp">.*?</div>', questData)
        # reform the data
        dialogueData = ""
        for i in range(0, len(character_name)):
            character_name[i] = character_name[i].replace('class="quest-content-block--title qcb-icon qcb-icon-07">', '').replace('</div>', '')
            character_dialogue[i] = character_dialogue[i].replace('class="quest-content-block--text talk-content jp">', '').replace('</div>', '').replace("<br />", "\n")
            dialogueData = "%s\n%s:\n%s\n" % (dialogueData, character_name[i], character_dialogue[i])

        path = '%s/[%s]%s' % (filepath, num, questName)
        filehandle = open(path, "w")
        filehandle.write(dialogueData)
        filehandle.close()
        print('%s has been written' % path)
    print(num)

def Spider_GetSeriesInfo():
    # Step1: Get the series info
    QuestSearchInit_url = 'https://ff14.huijiwiki.com/wiki/QuestSearch'
    QuestSearch_response = requests.get(QuestSearchInit_url)
    div = re.findall('{\"group_data\":.*?wgCommentsSortDescending', QuestSearch_response.text)
    SeriesData = div[0].replace(",\"wgCommentsSortDescending", "")
    # Transform the info into json
    Json_SeriesData = json.loads(SeriesData)
    ####################################################
    # Step2: join the url, category id, genre together
    ####################################################
    for key_type in Json_SeriesData['group_data']:
        for key_index in Json_SeriesData['group_data'][key_type]:
            key_name = Json_SeriesData['group_data'][key_type][key_index]
            # JSON TYPE I: id with place
            if 'place' in Json_SeriesData['category_data'][key_name]:
                for key_genre in Json_SeriesData['category_data'][key_name]['place']:
                    QuestTypeID = str(Json_SeriesData['category_data'][key_name]['type'])
                    QuestPlaceID = Json_SeriesData['category_data'][key_name]['place'][key_genre]
                    QuestPlace = Json_SeriesData['place_name_map'][str(QuestPlaceID)]
                    # create a folder named by genre/place
                    path = './Quests/%s/%s/%s' % (key_type, key_name, QuestPlace)
                    if os.path.exists(path) is True:
                        print('%s has been created!' % path)
                    else:
                        os.makedirs(path)
                    # get every single quests search result info
                    Spider_GetQuestInfo(category=key_name, type=QuestTypeID, genre=QuestPlace, filepath=path)
                continue
            # JSON TYPE II: id with genre
            if 'genre' in Json_SeriesData['category_data'][key_name]:
                for key_genre in Json_SeriesData['category_data'][key_name]['genre']:
                    QuestTypeID = str(Json_SeriesData['category_data'][key_name]['type'])
                    QuestGenreID = Json_SeriesData['category_data'][key_name]['genre'][key_genre]
                    QuestGenre = Json_SeriesData['genre_name_map'][str(QuestGenreID)]
                    # create a folder named by genre/place
                    path = './Quests/%s/%s/%s' % (key_type, key_name, QuestGenre)
                    if os.path.exists(path) is True:
                        print('%s has been created!' % path)
                    else:
                        os.makedirs(path)
                    # get every single quests search result info
                    Spider_GetQuestInfo(category=key_name, type=QuestTypeID, genre=QuestGenre, filepath=path)
                continue
            # JSON TYPE III: id only
            QuestTypeID = str(Json_SeriesData['category_data'][key_name]['type'])
            # create a folder named by category
            path = './Quests/%s/%s' % (key_type, key_name)
            if os.path.exists(path) is True:
                print('%s has been created!' % path)
            else:
                os.makedirs(path)
            Spider_GetQuestInfo(category=key_name, type=QuestTypeID, genre='0', filepath=path)





##################-Main-Body-##################
Spider_GetSeriesInfo()


