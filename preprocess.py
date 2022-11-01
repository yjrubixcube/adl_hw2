import json

old = open("./kag/valid.json", 'r')
context = open("./kag/context.json", 'r')
new = open("./kag/new_valid.json", 'w')

data = json.load(old)
old.close()

context = json.load(context)
# print(context[0])

new_json = []

for batch in data:
    # print(batch)
    new_batch = {
        "id": batch["id"],
        "ending0": context[batch["paragraphs"][0]],
        "ending1": context[batch["paragraphs"][1]],
        "ending2": context[batch["paragraphs"][2]],
        "ending3": context[batch["paragraphs"][3]],
        "label": batch["paragraphs"].index(batch['relevant']), 
        # "startphrase": batch["question"]
        "sent1": batch["question"],
        "sent2": batch["question"]
    }
    new_json.append(new_batch)
    # break

json.dump(new_json, new)

new.close()