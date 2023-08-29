from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
from chat.make_keyword import make_build_chain
from memory.build_memory import build_memory
from make_story.make_story import story_chain
from make_story.make_img_prompt import imgPrompt_chain

app = Flask(__name__)
CORS(app)

@app.route('/tailor/chat', methods=['POST'])
def chat():
    msgNum = int(request.json.get("msgNum"))
    msgType = request.json.get("msgType")
    sessionId = request.json.get("sessionId")
    history = request.json.get("history")
    text = request.json.get("text")

    memory = build_memory(history)
    chain = make_build_chain(memory)
    response = chain.run(text)
    AItext = response['text']
    status = response['status']
    keyword = response['keyword']
    recoKeyword = response['recoKeyword']

    result = {"msgNum":str(msgNum+1),"sessionId":sessionId, "msgType":"AI", "text":AItext, "status":status, "keyword":keyword, "recoKeyword":recoKeyword}
    return jsonify(result)


@app.route('/tailor/makeStory', methods=['POST'])
def make_story():
    keyword = request.json.get("keyword")

    chain_1 = story_chain()
    story = chain_1.run(keyword)

    chain_2 = imgPrompt_chain()
    imgPrompt = chain_2.run(story[1:])

    result = {"story":story, "imgPrompt":imgPrompt}
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')