from random import randint
import json

#Exercise 1 – Random Sentence Generator

# def get_words_from_file(file):
#     with open(file, "r")  as choco_file :
#         all_text = choco_file.readlines() #read the file
#     return all_text
# def get_random_sentence(all_text, length):
#     the_sentence = ""
#     for i in range(length):
#         the_sentence += all_text[randint(1, len(all_text))]
#     the_sentence = the_sentence.replace("\n", " ").lower()

#     return the_sentence

# def main(file):
#     print("This program takes random words from file and creates sentence from taken words.")
#     length = int(input("Please provide desired length of sentence between 2 and 20: "))
#     if (length > 20 or length < 2):
#         print("Error, length value is not correct")
#         exit()
#     all_words = get_words_from_file(file)
#     print(get_random_sentence(all_words, length))

# main("sowpods.txt")

#Exercise 2: Working With JSON

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

json_dict = json.loads(sampleJson)
print(json_dict["company"]["employee"]["payable"]["salary"])
json_dict["company"]["employee"]["birth_date"] = "22.08.1999"

json_file = "consequence.json"
with open(json_file, "w") as file_obj:
    json.dump(json_dict, file_obj, indent= 2, sort_keys=True)