# test make_keyword

# from chat.make_keyword import make_build_chain
# from memory.build_memory import build_memory
#
# UserChat = ['start', '나는 브라키오사우루스 그림을 그렸어!', '브라키오사우루스는 초록색이구, 유치원에서 그렸어!']
# AIChat = ["안녕, 친구! 무슨 그림을 그렸어? 내게 이야기해줄래?","브라키오사우루스가 어떤 색이야? 그리고 어디에서 브라키오사우루스를 그렸어?","와! 초록색 브라키오사우루스라니! 유치원에서 그림을 그리는 건 어떤 기분이었어?",]
#
# history = {'UserChat':UserChat,'AIChat':AIChat}
# memory = build_memory(history)
#
# chain = make_build_chain(memory)
# print(chain.run('너무너무 재밌었어!!'))

# test make_story

# from make_story.make_story import story_chain
#
# keyword = ["브라키오사우루스", "초록색", "유치원", "재미있게", "그림"]
#
# chain = story_chain()
# print(chain.run(keyword))

# test img_prompt

from make_story.make_img_prompt import imgPrompt_chain

story = ['옛날옛날에, 매우 큰 브라키오사우루스가 있었습니다. 이 브라키오사우루스는 머리까지 이르는 멋진 초록색 피부를 가지고 있었어요.','브라키오사우루스는 자신의 유치원을 가지고 있었습니다. 그 유치원은 그림 그리기, 노래 부르기, 놀이하면서 재미있게 지내는 곳이었어요.','어린 동물들은 브라키오사우루스의 유치원에서 재미있게 놀면서 많은 것을 배웠습니다. 그들은 그림을 그리며 브라키오사우루스의 멋진 초록색 피부를 그렸어요.','그래서 브라키오사우루스의 유치원은 언제나 즐거움으로 가득 찼습니다. 그리고 모든 동물들이 브라키오사우루스와 그의 유치원을 사랑하게 되었답니다.']

chain = imgPrompt_chain()
print(chain.run(story))